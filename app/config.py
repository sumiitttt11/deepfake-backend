import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'efficientnet_deepfake.h5')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
