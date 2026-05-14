"""
RGFLAT Core - Parameters & Configuration

Unified configuration system combining RoleplayConfig and RoleplayParameters.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, Union, Optional


@dataclass
class RoleplayConfig:
    """Main configuration for RoleplayEngine."""
    character_name: str = "Unknown"
    scenario: str = ""
    setting: str = ""
    mood: str = "neutral"
    max_memories_in_prompt: int = 6
    auto_save: bool = False
    save_path: str = "roleplay_session.json"
    debug: bool = False
    use_real_llm: bool = False
    grok_model: str = "grok-2-1212"

    # Extended parameters (from RoleplayParameters)
    personality_traits: str = "mysterious, teasing, dominant"
    speech_style: str = "casual with sarcastic undertones"
    background: str = ""
    relationship_dynamic: str = ""
    emotional_intensity: Union[int, str] = 75
    sexual_tension: Union[int, str] = 60
    power_dynamic: str = "dominant leans slightly submissive"
    pacing: str = "slow burn with sudden spikes"
    dialogue_style: str = "teasing, confident, occasionally vulgar"
    response_length: str = "medium (2-4 paragraphs)"
    keep_in_character: bool = True
    avoid_ooc: bool = True
    enable_memory: bool = True
    enable_consistency: bool = True
    consistency_target: int = 90
    is_multi_character: bool = False
    active_character_name: str = ""

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in self.__dict__.items()}

    def get_prompt_context(self) -> str:
        return f"""
Character: {self.character_name}
Personality: {self.personality_traits}
Speech: {self.speech_style}
Setting: {self.setting}
Mood: {self.mood}
Relationship: {self.relationship_dynamic}
Emotional Intensity: {self.emotional_intensity}
Sexual Tension: {self.sexual_tension}
Power Dynamic: {self.power_dynamic}
Pacing: {self.pacing}
"""
