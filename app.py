import streamlit as st
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import numpy as np

# Load the Hugging Face model
MODEL_NAME = "linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification"

@st.cache_resource
def load_model():
    processor = AutoImageProcessor.from_pretrained(MODEL_NAME)
    model = AutoModelForImageClassification.from_pretrained(MODEL_NAME)
    return processor, model

processor, model = load_model()

# Streamlit UI
st.title("🌿 Plant Disease Detection AI")
st.write("Upload a leaf image to detect possible diseases.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Preprocess image
    inputs = processor(images=image, return_tensors="pt")
    
    # Make prediction
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class = outputs.logits.argmax(-1).item()
    
    # Get class labels
    class_labels = model.config.id2label
    detected_disease = class_labels[predicted_class]
    
    # Display results
    st.subheader("🛑 Detection Result:")
    st.write(f"**Detected Disease:** {detected_disease}")
    
    st.success("Detection complete! Try another image if needed.")
