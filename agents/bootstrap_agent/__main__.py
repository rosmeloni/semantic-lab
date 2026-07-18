"""Command-line entry point for Bootstrap Agent v1."""

from pathlib import Path


def main() -> None:
    """Load and display the first sample business document."""
    document_path = Path("datasets/sample_company/company_overview.md")

    if not document_path.exists():
        print(f"Document not found: {document_path}")
        return

    document_content = document_path.read_text(encoding="utf-8")

    print(f"Loaded document: {document_path}")
    print("-" * 60)
    print(document_content)


if __name__ == "__main__":
    main()