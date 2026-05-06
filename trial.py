import streamlit as st
from PIL import Image  # Import Image from Pillow
st.title("TRIALLLL...TITLE!!!")
st.header("This is a header") 
st.subheader("This is a subheader")
st.text("Hello WORLD!!!Dis is a text")
st.markdown("### This is a markdown")
st.success("Success")

st.info("Information")

st.warning("Warning")

st.error("Error")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)
st.write("Text with write")

# Writing python inbuilt function range()
st.write(range(10))
img = Image.open("img1.png") # Open the image file
st.image(img, width=200) # Display the image with a specified width
# Display a checkbox with the label 'Show/Hide'
if st.checkbox("Show/Hide"):
    # Show this text only when the checkbox is checked
    st.text("Showing the widget")
# Create a radio button to select gender
status = st.radio("Select Gender:", ['Male', 'Female'])

# Display the selected option using success message
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")
