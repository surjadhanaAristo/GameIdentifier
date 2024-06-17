from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
import cv2 as cv
import numpy as np
import tensorflow as tf

app = Flask(__name__)
CORS(app)  # Enable CORS

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'GameIdentifier', 'Website', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define the path to the model and classes
MODEL_PATH = os.path.join(os.getcwd(), 'GameIdentifier', 'models', 'hsrandbloonsidentifier.keras')
CLASSES_PATH = os.path.join(os.getcwd(), 'GameIdentifier', 'models', 'mlb_classes.npy')

# Check if model and classes file exist
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
if not os.path.exists(CLASSES_PATH):
    raise FileNotFoundError(f"Classes file not found: {CLASSES_PATH}")

# Load the trained model
model = tf.keras.models.load_model(MODEL_PATH)
mlb_classes = np.load(CLASSES_PATH, allow_pickle=True)  # Load with allow_pickle=True

input_shape = (96, 96, 3)

@app.route('/upload', methods=['POST'])
def upload_file():
    print("Received file upload request")
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Process the image and make prediction
        image = cv.imread(filepath)
        image = cv.resize(image, (input_shape[1], input_shape[0]))
        image = (image / 255.0).reshape(-1, input_shape[1], input_shape[0], input_shape[2])
        yhat = model.predict(image)
        preds = zip(list(mlb_classes), list(yhat[0]))
        preds = sorted(list(preds), key=lambda z: z[1], reverse=True)[:2]
        
        result = {pred[0]: round(pred[1] * 100, 2) for pred in preds}
        
        print("Prediction result: ", result)
        return jsonify(result)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
