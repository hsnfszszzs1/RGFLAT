"""
RGFLAT Consistency Package.

Contains both the lightweight historical ``CharacterConsistency`` helper and a
higher-level ``ConsistencyChecker`` facade used by newer package code.
"""

from typing import Dict, List


class CharacterConsistency:
    """Track simple trait consistency for a single character."""

    def __init__(self, character_name: str):
        self.character_name = character_name
        self.traits: List[str] = []
        self.violations: List[str] = []
        self.score = 100

    def add_trait(self, trait: str) -> None:
        self.traits.append(trait.lower())

    def check_response(self, response: str) -> float:
        """Return an updated consistency score from 0 to 100."""
        violations_found = 0
        response_lower = response.lower()

        for trait in self.traits:
            if trait in ["shy", "timid"] and any(
                word in response_lower for word in ["confident", "bold", "loud"]
            ):
                violations_found += 1
            if trait == "dominant" and any(
                word in response_lower for word in ["submissive", "shy", "hesitant"]
            ):
                violations_found += 1
            if trait == "formal" and any(
                word in response_lower for word in ["yo", "dude", "lol"]
            ):
                violations_found += 1

        if violations_found:
            self.score = max(0, self.score - violations_found * 10)
            self.violations.append(f"{violations_found} potential contradiction(s)")
        else:
            self.score = min(100, self.score + 1)

        return self.score

    def get_report(self) -> Dict[str, object]:
        return {
            "character": self.character_name,
            "score": self.score,
            "violations": self.violations,
            "traits": self.traits,
        }


class ConsistencyChecker:
    """Facade for narrative consistency checks."""

    def __init__(self, target_score: int = 90):
        self.target_score = target_score

    def check_consistency(
        self, character_name: str, response: str, memory_context: dict
    ) -> dict:
        checker = CharacterConsistency(character_name)
        for trait in memory_context.get("traits", []):
            checker.add_trait(trait)
        score = checker.check_response(response)
        return {
            "score": score,
            "target_score": self.target_score,
            "issues": checker.violations,
            "suggestions": [] if score >= self.target_score else ["Review response for trait drift."],
        }
