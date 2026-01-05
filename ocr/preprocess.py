import cv2
import numpy as np

def preprocess_image(image_path: str) -> np.ndarray:
    """
    Prepare handwritten clerking image for OCR
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Noise reduction
    img = cv2.GaussianBlur(img, (5,5), 0)

    # Adaptive thresholding
    img = cv2.adaptiveThreshold(
        img, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )

    # Deskew
    coords = np.column_stack(np.where(img > 0))
    angle = cv2.minAreaRect(coords)[-1]
    angle = -(90 + angle) if angle < -45 else -angle

    (h, w) = img.shape
    M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1.0)
    img = cv2.warpAffine(img, M, (w, h),
                          flags=cv2.INTER_CUBIC,
                          borderMode=cv2.BORDER_REPLICATE)

    return img
