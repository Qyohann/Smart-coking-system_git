import tensorflow as tf
from tensorflow import keras 
import numpy as np

model = keras.models.load_model('./model_weight/predict_model.h5')
print(model)


