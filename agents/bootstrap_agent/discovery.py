from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List

IGNORED_DIRS = {".git", ".hg", ".svn", ".venv", "venv", "__pycache__", "node_modules"}


@dataclass(frozen=True)
class Artifact:
    path: Path
    kind: str


def discover_artifacts(root: Path | str) -> List[Artifact]:
    """Discover candidate artefacts from a directory tree.

    The first implementation focuses on simple filesystem discovery and
    lightweight classification based on file extension.
    """
    root_path = Path(root)
    if not root_path.exists():
        return []

    artifacts: List[Artifact] = []
    for path in sorted(root_path.rglob("*")):
        if not path.is_file():
            continue

        if any(part in IGNORED_DIRS for part in path.parts):
            continue

        relative_path = path.relative_to(root_path)
        suffix = path.suffix.lower()

        if suffix in {".md", ".txt", ".rst", ".pdf"}:
            kind = "document"
        elif suffix in {".py", ".js", ".ts", ".java", ".go", ".rs", ".cpp", ".c", ".cs"}:
            kind = "code"
        elif suffix in {".yaml", ".yml", ".json", ".xml", ".csv"}:
            kind = "data"
        else:
            kind = "other"

        artifacts.append(Artifact(path=relative_path, kind=kind))

    return artifacts
