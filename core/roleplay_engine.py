"""
RGFLAT Core - RoleplayEngine v3 (Refactored)

Central orchestrator for the roleplay system.
"""

from typing import Optional, Dict, Any, Callable, List
from dataclasses import dataclass, field
import uuid

# Core imports
try:
    from .parameters import RoleplayConfig
except ImportError:
    from core.parameters import RoleplayConfig

# Updated imports for new package structure
from memory.memory_system import MemorySystem
from prompts.prompt_builder import MemoryAwarePromptBuilder, LocalPromptPoetV2
from adapters.waidrin_adapter import WaidrinAdapterV2


class RoleplayEngine:
    """
    Advanced Unified Roleplay Engine v3 (Core)
    """

    def __init__(self, config: RoleplayConfig):
        self.config = config
        self.session_id = str(uuid.uuid4())[:8]
        self.memory = MemorySystem()
        self.components: Dict[str, Any] = {}
        self.hooks: Dict[str, List[Callable]] = {}
        self.session_history: List[Dict] = []
        self.state: Dict[str, Any] = {"turn": 0}

        self._setup_default_components()
        self._initialize_session()

    def _setup_default_components(self):
        self.components["prompt_builder"] = MemoryAwarePromptBuilder(
            self.memory, LocalPromptPoetV2()
        )
        self.components["waidrin_adapter"] = WaidrinAdapterV2(self.memory)

    def _initialize_session(self):
        waidrin = self.components.get("waidrin_adapter")
        if waidrin:
            waidrin.initialize_session(self.config.character_name)
        if self.config.debug:
            print(f"[RoleplayEngine] Session {self.session_id} started")

    # ====================== PLUGIN SYSTEM ======================

    def register_component(self, name: str, component: Any):
        self.components[name] = component
        if self.config.debug:
            print(f"[RoleplayEngine] Component registered: {name}")

    def get_component(self, name: str) -> Any:
        return self.components.get(name)

    # ====================== BEHAVIOR TREE SUPPORT ======================

    def register_behavior_tree(self, name: str, behavior_tree):
        self.components[f"bt_{name}"] = behavior_tree
        if self.config.debug:
            print(f"[RoleplayEngine] Behavior Tree registered: {name}")

    def run_behavior_tree(self, name: str, context: Dict = None, debug: bool = False):
        bt = self.components.get(f"bt_{name}")
        if not bt:
            raise ValueError(f"Behavior Tree '{name}' not found")
        ctx = context or {"character": self.config.character_name}
        if debug:
            return bt.debug_tick(ctx, verbose=True)
        return bt.tick(ctx)

    def visualize_behavior_tree(self, name: str):
        bt = self.components.get(f"bt_{name}")
        if bt:
            print(f"\n=== Behavior Tree: {name} ===")
            bt.print_tree()
        else:
            print(f"Behavior Tree '{name}' not found")

    def get_behavior_tree_status(self, name: str):
        bt = self.components.get(f"bt_{name}")
        return bt.get_tree_status() if bt else None

    # ====================== HYBRID AI SUPPORT ======================

    def register_hybrid_selector(self, name: str, utility_selector):
        self.components[f"hybrid_{name}"] = utility_selector
        if self.config.debug:
            print(f"[RoleplayEngine] Hybrid Selector registered: {name}")

    def run_hybrid_decision(self, name: str, context: Dict = None, debug: bool = False):
        selector = self.components.get(f"hybrid_{name}")
        if not selector:
            raise ValueError(f"Hybrid Selector '{name}' not found")
        ctx = context or {"character": self.config.character_name}
        from ai.hybrid_ai import run_hybrid_decision as run_hybrid
        return run_hybrid(selector, ctx, debug=debug)

    # ====================== EVENT / HOOK SYSTEM ======================

    def on(self, event: str, callback: Callable):
        if event not in self.hooks:
            self.hooks[event] = []
        self.hooks[event].append(callback)

    def _emit(self, event: str, data: Any = None):
        for callback in self.hooks.get(event, []):
            callback(self, data)

    # ====================== REAL GROK LLM INTEGRATION ======================

    def _call_grok_api(self, prompt: str, system_prompt: str = None) -> str:
        import os
        import requests

        api_key = os.getenv("XAI_API_KEY") or os.getenv("GROK_API_KEY")
        if not api_key:
            if self.config.debug:
                print("[RoleplayEngine] No XAI_API_KEY found — falling back to placeholder")
            return None

        url = "https://api.x.ai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        payload = {
            "model": self.config.grok_model,
            "messages": messages,
            "temperature": 0.85,
            "max_tokens": 800,
            "stream": False
        }

        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            if self.config.debug:
                print(f"[RoleplayEngine] Grok API error: {e}")
            return None

    # ====================== CORE METHODS ======================

    def add_memory(self, content: str, importance: float = 5.0,
                   emotion: str = "neutral", intensity: float = 0.5,
                   tags: List[str] = None, memory_type: str = "event"):
        entry = self.memory.add_memory(
            content=content,
            importance=importance,
            emotion=emotion,
            emotional_intensity=intensity,
            tags=tags or [],
            memory_type=memory_type,
            character=self.config.character_name
        )
        self._emit("memory_added", entry)
        return entry

    def update_relationship(self, other_character: str, **kwargs):
        self.memory.update_relationship(self.config.character_name, other_character, **kwargs)

    def step(self, user_input: str, use_waidrin: bool = False, use_real_llm: bool = None) -> Dict[str, Any]:
        self.state["turn"] += 1
        self.add_memory(content=f"User: {user_input}", importance=4.0)

        prompt_builder = self.components["prompt_builder"]
        full_prompt = prompt_builder.build_prompt(
            character_name=self.config.character_name,
            user_input=user_input,
            scenario=self.config.scenario,
            setting=self.config.setting,
            mood=self.config.mood,
            query_for_memories=user_input,
            limit_memories=self.config.max_memories_in_prompt
        )

        should_use_llm = use_real_llm if use_real_llm is not None else self.config.use_real_llm

        if use_waidrin:
            waidrin = self.components.get("waidrin_adapter")
            context = waidrin.get_context_for_waidrin(user_input) if waidrin else {}
            response = f"[Waidrin response with {len(context.get('memories', []))} memories]"
        elif should_use_llm:
            system_context = f"You are {self.config.character_name}. Stay fully in character."
            real_response = self._call_grok_api(full_prompt, system_context)
            if real_response:
                response = real_response
                if self.config.debug:
                    print("[RoleplayEngine] Used real Grok LLM response")
            else:
                response = f"[{self.config.character_name}] {user_input}... (LLM call failed — placeholder)"
        else:
            response = f"[{self.config.character_name}] {user_input}... (response)"

        turn_result = {
            "turn": self.state["turn"],
            "user_input": user_input,
            "response": response,
            "used_real_llm": should_use_llm and response and not response.startswith("[")
        }
        self.session_history.append(turn_result)
        self._emit("turn_complete", turn_result)
        return turn_result

    def get_context(self) -> Dict:
        return {
            "session_id": self.session_id,
            "config": self.config,
            "state": self.state,
            "memory": self.memory.to_dict(),
            "components": list(self.components.keys()),
            "turns": len(self.session_history)
        }

    def save(self, path: Optional[str] = None):
        path = path or self.config.save_path
        self.memory.save(path)

    def load(self, path: Optional[str] = None):
        path = path or self.config.save_path
        self.memory.load(path)

    def __repr__(self):
        return f"<RoleplayEngine id={self.session_id} turns={len(self.session_history)}>"
