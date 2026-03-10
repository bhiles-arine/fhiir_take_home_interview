"""Configuration for FHIR server base URL and options."""

import os

# Public FHIR R4 servers (no auth required for read)
# HAPI: https://hapi.fhir.org/baseR4
# SMART Health IT: https://r4.smarthealthit.org
FHIR_BASE_URL = os.environ.get("FHIR_BASE_URL", "https://hapi.fhir.org/baseR4")

# Optional: request timeouts, retries, etc.
REQUEST_TIMEOUT_SECONDS = int(os.environ.get("FHIR_REQUEST_TIMEOUT", "30"))
