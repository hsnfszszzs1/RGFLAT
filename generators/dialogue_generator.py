"""
RGFLAT Generators - Dialogue Generator

Cleaned up version with proper structure.
"""

class DialogueGenerator:
    """Dialogue generator for roleplay responses."""

    def __init__(self, params=None, physics=None, memory=None, consistency=None, multi_char=None):
        self.params = params
        self.physics = physics
        self.memory = memory
        self.consistency = consistency
        self.multi_char = multi_char

    def generate_response(self, user_input: str, use_waidrin: bool = False) -> str:
        if use_waidrin:
            return f"[Waidrin-enhanced response for: {user_input}]"
        character = self.params.character_name if self.params else "Character"
        return f"[{character}: {user_input}...]"

    def update_after_response(self, response: str, user_input: str):
        if self.memory:
            self.memory.add_memory(f"User: {user_input}", importance=4)
            self.memory.add_memory(f"{self.params.character_name if self.params else 'Character'}: {response[:80]}...", importance=5)

    def get_status(self) -> dict:
        return {
            "has_physics": bool(self.physics),
            "has_memory": bool(self.memory),
        }
