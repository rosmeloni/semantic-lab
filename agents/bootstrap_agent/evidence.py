from __future__ import annotations

from dataclasses import dataclass
from email import policy
from email.parser import BytesParser
from pathlib import Path

from agents.bootstrap_agent.discovery import Artifact


@dataclass(frozen=True)
class Evidence:
    source_path: Path
    kind: str
    content: str
    metadata: dict[str, str]


def extract_email_evidence(path: Path | str) -> Evidence:
    """Extract deterministic evidence from an .eml file."""

    email_path = Path(path)

    with email_path.open("rb") as file:
        message = BytesParser(policy=policy.default).parse(file)

    metadata = {
        "from": message.get("From", ""),
        "to": message.get("To", ""),
        "subject": message.get("Subject", ""),
        "date": message.get("Date", ""),
    }

    body = ""

    if message.is_multipart():
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_content()
                break
    else:
        body = message.get_content()

    return Evidence(
        source_path=email_path,
        kind="email",
        content=body.strip(),
        metadata=metadata,
    )


def extract_evidence(root: Path | str, artifact: Artifact) -> Evidence:
    """Extract evidence from a discovered artifact."""

    root_path = Path(root)
    full_path = root_path / artifact.path

    if artifact.kind == "email":
        return extract_email_evidence(full_path)

    raise ValueError(f"Unsupported artifact kind: {artifact.kind}")