import streamlit as st
import pickle
from simplet5 import SimpleT5

model = SimpleT5()

model.load_model("t5","/Users/srinivas/Desktop/model_files ", use_gpu=True)
st.subheader("TEXT SUMMARISATION")
input = st.text_area("Enter text here")


st.text(model.predict(input))

