import json
from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
import cv2 as cv2
import matplotlib.pyplot as plt
from flask_socketio import SocketIO, emit
from tensorflow.keras.losses import CategoricalCrossentropy

app = Flask(__name__)
socketio = SocketIO(app)

classes = ['actinic keratosis', 'basal cell carcinoma', 'dermatofibroma', 'melanoma', 'nevus', 'pigmented benign keratosis', 'seborrheic keratosis', 'squamous cell carcinoma', 'vascular lesion']

# Custom function to handle the loading issue
def load_custom_model(path):
    model = load_model(path, compile=False)  # Load without compiling
    model.compile(
        optimizer='adam',  # Recompile with valid parameters
        loss=CategoricalCrossentropy(reduction='sum_over_batch_size'),  # Fix reduction issue
        metrics=['accuracy']
    )
    return model

model = load_custom_model('model.h5')  # Load the fixed model

def return_prediction(model, img):
    print('Input image shape is ', img.shape)
    img_size = (180, 180)
    img = cv2.resize(img, img_size)
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    index = np.argmax(pred)
    klass = classes[index]
    print(f'The image is predicted as being {klass}')
    res = [klass]
    return res

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/pred', methods=['POST'])
def pred():
    img = plt.imread(request.files['myImage'])
    result = return_prediction(model, img)
    return json.dumps({'cat': result[0]})

if __name__ == '__main__':
    app.run(port=7600)
