def extract_entities(text: str) -> dict:
    """
    Extract age, sex, complaints, duration
    """
    return {
        "age": find_age(text),
        "sex": find_sex(text),
        "complaints": find_complaints(text)
    }
