import cv2
import numpy as np

def translate_image(image_path, x_translation, y_translation):
    image = cv2.imread(image_path)

    rows, cols = image.shape[:2]
    translation_matrix = np.float32([[1, 0, x_translation], [0, 1, y_translation]])

    translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))

    cv2.imshow('Original Image', image)
    cv2.imshow('Translated Image', translated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = r"C:\Users\cakeo\Desktop\Computer Vision\GT_650.jpg"
x_translation = 100  
y_translation = 50   
translate_image(image_path, x_translation, y_translation)
