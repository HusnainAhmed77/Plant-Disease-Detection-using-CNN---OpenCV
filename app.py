import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
import json

# Load model
model = tf.keras.models.load_model("rice_leaf_disease_model.h5")

# Load class labels
with open("class_indices.json", "r") as f:
    class_labels = json.load(f)

# Function to predict
def predict(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    predicted_class = class_labels[str(np.argmax(pred))]
    confidence = float(np.max(pred)) * 100
    return predicted_class, confidence

# Streamlit UI
st.title("🌾 Rice Leaf Disease Classifier")
st.write("Upload a rice leaf image to detect disease")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
if uploaded_file is not None:
    # Read file
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    st.image(image, channels="BGR", caption="Uploaded Image", use_column_width=True)

    # Prediction
    label, conf = predict(image)
    st.success(f"Prediction: **{label}** with {conf:.2f}% confidence")
