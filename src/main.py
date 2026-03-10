"""
Entry point for the Patient Clinical Summary.

Run from repo root:
  python -m src.main <patient_id>

Example:
  python -m src.main 12345
"""

import json
import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python -m src.main <patient_id>", file=sys.stderr)
        sys.exit(1)

    patient_id = sys.argv[1].strip()

    # TODO: Replace with your implementation:
    # 1. Fetch Patient and related resources from FHIR server
    # 2. Build clinical summary (demographics, conditions, medications, vitals, encounters)
    # 3. Return structured summary as JSON
    summary = {
        "patient_id": patient_id,
        "demographics": {},
        "conditions": [],
        "medications": [],
        "vitals": [],
        "encounters": [],
        "note": "Replace this stub with your implementation.",
    }

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
