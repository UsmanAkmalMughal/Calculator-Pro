import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for the numbers
number1 = st.text_input("Enter the first number:", "0")
number2 = st.text_input("Enter the second number:", "0")

# Dropdown menu for selecting the operation
operation = st.selectbox("Select an operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Button to perform the calculation
if st.button("Calculate"):
    try:
        # Convert inputs to floats
        num1 = float(number1)
        num2 = float(number2)

        # Perform the calculation based on the selected operation
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"

        # Display the result
        st.success(f"The result is: {result}")

    except ValueError:
        st.error("Please enter valid numbers.")

