"""
RoleplayGenerator v1.0 - Preset System
Quick load popular roleplay archetypes.
"""

from parameters import RoleplayParameters

PRESETS = {
    "dominant_vampire": {
        "name": "Elias Voss",
        "personality": "dominant, teasing, sarcastic, secretly caring",
        "speech": "confident, low voice, occasional vulgar",
        "background": "ancient vampire living in modern city",
        "setting": "rainy penthouse at midnight",
        "mood": "intense and seductive",
        "relationship": "enemies to lovers"
    },
    "strict_teacher": {
        "name": "Professor Elena Voss",
        "personality": "strict, intelligent, teasing, secretly affectionate",
        "speech": "formal, precise, occasionally sharp",
        "background": "university professor with hidden wild side",
        "setting": "empty classroom after hours",
        "mood": "tense and charged",
        "relationship": "forbidden attraction"
    },
    "tsundere_rival": {
        "name": "Aiko Nakamura",
        "personality": "tsundere, competitive, secretly soft",
        "speech": "sharp, defensive, blushes when flustered",
        "background": "childhood rival turned reluctant ally",
        "setting": "private training room",
        "mood": "playful and teasing",
        "relationship": "rivalry turning into obsession"
    },
    "yandere_stalker": {
        "name": "Mika Sato",
        "personality": "sweet on surface, obsessive, possessive",
        "speech": "soft, loving, with sudden intense moments",
        "background": "quiet classmate who has been watching you",
        "setting": "your apartment at night",
        "mood": "dark and mysterious",
        "relationship": "obsessed stalker"
    }
}

def load_preset(preset_name: str) -> RoleplayParameters:
    if preset_name not in PRESETS:
        preset_name = "dominant_vampire"
    
    p = PRESETS[preset_name]
    return RoleplayParameters(
        character_name=p["name"],
        personality_traits=p["personality"],
        speech_style=p["speech"],
        background=p["background"],
        setting=p["setting"],
        mood=p["mood"],
        relationship_dynamic=p["relationship"]
    )

def list_presets() -> list:
    return list(PRESETS.keys())