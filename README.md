# Take-Home: FHIR Patient Clinical Summary
## Overview

Build a **Patient Clinical Summary** service that calls a FHIR R4 API to load a patient and related clinical data, then produces a structured summary suitable for display in a clinical or patient-facing app.

You will query a public FHIR server, resolve references across resources, and handle missing data and coding systems (e.g. LOINC, SNOMED) in a robust way.

---

## Scenario

A healthcare app needs a single “patient summary” API that, given a patient ID, returns:

- **Demographics** – name, birth date, gender, identifiers
- **Active conditions** – problems/diagnoses (active only)
- **Current medications** – medication requests or statements that are active
- **Recent vitals** – observations (e.g. blood pressure, heart rate, temperature) from the last 30 days, with units and reference ranges where available
- **Recent encounters** – encounters from the last 90 days (type, period, reason)

All clinical data should be tied to the same patient via FHIR references. Codes (e.g. condition code, observation code) should be exposed in a consistent way (e.g. system, code, display text) so the UI can show human-readable labels.

---

## Requirements

### Functional

1. **FHIR server**  
   Use a public R4 server. Suggested:
   - **HAPI public:** `https://hapi.fhir.org/baseR4`
   - **SMART Health IT:** `https://r4.smarthealthit.org` (no auth required for read)

   Document in your README which base URL you used and how to switch it (e.g. env var or config).

2. **Patient lookup**  
   - `GET [base]/Patient/[id]` to load the patient.
   - If the patient is not found, return a clear error (HTTP-style or structured).

3. **Related data**  
   Fetch related resources for that patient using search (and optionally `_include` if the server supports it):
   - **Condition** – filter by patient reference; active only.
   - **MedicationRequest** or **MedicationStatement** – filter by patient; active only.
   - **Observation** – filter by patient and date (e.g. last 30 days); include category or code if you want to focus on vitals.
   - **Encounter** – filter by patient and date (e.g. last 90 days).

   You may use chained search (e.g. `?patient=Patient/[id]`) or separate search endpoints. Handle pagination (e.g. `_count`, `next` link) if the server returns many results.

4. **Summary model**  
   Produce a single structured summary (e.g. a Pydantic model or dataclass) containing:
   - Demographics (from Patient).
   - Lists of conditions, medications, observations (vitals), and encounters with:
     - Relevant dates/periods.
     - Code information: coding system, code, and display text where available.
     - Status or clinical status where relevant (e.g. active, completed).

5. **Code display**  
   For coded fields (e.g. condition code, observation code, encounter type), expose at least:
   - `system` (e.g. `http://snomed.info/sct`)
   - `code`
   - `display` (text for UI)

   If `display` is missing, you may leave it blank or derive a fallback (e.g. use code); document your choice.

6. **Robustness**  
   - Missing or malformed data (e.g. no name, no coding) should not crash the service.
   - Invalid patient ID or server errors should be handled and communicated clearly.

### Non-functional (what we’ll look for)

- **Structure** – Clear separation between: FHIR client, resource parsing/normalization, and summary assembly.
- **Testing** – Unit tests for summary logic and parsing; integration test against the public server is optional but valuable.
- **Documentation** – README with: how to run, how to test, design decisions (e.g. date filters, handling missing display).
- **Code quality** – Readable, type hints where helpful, no unnecessary dependencies.

---

## Deliverables

1. **Code**  
   - Python project that builds the summary from a given patient ID.
   - Entry point: CLI or minimal HTTP API (e.g. Flask/FastAPI) that accepts a patient ID and returns the summary as JSON.

2. **README**  
   - How to install (e.g. `pip install -r requirements.txt`), run, and test.
   - Which FHIR server you used and how to configure the base URL.
   - Short “Design notes” (e.g. date ranges, pagination, handling missing codes).

3. **Tests**  
   - At least a few unit tests (e.g. mapping FHIR resources to your summary model, handling missing optional fields).
   - Optional: one integration test that hits the public FHIR server.

Do **not** implement authentication (e.g. SMART on FHIR). Assume read-only, unauthenticated access to the public server.

---

## Out of scope

- Authentication / OAuth / SMART on FHIR
- Persistence or database
- Full US Core or other profile validation
- UI or frontend
- Deployment (Docker is optional; a simple “how to run locally” is enough)

---

## Evaluation

We’ll assess:

- **Correctness** – Summary matches the requested structure and uses real FHIR data.
- **FHIR usage** – Sensible use of search, references, and code handling.
- **Design** – Clear layers (client vs. parsing vs. summary), extensibility.
- **Robustness** – Graceful handling of missing data and errors.
- **Tests** – Meaningful coverage of core logic.
- **Documentation** – README and design notes are clear and honest about tradeoffs.

---

## Getting started

- Clone this repo and work in your own branch.
- Install dependencies: `pip install -r requirements.txt`
- Run the stub: `python -m src.main <patient_id>` (see `src/main.py`).
- Replace the stub with your implementation and add tests under `tests/`.

Use any public R4 patient ID from the server you choose (e.g. from HAPI or SMART Health IT). Document in the README a sample patient ID that works with your solution.

---

## Hints

- **Patient:** `GET [base]/Patient/[id]`
- **Search by patient:** e.g. `GET [base]/Condition?patient=Patient/[id]&clinical-status=active`, `GET [base]/Observation?subject=Patient/[id]&date=ge2024-01-01`, etc.
- **Pagination:** Use `_count` and follow `link` with `rel="next"` in the Bundle response if needed.
- **Codes:** In FHIR, coded values are often in `.coding` (list of `{ system, code, display }`); pick the first or a preferred one for display.

Good luck.
