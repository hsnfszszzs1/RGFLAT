"""Compatibility wrapper for the package-based roleplay engine.

New code should import from ``core`` or ``core.roleplay_engine``.  This module is
kept so older flat-layout examples continue to work.
"""

from core.roleplay_engine import RoleplayEngine
from core.parameters import RoleplayConfig, RoleplayParameters

__all__ = ["RoleplayEngine", "RoleplayConfig", "RoleplayParameters"]
