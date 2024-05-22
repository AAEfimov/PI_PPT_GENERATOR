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

default_font = {"name": "Arial", "size": 12, "bold": False, "italic": False}

def presentate_pdf(defined_list, img=None):
    """
    Generate PDF presentation from the list of topics and summaries
    """
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