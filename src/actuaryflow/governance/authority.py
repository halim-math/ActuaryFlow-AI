from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AuthorityProfile:
    reviewer_id: str
    roles: frozenset[str]
    max_financial_authority: float
    product_lines: frozenset[str]

    def can_review(self, *, required_role: str, amount: float, product_line: str) -> bool:
        return (
            required_role in self.roles
            and amount <= self.max_financial_authority
            and product_line in self.product_lines
        )
