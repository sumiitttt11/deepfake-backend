import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def preprocess_image(image_file):
    img = load_img(image_file, target_size=(64, 64))
    img = img_to_array(img)
    img = img.reshape(1, 64, 64, 3).astype('float32') / 255.0
    return img
