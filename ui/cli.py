"""
RGFLAT UI - Command Line Interface

Main entry point for interactive roleplay.
"""

import sys
try:
    from core.roleplay_engine import RoleplayEngine, RoleplayConfig
    from presets.presets import load_preset, list_presets
except ImportError:
    from roleplay_engine import RoleplayEngine, RoleplayConfig
    from presets import load_preset, list_presets


def main():
    print("=== RGFLAT RoleplayGenerator ===")
    print("Available presets:", list_presets())
    
    preset = input("Choose preset (default: dominant_vampire): ") or "dominant_vampire"
    
    config = load_preset(preset)
    engine = RoleplayEngine(config)
    
    print(f"\nStarting roleplay as {config.character_name}...")
    print("Type 'quit' to exit.\n")
    
    while True:
        user_input = input(">> ")
        if user_input.lower() in ["quit", "exit"]:
            break
        result = engine.step(user_input)
        print(result.get("response", "..."))

if __name__ == "__main__":
    main()
