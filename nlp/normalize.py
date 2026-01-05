MEDICAL_ABBREVIATIONS = {
    "c/o": "complains of",
    "SOB": "shortness of breath",
    "yrs": "years"
}

def normalize_text(text: str) -> str:
    """
    Expand abbreviations and correct spacing
    """
    for abbr, full in MEDICAL_ABBREVIATIONS.items():
        text = text.replace(abbr, full)

    text = " ".join(text.split())
    return text
