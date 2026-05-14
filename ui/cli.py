"""
RGFLAT UI - Command Line Interface.

Supports both interactive sessions and one-shot prompt/response generation.
"""

import argparse

from core import RoleplayEngine
from presets import list_presets, load_preset


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run RGFLAT roleplay sessions.")
    parser.add_argument(
        "--preset",
        default="dominant_vampire",
        choices=list_presets(),
        help="Preset character/scenario to load.",
    )
    parser.add_argument(
        "--message",
        help="Run a single turn instead of starting interactive mode.",
    )
    parser.add_argument(
        "--use-waidrin",
        action="store_true",
        help="Use the Waidrin adapter context path for this turn.",
    )
    parser.add_argument(
        "--use-real-llm",
        action="store_true",
        help="Call the configured Grok/xAI chat API when credentials are available.",
    )
    parser.add_argument("--debug", action="store_true", help="Print debug output.")
    return parser


def create_engine(preset_name: str, use_real_llm: bool = False, debug: bool = False) -> RoleplayEngine:
    config = load_preset(preset_name)
    config.use_real_llm = use_real_llm
    config.debug = debug
    return RoleplayEngine(config)


def run_one_shot(args: argparse.Namespace) -> None:
    engine = create_engine(args.preset, args.use_real_llm, args.debug)
    result = engine.step(
        args.message,
        use_waidrin=args.use_waidrin,
        use_real_llm=args.use_real_llm,
    )
    print(result.get("response", "..."))


def run_interactive(args: argparse.Namespace) -> None:
    print("=== RGFLAT RoleplayGenerator ===")
    print("Available presets:", list_presets())

    engine = create_engine(args.preset, args.use_real_llm, args.debug)
    print(f"\nStarting roleplay as {engine.config.character_name}...")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input(">> ")
        if user_input.lower() in ["quit", "exit"]:
            break
        result = engine.step(
            user_input,
            use_waidrin=args.use_waidrin,
            use_real_llm=args.use_real_llm,
        )
        print(result.get("response", "..."))


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.message:
        run_one_shot(args)
    else:
        run_interactive(args)


if __name__ == "__main__":
    main()
