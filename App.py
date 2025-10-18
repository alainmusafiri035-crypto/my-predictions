import streamlit as st
import pickle
import numpy as np
with open('musa.pkl','rb') as fille:
    model=pickle.load(file)

st.title("taxi trip pricing prediction dashboard")
st.write("Enter The following input to get prediction")
duration=st.number_input("time to destination")
kilometers=st.number_input("trip kilometers")
passengers=st.number_input("number of passengers")

if st.button("Submit"):
    input_data=np.array([[duration,kilometers,passengers]])
    result=model.predict(input_data)
    #st.success("Predicted taxi trip pricing= ", result)
    st.success(f"Predicted taxi trip pricing: {result[0]:,.2f}$")    

