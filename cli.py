#!/usr/bin/env python3
"""
RoleplayGenerator v1.2 - CLI
Uses RoleplayEngine v3 + MemorySystem v1.2 + Behavior Trees support
"""

import argparse
from roleplay_engine import RoleplayEngine, RoleplayConfig
from presets import load_preset


def main():
    parser = argparse.ArgumentParser(description="RoleplayGenerator v1.2")
    parser.add_argument("--preset", type=str, default=None, help="Load preset")
    parser.add_argument("--character", type=str, default="Karina Moss")
    parser.add_argument("--use-waidrin", action="store_true", help="Use Waidrin")
    parser.add_argument("--use-real-llm", action="store_true", help="Use real Grok LLM (requires XAI_API_KEY)")
    parser.add_argument("--message", type=str, default=None)
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    print("🎭 RoleplayGenerator v1.2")

    if args.preset:
        params = load_preset(args.preset)
        character_name = params.character_name
        print(f"Loaded preset: {args.preset}")
    else:
        character_name = args.character

    config = RoleplayConfig(
        character_name=character_name,
        debug=args.debug,
        use_real_llm=args.use_real_llm
    )

    engine = RoleplayEngine(config)
    print(f"Session started: {engine.session_id}")

    if args.message:
        result = engine.step(args.message, use_waidrin=args.use_waidrin, use_real_llm=args.use_real_llm)
        print(result.get('response', 'No response'))
        return

    print("\nInteractive mode. Type 'exit' to quit.")
    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() in ["exit", "quit"]:
                break
            result = engine.step(user_input, use_waidrin=args.use_waidrin, use_real_llm=args.use_real_llm)
            print(result.get('response', ''))
        except KeyboardInterrupt:
            break

    print("Session ended.")


if __name__ == "__main__":
    main()
