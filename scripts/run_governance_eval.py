from __future__ import annotations

import json
from pathlib import Path

from actuaryflow.evaluation.metrics import accuracy
from actuaryflow.governance.policy import GovernancePolicy


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    expected: list[bool] = []
    actual: list[bool] = []
    policy = GovernancePolicy()
    with (ROOT / "eval" / "governance_cases.jsonl").open(encoding="utf-8") as handle:
        for line in handle:
            case = json.loads(line)
            required, _ = policy.requires_review(set(case["flags"]), amount=float(case["amount"]))
            expected.append(bool(case["expected_review"]))
            actual.append(required)
    print(json.dumps({"review_routing_accuracy": accuracy(expected, actual), "cases": len(expected)}, indent=2))


if __name__ == "__main__":
    main()
