"""
text2ppt.py
generate ppt
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2024, Planet Earth"

import io
import re

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from text2ppt import default_font


# Create a new PDF presentation
def presentate_pdf(
    defined_list, img=None, title="", subtitle="", font_param=default_font
):

    binary_output = io.BytesIO()
    c = canvas.Canvas(binary_output, pagesize=letter)
    width, height = letter

    def add_slide(c, title, subtitle):
        c.setFont(font_param["name"], font_param["size"])
        if font_param["bold"]:
            c.setFont(f"{font_param['name']}-Bold", font_param["size"])
        if font_param["italic"]:
            c.setFont(f"{font_param['name']}-Oblique", font_param["size"])
        c.drawString(72, height - 72, title.strip())
        text_object = c.beginText(72, height - 108)
        text_object.setTextOrigin(72, height - 108)
        text_object.textLines(subtitle)
        c.drawText(text_object)

    def add_slide_img(c, img_path):
        img_path = "" + img_path
        try:
            c.drawImage(img_path, 72, height - 300, width - 144, 150)
        except Exception as e:
            print(f"Image drawing failed: {e}")

    for d in defined_list:
        d["Summary"] = [
            re.sub(r"\d+\.\s+", "", item).strip()
            for item in d["Summary"]
            if re.sub(r"\d+\.\s+", "", item).strip()
        ]

    for i in range(0, len(defined_list)):
        add_slide(
            c,
            defined_list[i]["Topic"] if len(title) == 0 else title,
            "\n".join(
                defined_list[i]["Summary"][0:len(defined_list[i]["Summary"]) // 2]
            ),
        )
        c.showPage()

        add_slide(
            c,
            defined_list[i]["Topic"] if len(subtitle) == 0 else subtitle,
            "\n".join(
                defined_list[i]["Summary"][len(defined_list[i]["Summary"]) // 2:]
            ),
        )
        c.showPage()

        if img:
            try:
                imgout = f"images/{img}"
                add_slide_img(c, imgout)
            except Exception as e:
                print(f"Image drawing failed: {e}")

        c.showPage()

    c.save()
    binary_output.seek(0)

    return binary_output
