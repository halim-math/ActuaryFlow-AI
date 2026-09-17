from __future__ import annotations

from typing import Any


def render_markdown_report(*, title: str, metrics: dict[str, Any], notes: list[str] | None = None) -> str:
    lines = [f"# {title}", "", "## Metrics", ""]
    for key in sorted(metrics):
        lines.append(f"- **{key}**: {metrics[key]}")
    if notes:
        lines.extend(["", "## Notes", ""])
        lines.extend(f"- {note}" for note in notes)
    lines.extend([
        "",
        "Results are evaluation evidence for research and governance; they are not a substitute for domain validation.",
    ])
    return "\n".join(lines) + "\n"
