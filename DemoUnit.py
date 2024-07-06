import streamlit as st
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from io import StringIO
import numpy as np
import tensorflow as tf
from keras.models import load_model

model1 = load_model('model/Model1.h5')
model2 = load_model('model/Model2.h5')
model3 = load_model('model/Model3.h5')

st.markdown("<h1 style='text-align: center;'>Demo Unit</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Cataract and Normal</h1>", unsafe_allow_html=True)
st.text('')
st.text('')
class_names = ['Cataract', 'Normal']

uploaded_files = st.file_uploader("Choose a file", type=['png', 'jpg', 'jpeg'])
if uploaded_files is not None:
    bytes_data = uploaded_files.getvalue()
    st.image(bytes_data)
    image = load_img(uploaded_files,target_size=(150,150))
    x = img_to_array(image)
    x = x/255.0
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])

    pred1 = model1.predict(images)
    pred2 = model2.predict(images)
    pred3 = model3.predict(images)

#Pred 1
    if np.max(pred1) > 0.6:
        conf1 = np.max(pred1)
        pred1 = "Normal"
    else:
        conf1 = np.max(pred1)
        pred1 = "Cataract"

# Pred 2
    if np.max(pred2) > 0.6:
        conf2 = np.max(pred2)
        pred2 = "Normal"
    else:
        conf2 = np.max(pred2)
        pred2 = "Cataract"

# Pred 3        
    if np.max(pred3) > 0.6:
        conf3 = np.max(pred3)
        pred3 = "Normal"
    else:
        conf3 = np.max(pred3)
        pred3 = "Cataract"
        
    st.markdown("<h1 style='text-align: Left;'>Model 1</h1>", unsafe_allow_html=True)
    st.header(f"Predictions: {pred1}")
    st.header(f"Confidence: {conf1} %")
    st.markdown("<h1 style='text-align: Left;'>Model 2</h1>", unsafe_allow_html=True)
    st.header(f"Predictions: {pred2}")
    st.header(f"Confidence: {conf2} %")
    st.markdown("<h1 style='text-align: Left;'>Model 3</h1>", unsafe_allow_html=True)
    st.header(f"Predictions: {pred3}")
    st.header(f"Confidence: {conf3} %")

    # Run Apps
    # streamlit run DemoUnit.py --server.enableXsrfProtection false