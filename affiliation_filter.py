import re

ACADEMIC_KEYWORDS = ["university", "institute", "hospital", "college", "school"]
COMPANY_KEYWORDS = ["pharma", "biotech", "inc", "ltd", "corporation", "gmbh"]

def classify_affiliation(affiliation: str):
    """Classifies whether an affiliation is academic or non-academic."""
    if any(word in affiliation.lower() for word in ACADEMIC_KEYWORDS):
        return "academic"
    if any(word in affiliation.lower() for word in COMPANY_KEYWORDS):
        return "company"
    return "unknown"
