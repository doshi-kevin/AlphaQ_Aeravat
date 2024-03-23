import streamlit as st

# Function to calculate weighted average
def calculate_weighted_average(inputs):
    total_weight = 0
    weighted_sum = 0
    
    for input_data, weight in inputs:
        total_weight += weight
        weighted_sum += input_data * weight
    
    if total_weight != 0:
        return (weighted_sum / total_weight)
    else:
        return 0

# Main function to run the Streamlit app
def main():
    st.title("Deepfake Detection System")
    
    # Input fields
    st.header("Input Fields")
    input_video_percentage = st.slider("Input Video Break Image Percentage", 0, 100, 50)
    synthetic_video_percentage = st.slider("Synthetic Video Check Percentage", 0, 100, 50)
    screenshot_image_percentage = st.slider("Screenshot Image Percentage", 0, 100, 50)
    audio_waves_type = st.selectbox("Audio Waves Type", [0, 1])
    speech_type = st.selectbox("Speech Type", [0, 1])
    
    # Reverse the second value (subtract from 100)
    synthetic_video_percentage = 100 - synthetic_video_percentage
    
    # Weighted factors
    st.header("Weighted Factors")
    weighted_factors = [
        (input_video_percentage, 35),
        (synthetic_video_percentage, 30),
        (screenshot_image_percentage, 20),
        (audio_waves_type, 10),
        (speech_type, 5)
    ]
    
    # Calculate total output percentage
    total_output_percentage = calculate_weighted_average(weighted_factors)
    
    # Display results
    st.header("Results")
    st.write(f"Total Output Percentage: {total_output_percentage}%")
    
    # Output deepfake if percentage > 50
    if total_output_percentage > 50:
        st.warning("Deepfake Detected!")
    else:
        st.success("No Deepfake Detected.")

if __name__ == "__main__":
    main()
