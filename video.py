import os
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.efficientnet import preprocess_input
import cv2

# Load the EfficientNet model
MODEL_PATH = 'EfficientNet_model.h5'
model = load_model(MODEL_PATH)

# Function to preprocess frames
# Function to preprocess frames
def preprocess_frame(frame):
    # Resize frame to match model input shape (e.g., 32x32 pixels)
    resized_frame = cv2.resize(frame, (32, 32))
    return resized_frame


# Function to process the uploaded video
def process_video(video_file):
    # Save uploaded video to a temporary file
    with open("temp_video.mp4", "wb") as f:
        f.write(video_file.read())

    # Open the saved video file using OpenCV
    cap = cv2.VideoCapture("temp_video.mp4")

    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Preprocess frame
        frame = preprocess_frame(frame)
        frames.append(frame)

    cap.release()

    # Delete the temporary video file
    os.remove("temp_video.mp4")

    return frames


def main():
    st.title("EfficientNet Video Classifier")

    # Upload video file
    uploaded_file = st.file_uploader("Upload video", type=['mp4', 'avi', 'mov', 'mkv'])

    if uploaded_file is not None:
        # Display uploaded video
        st.video(uploaded_file)

        # Process video and make predictions
        frames = process_video(uploaded_file)
        predictions = []
        for frame in frames:
            # Make prediction
            prediction = model.predict(np.expand_dims(frame, axis=0))
            predictions.append(prediction)

        # Calculate mean probability
        probabilities = [float(prediction[0][0]) for prediction in predictions]
        mean_probability = np.mean(probabilities)

        # Display mean probability and print "yes" or "no"
        st.write("Mean Probability:", mean_probability)
        if mean_probability > 0.70:
            st.write("No")
        else:
            st.write("Yes")




if __name__ == "__main__":
    main()
