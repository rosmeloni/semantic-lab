import tempfile
import unittest
from pathlib import Path

from agents.bootstrap_agent.discovery import discover_artifacts


class DiscoverArtifactsTests(unittest.TestCase):
    def test_discovers_files_and_classifies_them(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            docs_dir = root / "docs"
            docs_dir.mkdir()
            (docs_dir / "overview.md").write_text("hello world", encoding="utf-8")

            src_dir = root / "src"
            src_dir.mkdir()
            (src_dir / "app.py").write_text("print('hello')", encoding="utf-8")

            (root / "notes.txt").write_text("keep note", encoding="utf-8")

            noisy_dir = root / ".venv"
            noisy_dir.mkdir()
            (noisy_dir / "ignored.py").write_text("print('ignored')", encoding="utf-8")

            artifacts = discover_artifacts(root)

            self.assertEqual(len(artifacts), 3)
            self.assertTrue(any(a.path == Path("docs/overview.md") and a.kind == "document" for a in artifacts))
            self.assertTrue(any(a.path == Path("src/app.py") and a.kind == "code" for a in artifacts))
            self.assertTrue(any(a.path == Path("notes.txt") and a.kind == "document" for a in artifacts))


if __name__ == "__main__":
    unittest.main()
