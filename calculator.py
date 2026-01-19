import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


st.title("🧮 Calculator")

# Inputs
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

st.write("### Choose Operation")

col1, col2, col3, col4 = st.columns(4)

result = None

try:
    if col1.button("➕ Add"):
        result = add(num1, num2)

    if col2.button("➖ Subtract"):
        result = subtract(num1, num2)

    if col3.button("✖ Multiply"):
        result = multiply(num1, num2)

    if col4.button("➗ Divide"):
        result = divide(num1, num2)

    if result is not None:
        st.success(f"Result: {result}")

except ValueError as e:
    st.error(str(e))
