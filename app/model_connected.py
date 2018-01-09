import numpy as np
import tensorflow as tf
import keras
from keras.models import load_model
from keras.preprocessing.image import img_to_array

top_model_weights_path = 'weights-connected.h5'
model_name = 'model-connected.h5'

model = load_model(model_name)
model.load_weights(top_model_weights_path)
graph = tf.get_default_graph()

def shape_img(img):
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)
    x = x / 255.
    return x

def predict_classes(proba):
    if proba.shape[-1] > 1:
        return proba.argmax(axis=-1)
    else:
        return (proba > 0.2).astype('int32')

def predict(img):
    img = shape_img(img)
    with graph.as_default():
        return ['hotdog', 'not hotdog'][predict_classes(model.predict(img))[0,0]], 1 - model.predict(img)[0,0]
