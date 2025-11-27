import streamlit as st
from PIL import Image  # Pillow library, used for opening and processing images

# Create a collapsible UI section.
# The camera widget will appear only after the user opens the expander.
with st.expander("Start Camera"):
    # Camera input widget: opens the webcam and allows the user to take a picture.
    # Once the picture is captured, it is stored in `camera_image`.
    camera_image = st.camera_input("Camera")

# After the user takes a photo, process it.
if camera_image:
    # Open the captured image using Pillow so we can manipulate it.
    img = Image.open(camera_image)

    # Convert the image to grayscale ("L" stands for luminance).
    gray_img = img.convert("L")

    # Display the grayscale version back in the app.
    st.image(gray_img)

