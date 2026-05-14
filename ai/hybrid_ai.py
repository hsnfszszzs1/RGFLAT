"""
RGFLAT AI Package - Hybrid AI (Utility AI + Behavior Trees)

Combines Utility AI selection with Behavior Tree execution.
"""

from typing import List, Dict, Optional, Callable

# Updated import for package structure
try:
    from .behavior_tree import BTNode, NodeStatus, Blackboard, BehaviorTree
except ImportError:
    from ai.behavior_tree import BTNode, NodeStatus, Blackboard, BehaviorTree


class UtilityAction:
    def __init__(self, name: str, 
                 considerations: List[Callable[[Dict], float]],
                 behavior_tree: Optional[BehaviorTree] = None):
        self.name = name
        self.considerations = considerations
        self.behavior_tree = behavior_tree

    def calculate_utility(self, context: Dict) -> float:
        if not self.considerations:
            return 0.3
        scores = [max(0.0, min(1.0, c(context))) for c in self.considerations]
        return sum(scores) / len(scores)


class UtilitySelector:
    def __init__(self, actions: List[UtilityAction]):
        self.actions = actions

    def select_best_action(self, context: Dict) -> Optional[UtilityAction]:
        if not self.actions:
            return None
        scored = [(action, action.calculate_utility(context)) for action in self.actions]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[0][0]


# ====================== ROLEPLAY CONSIDERATIONS ======================

def create_emotion_consideration(physics, target_emotion: str, weight: float = 1.0):
    def consider(context):
        if physics.emotional_state.dominant_emotion == target_emotion:
            return weight
        return 0.0
    return consider


def create_memory_consideration(memory_system, keyword: str, weight: float = 1.0):
    def consider(context):
        memories = memory_system.get_relevant_memories(query=keyword, limit=4)
        if not memories:
            return 0.0
        avg_importance = sum(m.get("importance", 0) for m in memories) / len(memories)
        return min(1.0, (avg_importance / 10.0) * weight)
    return consider


def create_tension_consideration(physics, threshold: float = 6.0, weight: float = 1.0):
    def consider(context):
        return weight if physics.emotional_state.tension >= threshold else 0.0
    return consider


# ====================== HYBRID RUNNER ======================

def run_hybrid_decision(utility_selector: UtilitySelector, 
                        context: Dict,
                        physics=None,
                        memory_system=None,
                        debug: bool = False) -> Optional[str]:
    best_action = utility_selector.select_best_action(context)
    if not best_action:
        return None

    if debug:
        print(f"[Hybrid AI] Selected: {best_action.name}")

    if best_action.behavior_tree:
        status = best_action.behavior_tree.tick(context)
        if debug:
            print(f"[Hybrid AI] BT Result: {status}")

    return best_action.name
