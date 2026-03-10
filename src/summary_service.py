"""
Service that fetches FHIR resources and builds the Patient Clinical Summary.

Suggested structure:
- get_patient_summary(patient_id: str) -> PatientSummary
- Or split into: fetch_patient(), fetch_conditions(), ... and build_summary()
"""

# TODO: Implement:
# 1. FHIR client (requests or fhirclient) to GET Patient and search related resources
# 2. Parsing/normalization of FHIR resources (e.g. extract code display, handle missing fields)
# 3. Assembly of the summary from demographics + conditions + medications + vitals + encounters
# 4. Error handling for missing patient, server errors, invalid responses


def get_patient_summary(patient_id: str):  # -> PatientSummary
    """Fetch patient and related resources from FHIR server; return structured summary."""
    raise NotImplementedError("Implement get_patient_summary using the FHIR API")
