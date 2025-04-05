import tensorflow as tf
from keras.models import load_model

# Enable eager execution
tf.compat.v1.enable_eager_execution()

class DeepfakeModel:
    def __init__(self):
        self.model = load_model("app/model/efficientnet_deepfake.h5")


    def predict(self, image_array):
        prediction = self.model.predict(image_array)
        return int(prediction[0][0] > 0.5)
