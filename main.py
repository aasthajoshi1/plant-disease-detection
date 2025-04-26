import streamlit as st  # type: ignore
import numpy as np
import tensorflow as tf  # type: ignore
from PIL import Image
import gdown
import os

# Function to download the model if not present
def download_model():
    model_url = 'https://drive.google.com/uc?id=1QgT_lSlOSRQ_4SGl1bsW4wrukXAN0jBz'
    output_path = 'trained_model_final.keras'

    if not os.path.exists(output_path):
        gdown.download(model_url, output_path, quiet=False)
    else:
        print("Model already downloaded.")

# TensorFlow Model Prediction
def model_prediction(test_image):
    download_model()  # Ensure model is available
    model = tf.keras.models.load_model("trained_model_final.keras", compile=False)
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index, prediction

# Solutions Dictionary (disease -> solution)
solutions = {
    'Apple___Apple_scab': "Apply fungicides like Captan or Mancozeb and remove infected leaves.",
    'Apple___Black_rot': "Use copper-based fungicides and ensure proper spacing for air circulation.",
    'Apple___Cedar_apple_rust': "Apply fungicides such as myclobutanil, and remove infected leaves.",
    'Apple___healthy': "Maintain proper care and monitoring, no disease detected.",
    'Blueberry___healthy': "Ensure proper irrigation, prune any dead or damaged branches.",
    'Cherry_(including_sour)___Powdery_mildew': "Apply sulfur-based fungicides and prune affected branches.",
    'Cherry_(including_sour)___healthy': "Regularly inspect for pests and diseases, and prune dead branches.",
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': "Apply fungicides like Chlorothalonil and avoid excessive irrigation.",
    'Corn_(maize)__Common_rust': "Apply rust-resistant corn varieties and use fungicides like Azoxystrobin.",
    'Corn_(maize)___Northern_Leaf_Blight': "Use resistant varieties and apply fungicides like Chlorothalonil.",
    'Corn_(maize)___healthy': "Ensure proper irrigation and pest control practices.",
    'Grape___Black_rot': "Apply fungicides like Mancozeb and prune affected parts.",
    'Grape__Esca(Black_Measles)': "Remove and destroy infected vines, and apply fungicides.",
    'Grape__Leaf_blight(Isariopsis_Leaf_Spot)': "Apply fungicides like Chlorothalonil and avoid overhead irrigation.",
    'Grape___healthy': "Maintain proper care and monitor for pests regularly.",
    'Orange__Haunglongbing(Citrus_greening)': "Remove infected trees, and use resistant rootstocks.",
    'Peach___Bacterial_spot': "Use copper-based bactericides and remove infected leaves.",
    'Peach___healthy': "Keep trees well-watered, prune dead branches, and inspect regularly.",
    'Pepper,bell__Bacterial_spot': "Apply copper-based bactericides and remove infected plants.",
    'Pepper,bell__healthy': "Ensure proper irrigation and fertilization, and monitor for pests.",
    'Potato___Early_blight': "Apply fungicides like Chlorothalonil and remove infected plants.",
    'Potato___Late_blight': "Apply fungicides like Metalaxyl and remove infected leaves.",
    'Potato___healthy': "Maintain good soil drainage, and ensure proper watering practices.",
    'Raspberry___healthy': "Prune damaged branches and apply fungicides as needed.",
    'Soybean___healthy': "Monitor for pests, provide adequate nutrients, and ensure proper irrigation.",
    'Tomato___Spider_mites Two-spotted_spider_mite': "Use miticides like Avid, and ensure proper irrigation.",
    'Tomato___Target_Spot': "Use fungicides like Azoxystrobin and remove infected leaves.",
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': "Remove infected plants and control whiteflies.",
    'Tomato___Tomato_mosaic_virus': "Use resistant varieties, and remove infected plants.",
    'Tomato___healthy': "Maintain proper care, water properly, and prune regularly."
}

# Sidebar
st.sidebar.title("Plant Disease Recognition Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition","FAQs"])


