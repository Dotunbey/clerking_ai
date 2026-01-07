from ocr.inference import run_ocr
from nlp.normalize import normalize_text
from nlp.section_classifier import SectionClassifier
from nlp.ner import extract_entities
from drafting.generator import generate_draft

classifier = SectionClassifier("models/section.pt")

def run_full_pipeline(image_path: str) -> str:
    raw_text = run_ocr(image_path)
    clean_text = normalize_text(raw_text)
    sections = classifier.classify(clean_text)
    entities = extract_entities(sections["presenting_complaints"])
    draft = generate_draft(entities)

    return draft
