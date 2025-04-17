<<<<<<< HEAD
import streamlit as st
st.title ("credit card fraud detection")
st.write ("Enter following details")
amount=st.number_input("Transaction Amount")
card= st.selectbox("Card Type",["Visa","Master card","other"]) 
if st.button("Submit"):
   st.write("TRANSACTION SUBMITTED")
=======

>>>>>>> b5c7dfd9a368c82ad706e2ad508b210f248d1178
