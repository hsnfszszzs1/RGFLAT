"""
RGFLAT Generators - Scenario Generator

Creates rich scenarios with mood, setting, and relationship dynamics.
"""

import random

try:
    from core.parameters import RoleplayParameters
except ImportError:
    pass


class ScenarioGenerator:
    def __init__(self):
        self.moods = ["intense and seductive", "playful and teasing", "dark and mysterious", "romantic and slow", "tense and charged"]
        self.settings = ["rainy penthouse at midnight", "abandoned library", "luxury hotel suite", "quiet caf\u00e9 at closing time", "private jet at 30,000 feet"]
        self.dynamics = ["enemies to lovers", "power imbalance", "friends with benefits", "forbidden attraction", "rivalry turning into obsession"]

    def generate_scenario(self, intensity: int = 70) -> dict:
        return {
            "setting": random.choice(self.settings),
            "mood": random.choice(self.moods),
            "relationship_dynamic": random.choice(self.dynamics),
            "intensity": intensity
        }

    def apply_to_params(self, params, scenario: dict = None):
        if scenario is None:
            scenario = self.generate_scenario()
        if params:
            params.setting = scenario["setting"]
            params.mood = scenario["mood"]
            params.relationship_dynamic = scenario["relationship_dynamic"]
        return params
