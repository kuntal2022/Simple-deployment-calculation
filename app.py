
import streamlit as st
st.header("Calculation")
a = st.number_input("Enter the first number")
b = st.number_input("Enter the second number")
cal=st.text_input("What You wish To Perform Add, Sub, Div, Mul")
cal=cal.lower()


if cal=="add":

    result = a+b
elif cal =="sub":
    result =a-b
elif cal == "div":
    if b==0:
        result ="Inf"
    else:
        result=a/b
elif cal =="mul":
    result = a*b
else:
    result ="Choose the correct opperator"


st.write(result)