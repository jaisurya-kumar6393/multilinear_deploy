import pickle
import streamlit as st
model1=pickle.load(open("Multi.pkl","rb"))
def mydeploy():
    st.title("Areaprice prediction")
    area=st.number_input("enter area")
    bedrooms=st.number_input("bedrooms")
    age=st.number_input("enter age")
    pred=st.button("predict")
    if pred:
        x=model1.predict([[area,bedrooms,age]])
        st.write(x[0])
mydeploy()
    
    
