class SectionClassifier:
    def __init__(self, model_path: str):
        self.model = self.load(model_path)

    def load(self, path):
        pass

    def classify(self, text: str) -> dict:
        """
        Returns segmented sections
        """
        return {
            "bio_data": extract_bio(text),
            "presenting_complaints": extract_complaints(text)
        }
