import cv2
import numpy as np
import os

IMAGE_DIRECTORY = 'path_to_your_images'  # replace with your directory

# Thresholds
LIGHT_THRESHOLD = 200
DARK_THRESHOLD = 50

def is_image_dark(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return np.mean(image) < DARK_THRESHOLD

def is_image_light(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return np.mean(image) > LIGHT_THRESHOLD

def classify_images():
    for filename in os.listdir(IMAGE_DIRECTORY):
        if filename.endswith('.png'):
            image_path = os.path.join(IMAGE_DIRECTORY, filename)

            if is_image_dark(image_path):
                print(f'{filename} has dark colors. Suitable for white shirt.')
            elif is_image_light(image_path):
                print(f'{filename} has light colors. Suitable for black shirt.')
            else:
                print(f'{filename} has mixed colors. Color of shirt depends on other factors.')

if __name__ == "__main__":
    classify_images()
