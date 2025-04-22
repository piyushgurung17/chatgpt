import streamlit as st
import pickle as pk
import numpy as np
import pandas as pd

model = pk.load(open('chatsentiment.pickle', 'rb'))
st.title('AI Sentiment predicting System')
st.image('https://as1.ftcdn.net/jpg/05/55/05/34/1000_F_555053469_DRRnDQaX5YDp0MBAFsLfikTR6HMSuSyJ.jpg')

#taking input from user\
st.markdown("<h2>INPUT A TWEET OR A STATUS ABOUT CHATGPT</h2>", unsafe_allow_html=True)
tweet = st.text_area("", height=150)  # Keeps the text area but removes the default label
#for prediction
if st.button('Predict'):
    input_data = [tweet]
    predicted=model.predict(input_data)
    if predicted[0] == 'bad':
        st.success("⚠️ The sentiment around ChatGPT appears to be negative, with concerns and dissatisfaction highlighted. There's room for improvement.")
    elif predicted[0] == 'neutral':
        st.success("🔄 The sentiment surrounding ChatGPT is neutral, reflecting a balanced perspective with neither strong approval nor disapproval.")
    else:  # assuming 'good' sentiment
        st.success("🌟 The sentiment toward ChatGPT is positive, with a strong indication of satisfaction and enthusiasm.")


#for saving user data
# user_data = pd.DataFrame([[age, exp, gender, edu, predicted_salary[0]]],
#                         columns=['Age', 'Experience', 'Gender', 'Education', 'Predicted Salary'])

# user_data.to_csv('recorded_inputs.csv', mode='a', header=False, index=False)