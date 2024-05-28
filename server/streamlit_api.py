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
import text2pdf
import text2ppt


def load_image():
    """
    Create filed on the web page to upload image
    """
    uploaded_file = sl.file_uploader(label="Выберите изображение")
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

opt_dict = {"GigaChat": 0, "LLAMA3": 1}
image_dict = {"Google": 0, "Local": 1, "StableDiffusion": 2}

text = sl.text_input("Ключевое слово для генерации презентации")

customize = sl.checkbox("Customize")

presentation_title = ""
presentation_subtitle = ""
font = {"name": "Arial", "size": 12, "bold": False, "italic": False}

if customize:
    # Add fields for title and subtitle
    presentation_title = sl.text_input("Заголовок презентации")
    presentation_subtitle = sl.text_input("Подзаголовок презентации")
    f_italic = sl.checkbox("italic")
    f_bold = sl.checkbox("bold")
    f_name = sl.text_input("Font", value="Arial")
    f_size = int(sl.text_input("size", 16))
    font = {"name": f_name, "size": f_size, "bold": f_italic, "italic": f_bold}


"""
Test area on the web page to input PPT main them
"""
option_text = sl.selectbox(
    "Модель для генерации текста:", ([k for k in opt_dict.keys()])
)

ollama_host = "ollama"
ollama_port = 11434

if opt_dict[option_text] == 1:
    sl.write("OLLAMA server address")
    ollama_host = sl.text_input("host", ollama_host)
    ollama_port = int(sl.text_input("port", ollama_port))

filename = sl.text_input("Имя файла:", "presentation")
# Add a selectbox for the file format
file_format = sl.selectbox("Формат файла для сохранения:", ["pptx", "pdf"])
"""
Test area on the web page to input PPT result filename
"""
experimental = sl.checkbox("Experimental")

img = None

if experimental:
    option_image = sl.selectbox(
        "Источник изображений", ([k for k in image_dict.keys()])
    )

    if image_dict[option_image] == 1:
        img = load_image()


# Update the exec_p function to handle both formats
def exec_p():
    os.environ["OLLAMA_ADDR"] = f"http://{ollama_host}:{ollama_port}"
    if text:
        text_list = text.split(",")
        print(text_list)
        x = pdf2final_list.process(text_list, opt_dict[option_text])
        if file_format == "pptx":
            binary_output = text2ppt.presentate(
                x,
                img,
                title=presentation_title,
                subtitle=presentation_subtitle,
                font_param=font,
            )
            sl.download_button(
                label="Download pptx",
                data=binary_output.getvalue(),
                file_name=f"{filename}.pptx",
            )
        elif file_format == "pdf":
            binary_output = text2pdf.presentate_pdf(
                x,
                img,
                title="",
                subtitle="",
                font_param={
                    "name": "Helvetica",
                    "size": 12,
                    "bold": False,
                    "italic": False,
                },
            )
            sl.download_button(
                label="Download pdf",
                data=binary_output.getvalue(),
                file_name=f"{filename}.pdf",
            )
    else:
        sl.text("Пожалуйста, добавьте ключевое слово презентации")


button = sl.button("generate", on_click=exec_p)
