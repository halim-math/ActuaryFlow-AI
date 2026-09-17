from __future__ import annotations

import argparse
import json

from .schemas import AgentRequest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="ActuaryFlow-AI decision support CLI")
    parser.add_argument("message", help="insurance or actuarial request")
    parser.add_argument("--jurisdiction")
    parser.add_argument("--product-line")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    request = AgentRequest(
        message=args.message,
        jurisdiction=args.jurisdiction,
        product_line=args.product_line,
    )
    print(json.dumps(request.model_dump(), indent=2))
    print("Wire this request to the API or service composition in your deployment.")


if __name__ == "__main__":
    main()
