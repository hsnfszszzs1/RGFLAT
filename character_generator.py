"""Compatibility wrapper for character generation helpers."""

from generators.character_generator import generate_character


class CharacterGenerator:
    """Small object-oriented wrapper around ``generate_character``."""

    def generate(self, preset: str = None, **kwargs):
        return generate_character(preset=preset, **kwargs)


__all__ = ["CharacterGenerator", "generate_character"]
