"""
streamlit_api.py
Streamlit based web interface
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2024, Planet Earth"

import io
import os

import streamlit as sl
from PIL import Image

import pdf2final_list
import text2ppt


def load_image():
    """
    Create filed on the web page to upload image
    """
    uploaded_file = sl.file_uploader(label="Выберите изобрадение")
    # Check if an image file is uploaded
    if uploaded_file is not None:
        # Get the image data
        image_data = uploaded_file.getvalue()

        # Open the image using the BytesIO and Image modules
        img = Image.open(io.BytesIO(image_data))

        path = "images"
        # Save the uploaded image with its original name
        if not os.path.exists(path):
            os.makedirs(path)

        
        img.save(os.path.join(path, uploaded_file.name))

        # Return the name of the uploaded image file
        return uploaded_file.name
    else:
        # If no image is uploaded, return None
        return None


sl.title("Генератор презентаций, по ключевым словам или основным мыслям из текста")

text = sl.text_input("Ключевое слово для генерации презентации")
"""
Test area on the web page to input PPT main them
"""
filename = sl.text_input("Имя файла:", "PPT.pptx")
"""
Test area on the web page to input PPT result filename
"""
img = load_image()


def exec_p():
    """
    Button calback. Will check text.
    Call main functional to generate PPT
    """
    if text:
        text_list = text.split()
        print(text_list)
        x = pdf2final_list.process(text_list)
        binary_output = text2ppt.presentate(x, img)

        sl.download_button(label = 'Download pptx',
                   data = binary_output.getvalue(),
                   file_name = filename)

    else:
        sl.text("Пожалуйста, добавьте ключевое слово презентации")


button = sl.button("generate PPT", on_click=exec_p)
"""
Streamlit button.
after click, run calback and make_magic
"""
