"""
RGFLAT Generators - Multi-Character System

Supports multiple characters in the same roleplay session.
"""

from typing import Dict, List, Optional

try:
    from core.parameters import RoleplayParameters
except ImportError:
    pass


class MultiCharacterManager:
    def __init__(self):
        self.characters: Dict[str, any] = {}
        self.active_character: Optional[str] = None
        self.relationship_map = {}

    def add_character(self, name: str, params):
        self.characters[name] = params
        if self.active_character is None:
            self.active_character = name

    def switch_character(self, name: str):
        if name in self.characters:
            self.active_character = name

    def get_active(self):
        if self.active_character:
            return self.characters.get(self.active_character)
        return None

    def get_all_names(self) -> List[str]:
        return list(self.characters.keys())

    def set_relationship(self, char1: str, char2: str, dynamic: str):
        key = tuple(sorted([char1, char2]))
        self.relationship_map[key] = dynamic

    def get_relationship(self, char1: str, char2: str) -> str:
        key = tuple(sorted([char1, char2]))
        return self.relationship_map.get(key, "neutral")

    def generate_group_prompt(self) -> str:
        lines = ["You are in a group roleplay with multiple characters.\n"]
        for name, params in self.characters.items():
            lines.append(f"--- {name} ---")
        return "\n".join(lines)
