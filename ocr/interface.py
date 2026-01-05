from ocr.preprocess import preprocess_image
from ocr.model import HandwritingOCRModel

ocr_model = HandwritingOCRModel("models/ocr.pt")

def run_ocr(image_path: str) -> str:
    image = preprocess_image(image_path)
    text = ocr_model.predict(image)
    return text
