"""
text2ppt.py
generate ppt
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2024, Planet Earth"

import io
import re

from pptx import Presentation
from pptx.util import Inches, Pt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import addphoto


# Create a new PowerPoint presentation
def presentate(defined_list, img=None):
    prs = Presentation()

    # print(defined_list)

    def add_slide(prs, layout, title, subtitle):
        slide = prs.slides.add_slide(layout)
        slide.shapes.title.text = title.strip()
        slide.placeholders[1].text = subtitle
        font = slide.shapes.title.text_frame.paragraphs[0].font
        font.name = "Arial"
        font.size = Pt(30)
        font.bold = True
        font.italic = False
        for x in slide.placeholders[1].text_frame.paragraphs:
            font1 = x.font
            font1.name = "Arial"
            font1.size = Pt(16)
            font1.bold = False
            font1.italic = False
        return slide

    def add_slide_img(prs, layout, img_path):
        slide = prs.slides.add_slide(layout)
        img_path = "" + img_path
        left = Inches(1.10)
        top = Inches(0.7)
        width = Inches(8)
        height = Inches(6)
        slide.shapes.add_picture(img_path, left, top, width, height)

    title_slide_layout = prs.slide_layouts[1]  # Only text
    title_slide_layimg = prs.slide_layouts[6]  # Only image

    for d in defined_list:
        d["Summary"] = [
            re.sub(r"\d+\.\s+", "", item).strip()
            for item in d["Summary"]
            if re.sub(r"\d+\.\s+", "", item).strip()
        ]

    for i in range(0, len(defined_list)):
        add_slide(
            prs,
            title_slide_layout,
            defined_list[i]["Topic"],
            "\n".join(
                defined_list[i]["Summary"][0:len(defined_list[i]["Summary"]) // 2]
            ),
        )
        add_slide(
            prs,
            title_slide_layout,
            defined_list[i]["Topic"],
            "\n".join(
                defined_list[i]["Summary"][len(defined_list[i]["Summary"]) // 2:]
            ),
        )

        try:
            imgout = img if img else addphoto.get_images(defined_list[i]["Topic"], 1)[0]
            add_slide_img(prs, title_slide_layimg, "images/" + imgout)
        except Exception as e:
            print("got Exception ", e)
            imgout = img if img else addphoto.get_images(defined_list[i]["Topic"], 1)[0]
            add_slide_img(
                prs,
                title_slide_layimg,
                "images/" + addphoto.get_images(defined_list[i]["Topic"], 2)[1],
            )
        addphoto.empty_images()

    # Save the presentation
    binary_output = io.BytesIO()

    prs.save(binary_output)

    return binary_output

#save format presentation
def presentate_pdf(defined_list, img=None):
    binary_output = io.BytesIO()
    c = canvas.Canvas(binary_output, pagesize=letter)
    width, height = letter

    for d in defined_list:
        topic = d["Topic"]
        summary = "\n".join(d["Summary"])

        c.setFont("Helvetica-Bold", 20)
        c.drawString(72, height - 72, topic)

        c.setFont("Helvetica", 12)
        text_object = c.beginText(72, height - 108)
        text_object.setTextOrigin(72, height - 108)
        text_object.textLines(summary)
        c.drawText(text_object)

        if img:
            try:
                imgout = f"images/{img}"
                c.drawImage(imgout, 72, height - 300, width - 144, 150)
            except Exception as e:
                print(f"Image drawing failed: {e}")

        c.showPage()

    c.save()
    binary_output.seek(0)

    return binary_output
