"""Command-line entry point for Bootstrap Agent v1."""

import argparse
from pathlib import Path

from agents.bootstrap_agent.discovery import discover_artifacts


def main() -> None:
    """Discover candidate artefacts in a directory tree."""
    parser = argparse.ArgumentParser(description="Discover organisational artefacts")
    parser.add_argument("root", nargs="?", default=".", help="Directory to scan")
    args = parser.parse_args()

    root_path = Path(args.root)
    artifacts = discover_artifacts(root_path)

    if not artifacts:
        print(f"No artefacts found in {root_path}")
        return

    print(f"Discovered {len(artifacts)} artefact(s) in {root_path}")
    for artifact in artifacts:
        print(f"- {artifact.kind}: {artifact.path}")


if __name__ == "__main__":
    main()