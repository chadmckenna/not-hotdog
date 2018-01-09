import numpy as np
import tensorflow as tf
import keras
from keras.applications.vgg16 import VGG16
from keras.models import load_model
from keras.preprocessing.image import img_to_array

top_model_weights_path = 'weights-skewed.h5'
model_name = 'model-skewed.h5'

base_model = VGG16(weights='imagenet', include_top=False)

model = load_model(model_name)
model.load_weights(top_model_weights_path)
graph = tf.get_default_graph()

def shape_img(img):
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)
    x = x / 255.
    return x

def build_feature_img(model, img):
    return model.predict(shape_img(img))

def predict_class(prob):
    return 0 if prob > 0.80 else 1

def make_prediction(base_model, model, img):
    feature_img = build_feature_img(base_model, img)
    prob = 1 - model.predict_proba(feature_img)[0,0]
    return predict_class(prob), prob

def predict(img):
    with graph.as_default():
        prediction, prob = make_prediction(base_model, model, img)
        return ['hotdog', 'not hotdog'][prediction], prob