# Main Page
if app_mode == "Home":
        # CSS animation code to animate the image and text
        st.markdown("""
        <style>
        .title {
            animation: fadeIn 3s ease-out;
        }
        .image-container {
            animation: slideIn 3s ease-out;
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        @keyframes slideIn {
            0% { transform: translateX(100%); }
            100% { transform: translateX(0); }
        }
        </style>
        """, unsafe_allow_html=True)

        # Display title with animation
        st.markdown('<h1 class="title">🌱 Plant Disease Recognition System 🌱</h1>', unsafe_allow_html=True)

        # Image with animation
        image_path = "home_page.png"  # Ensure the image path is correct
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(image_path, use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Write the rest of the page content
        st.markdown("""
        Welcome to the *Plant Disease Recognition System*! Our mission is to assist in identifying plant diseases effectively and efficiently.
        
        ### How It Works:
        1. *Upload an Image: Go to the **Disease Recognition* page and upload an image of a plant with a suspected disease.
        2. *Prediction*: Our system will analyze the image and predict the disease based on advanced machine learning models.
        3. *Solution*: The system will provide a suggested treatment based on the identified disease.
        
        ### Why Choose Us?
        - *Accurate*: State-of-the-art machine learning techniques for accurate disease detection.
        - *Fast*: Results are provided within seconds to help you take prompt action.
        - *User-Friendly*: A simple and intuitive interface for easy use.
        """)

elif app_mode == "About":
        st.header("About the Project")
        st.markdown("""
        #### Dataset
        This dataset consists of over *87,000 images* of healthy and diseased crop leaves, categorized into *38 different classes. It has been used to train our deep learning model for disease prediction. The dataset includes **train, **test, and **validation* sets for proper model training and evaluation.
        
        #### Key Features
        - The model detects diseases like *Apple Scab, **Tomato Mosaic Virus, **Potato Late Blight*, and more.
        - Well-structured, balanced dataset for effective disease prediction.

        #### GitHub Repository
        For more details on the dataset and model, visit our [GitHub repository](https://github.com).
        """)

elif app_mode == "Disease Recognition":
        st.header("Upload Image for Disease Recognition")
        st.write("Upload an image of a plant leaf to detect potential diseases.")

        # Image upload
        test_image = st.file_uploader("Choose an Image:", type=["jpg", "jpeg", "png"])

        if test_image:
            image = Image.open(test_image)
            st.image(image, caption="Uploaded Image")

        # Predict button
        if st.button("Predict Disease"):
            with st.spinner("Analyzing the image..."):
                result_index, prediction = model_prediction(test_image)

                # Class Names
                class_name = ['Apple__Apple_scab', 'Apple_Black_rot', 'Apple_Cedar_apple_rust', 'Apple__healthy',
                            'Blueberry__healthy', 'Cherry(including_sour)__Powdery_mildew', 'Cherry(including_sour)___healthy',
                            'Corn_(maize)__Cercospora_leaf_spot Gray_leaf_spot', 'Corn(maize)__Common_rust',
                            'Corn_(maize)__Northern_Leaf_Blight', 'Corn(maize)__healthy', 'Grape__Black_rot',
                            'Grape__Esca(Black_Measles)', 'Grape__Leaf_blight(Isariopsis_Leaf_Spot)', 'Grape___healthy',
                            'Orange__Haunglongbing(Citrus_greening)', 'Peach__Bacterial_spot', 'Peach__healthy',
                            'Pepper,bell_Bacterial_spot', 'Pepper,_bell_healthy', 'Potato_Early_blight', 'Potato__Late_blight',
                            'Potato__healthy', 'Raspberry_healthy', 'Soybean_healthy', 'Tomato__Spider_mites Two-spotted_spider_mite',
                            'Tomato__Target_Spot', 'Tomato_Tomato_Yellow_Leaf_Curl_Virus', 'Tomato__Tomato_mosaic_virus',
                            'Tomato___healthy']
                
                disease = class_name[result_index]
                st.success(f"Model predicts: *{disease}*")

                # Show relevant solution
                solution = solutions.get(disease, "No solution available for this disease.")
                st.write(f"*Solution:* {solution}")

                # Optionally, show additional details (confidence, etc.)
                confidence = np.max(prediction) * 100  # Convert to percentage
                st.write(f"*Confidence:* {confidence:.2f}%")

#FAQs
elif app_mode == "FAQs":
    st.header("Frequently Asked Questions (FAQs)")
    
    st.subheader("General Information")
    st.markdown("""
        *Q1:* What is the Plant Disease Recognition System?  
        *A1:* It is an AI-based system that uses machine learning to recognize plant diseases from images of plant leaves. Simply upload an image, and the system will provide predictions along with relevant solutions.

        *Q2:* How does the system work?  
        *A2:* The system uses a trained deep learning model that processes the image you upload and compares it with the dataset it was trained on to identify the disease. It then outputs the disease name and a suggested treatment or action.

        *Q3:* What types of diseases can the system detect?  
        *A3:* The system can detect over 20 types of diseases affecting crops like tomatoes, apples, peppers, and more. The model is trained on a large dataset of plant diseases from various agricultural sectors.

    """)

    st.subheader("Image Upload and Prediction")
    st.markdown("""
        *Q4:* What types of images can I upload?  
        *A4:* You can upload JPG, JPEG, or PNG files. We recommend that the images be clear and focused on the plant leaf, with minimal obstructions such as dirt, water droplets, or other distractions.

        *Q5:* How do I upload an image?  
        *A5:* On the *Disease Recognition* page, you’ll find an option to upload an image of your plant leaf. After uploading, click on the *Predict Disease* button to get the results.

        *Q6:* Why is my uploaded image not being processed?  
        *A6:* Ensure that the image format is supported (JPG, JPEG, PNG) and that the image is not too large. If the issue persists, try uploading a higher-quality image with clear visibility of the leaf.

    """)

    st.subheader("Results and Predictions")
    st.markdown("""
        *Q7:* How accurate is the prediction?  
        *A7:* The model has an accuracy of up to 95%, depending on the image quality and the disease being detected. We continually update and improve the model to enhance its performance.

        *Q8:* Can the system predict multiple diseases in one image?  
        *A8:* Currently, the system is designed to predict a single disease from the uploaded image. However, future updates may include support for detecting multiple diseases simultaneously.

        *Q9:* What should I do if the prediction is incorrect?  
        *A9:* While the system is highly accurate, no AI model is perfect. If the prediction is incorrect, ensure that the image is clear and focused. If the issue persists, you can manually check other potential diseases using the *Disease Info* section.

    """)

    st.subheader("Solution and Treatment Recommendations")
    st.markdown("""
        *Q10:* Does the system provide treatment for detected diseases?  
        *A10:* Yes, for each predicted disease, the system provides recommended treatment or action based on common practices and research. These recommendations are based on available literature and may vary depending on the severity of the disease.

        *Q11:* How do I interpret the recommended solutions?  
        *A11:* The recommended solutions typically include methods such as using pesticides, fungicides, or changing environmental conditions to prevent the spread of the disease. Always consult an agricultural expert or specialist for confirmation before taking any actions.

    """)

    st.subheader("Model and Dataset Information")
    st.markdown("""
        *Q12:* What is the dataset used to train the model?  
        *A12:* The model was trained using a dataset of over 87,000 images of plant leaves, categorized into 38 disease classes. This dataset was created by collecting various images from reliable agricultural sources and is used to teach the model to recognize different diseases.

        *Q13:* How was the model trained?  
        *A13:* The model was trained using deep learning techniques, particularly convolutional neural networks (CNNs), which are effective for image recognition tasks. The dataset was split into training, validation, and test sets to ensure robust performance.

        *Q14:* Can I use this model on my own dataset?  
        *A14:* Yes, the model can be fine-tuned and retrained on your dataset if you have your own images. You would need to gather and label your images, then retrain the model using techniques such as transfer learning to adapt it to your dataset.

    """)

    st.subheader("Technical Support")
    st.markdown("""
        *Q15:* I encountered an error or bug, what should I do?  
        *A15:* If you encounter any technical issues, please make sure you are using a supported browser and that your internet connection is stable. If the problem persists, feel free to contact us via the *Contact Us* section, and we will assist you.

        *Q16:* How can I provide feedback or suggestions for improvement?  
        *A16:* We appreciate your feedback! Please feel free to share any suggestions or feedback through the *Contact Us* page. Your insights will help us improve the system and add new features.
    """)

    st.header("Contact Us")
    st.markdown("""
        Have questions or feedback? Reach out to us at:
        - Email: support@plantdiseaserecognition.com
        - Phone: +123 456 7890
        """)
