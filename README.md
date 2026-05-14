# 🎭 RGFLAT - RoleplayGenerator

RGFLAT is a lightweight roleplay engine organized around a small set of Python
packages: core orchestration, memory, prompt building, adapters, AI helpers,
generators, physics, presets, and UI entry points.

## Quick Start

```bash
# Install the one required dependency.
pip install -r requirements.txt

# Run a one-shot local placeholder response.
python -m ui --preset dominant_vampire --message "Hello there, stranger..."

# Start an interactive session.
python -m ui --preset tsundere_rival

# Optional editable install exposes the rgflat console command.
pip install -e .
rgflat --preset strict_teacher --message "You wanted to see me?"
```

## Optional Grok / xAI Responses

The engine can call the xAI chat-completions API when `requests` is installed
and an API key is present. Without credentials, it falls back to deterministic
placeholder responses.

```bash
pip install -e '.[llm]'
export XAI_API_KEY="your_key_here"
python -m ui --preset dominant_vampire --use-real-llm --message "Tell me about your past..."
```

## Python API

```python
from core import RoleplayEngine
from presets import load_preset

config = load_preset("dominant_vampire")
engine = RoleplayEngine(config)

result = engine.step("You're late again...")
print(result["response"])

engine.add_memory("User confessed feelings", importance=8.0, emotion="desire", intensity=0.9)
engine.save("my_session.json")
```

Compatibility wrappers remain available for older flat-layout imports:

```python
from roleplay_engine import RoleplayEngine, RoleplayConfig
from character_generator import CharacterGenerator
from consistency import CharacterConsistency
```

## Project Structure

```text
RGFLAT/
├── adapters/              # External integration adapters, including Waidrin
├── ai/                    # Behavior tree and hybrid utility AI helpers
├── core/                  # RoleplayEngine and canonical configuration dataclass
├── consistency/           # Character and narrative consistency checks
├── generators/            # Character, dialogue, scenario, and multi-character helpers
├── memory/                # MemorySystem, relationship tracker, lorebook support
├── physics/               # Emotional/tension state helpers
├── presets/               # Ready-to-use character/scenario presets
├── prompts/               # Local prompt templating and memory-aware prompt builder
├── ui/                    # CLI plus web assets under ui/web
├── roleplay_engine.py     # Backward-compatible import wrapper
├── character_generator.py # Backward-compatible import wrapper
├── pyproject.toml         # Packaging metadata and console script
└── requirements.txt       # Runtime dependency list
```

## Web UI

The browser assets live in `ui/web/`. Open `ui/web/index.html` directly, or open
the repository-root `index.html` redirect if a tool expects a root web entry.

## Notes for Contributors

- Prefer package imports (`from core import RoleplayEngine`, `from presets import load_preset`).
- Keep backward-compatible root wrappers thin; put implementation in packages.
- Use `python -m compileall .` and at least one CLI smoke test before committing.
