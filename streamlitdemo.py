import streamlit as st
import pandas as pd
#Example 1
# st.title("Hello Ashwin")
# st.header("Python")
# st.subheader("Streamlit")
# st.markdown("I love python")
# st.code(""" for i in range(1,5,1):
#                print("hello")""")
#Example 2
# dataset = pd.read_csv(r"D:\pythondemo\DESIGN CREATION polki sample.csv")
# st.dataframe(dataset)
name = st.text_input("Enter your name :")
fname = st.text_input("Enter your father name :")
adr = st.text_area("Enter your address :")
classdata = st.selectbox("Enter your class :", (1,2,3,4))
btn = st.button("Done")
if btn :
    st.markdown(f"""
    Name : {name} \n
    father Name : {fname} \n
    Address : {adr}
    Class : {classdata}""")
