# 🎭 RGFLAT - RoleplayGenerator v1.2 (Fixed & Runnable Edition)

**Advanced Roleplay Engine with Memory, Behavior Trees & Hybrid AI**  
**Updated & Fixed: May 2026**  
**Core:** `RoleplayEngine v3` + `MemorySystem v1.2`

> **Note:** This is the **fixed and runnable version** of the original repository. Import paths, missing methods, and module references have been corrected for immediate execution in a flat Python structure. Original repo had broken imports and incomplete methods.

---

## ✨ Key Features (All Fully Operational)

### Core Systems
- **RoleplayEngine v3** — Unified orchestrator, plugin/hooks system, session management
- **MemorySystem v1.2** — Emotional tagging + intensity, relationship graph, decay (with emotional persistence), automatic clustering, save/load persistence
- **Behavior Tree System** — Full support (Sequence, Selector, Parallel, Decorator, Memory/Physics-aware nodes)
- **Hybrid AI** — Utility AI + Behavior Trees for dynamic decision making
- **MemoryAwarePromptBuilder + Prompt Poet v2** — Automatic injection of memories, relationships, emotional context into prompts (Jinja2 templating)

### Integrations
- **WaidrinAdapterV2** — Deep bidirectional integration with Waidrin state machine + rich context
- **Preset system** — Vampire, Tsundere, Teacher, Yandere + easy custom
- **Character/Dialogue/Scenario Generators** + Multi-Character support + Consistency checker

### Interfaces
- **CLI** with interactive mode + one-shot + debug
- **Basic Web UI** (index.html) for parameter tweaking and prompt preview
- Full Python API for extension

---

## 🚀 Quick Start (No Installation Needed Beyond Python + jinja2)

```bash
# Clone or download this fixed version
cd RGFLAT

# One-shot example
python cli.py --preset dominant_vampire --message "Hello there, stranger..."

# Interactive mode
python cli.py --preset tsundere_rival

# With Waidrin integration
python cli.py --preset strict_teacher --use-waidrin --debug
```

**Requirements:** Python 3.8+ (jinja2 is optional but recommended for full prompt templating — already present in most environments).

---

## 📦 Installation (Fixed Version)

1. Download the ZIP or clone the fixed repo.
2. No `pip install` required for core functionality.
3. Run directly from the folder.

**Original (broken) clone command fixed here** — this version runs out-of-the-box.

---

## 🧠 Architecture Overview

```
RoleplayEngine
├── MemorySystem v1.2          (emotional + relational + persistent)
├── Prompt Poet v2 + MemoryAwarePromptBuilder
├── WaidrinAdapterV2
├── Behavior Trees + Hybrid AI (UtilitySelector)
├── Generators (Character, Dialogue, Scenario)
└── Consistency + RoleplayPhysics
```

---

## 📁 Project Structure (Complete Fixed Edition)

```
RGFLAT/
├── cli.py                      # Main entry point (interactive + one-shot)
├── roleplay_engine.py          # Core engine v3 (fixed imports)
├── memory.py                   # MemorySystem v1.2 + added missing methods
├── prompt_poet_local.py        # Prompt Poet v2 + MemoryAwarePromptBuilder
├── waidrin_adapter.py          # WaidrinAdapterV2 (renamed for compatibility)
├── presets.py                  # 4+ ready presets (fixed import)
├── parameters.py               # RoleplayParameters dataclass
├── behavior_tree.py            # Full BT system + example NPC tree
├── hybrid_ai.py                # Utility AI + hybrid runner
├── character_generator.py
├── consistency.py
├── dialogue_generator.py
├── multi_character.py
├── roleplay_physics.py
├── scenario_generator.py
├── index.html                  # Basic web UI
├── css/style.css
├── js/main.js
└── README.md                   # This file (updated)
```

---

## 🔧 Advanced Usage Examples

```python
from roleplay_engine import RoleplayEngine, RoleplayConfig
from presets import load_preset

config = RoleplayConfig(character_name="Elias Voss", debug=True)
engine = RoleplayEngine(config)

# One turn
result = engine.step("You're late again...", use_waidrin=False)
print(result["response"])

# Add memory manually
engine.add_memory("User confessed feelings", importance=8.0, emotion="desire", intensity=0.9)

# Save session
engine.save("my_session.json")
```

**Behavior Tree + Hybrid AI:**
```python
from behavior_tree import create_example_npc_tree
from hybrid_ai import UtilitySelector, UtilityAction

# Register and run (see full examples in source)
```

---

## 📌 Changes in This Fixed Edition
- All `core.` imports removed → flat module imports
- `prompt_poet_v2` → `prompt_poet_local.py`
- `waidrin_adapter_v2` → `waidrin_adapter.py`
- Added 3 missing methods to `MemorySystem` (get_lore_context, _get_emotional_summary, get_context_for_waidrin)
- README completed with accurate structure and instructions
- __pycache__ cleaned
- Ready for immediate use and further extension (add real LLM in `step()` or `build_prompt()`)

---

---

## 🤖 Real Grok LLM Integration (NEW in v1.2 Fixed)

This version now supports **real responses from Grok** (xAI)!

### How to use:
```bash
# Set your xAI API key (get free key at https://console.x.ai)
export XAI_API_KEY="your_key_here"

# Run with real Grok
python cli.py --preset dominant_vampire --use-real-llm --message "Tell me about your past..."

# Or in interactive mode
python cli.py --preset tsundere_rival --use-real-llm
```

### In Python code:
```python
config = RoleplayConfig(
    character_name="Elias Voss",
    use_real_llm=True,           # Enable Grok
    grok_model="grok-2-1212"     # or "grok-beta"
)
engine = RoleplayEngine(config)
result = engine.step("I love you...", use_real_llm=True)
print(result["response"])   # Real Grok-generated reply!
```

**Requirements:** `requests` (usually pre-installed) + valid `XAI_API_KEY`.

The full rich prompt (with memories, relationships, emotional state) is automatically sent to Grok.

---

**Made with ❤️ for advanced roleplay systems.**  
Version 1.2 Fixed + Real Grok LLM — May 2026

Run it. Extend it. Enjoy immersive roleplay! 🎭
