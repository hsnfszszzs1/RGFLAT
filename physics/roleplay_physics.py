"""
RGFLAT Physics Package - Roleplay Physics

Analog to Skin/Hair Physics from body remodeling systems.
Controls emotional, tension, and narrative dynamics.
"""

from typing import Dict


class RoleplayPhysics:
    def __init__(self):
        self.emotional_state = {
            "intensity": 70,
            "arousal": 40,
            "trust": 30,
            "tension": 65
        }

    def apply_tension_spike(self, amount: int = 20):
        self.emotional_state["tension"] = min(100, self.emotional_state["tension"] + amount)
        self.emotional_state["arousal"] = min(100, self.emotional_state["arousal"] + amount // 2)

    def apply_emotional_shift(self, intensity_change: int, trust_change: int = 0):
        self.emotional_state["intensity"] = max(0, min(100, self.emotional_state["intensity"] + intensity_change))
        if trust_change:
            self.emotional_state["trust"] = max(0, min(100, self.emotional_state["trust"] + trust_change))

    def get_current_state_prompt(self) -> str:
        state = self.emotional_state
        return f"""
[Current Emotional State]
- Emotional Intensity: {state['intensity']}/100
- Sexual Tension: {state['tension']}/100
- Arousal Level: {state['arousal']}/100
- Trust Level: {state['trust']}/100
"""

    def to_dict(self) -> Dict:
        return self.emotional_state
