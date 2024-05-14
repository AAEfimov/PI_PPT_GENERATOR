"""
gpt_sber.py
wrapper to any GPT API
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2024, Planet Earth"


import os

from gigachat import GigaChat

GPT_TOKEN = os.getenv("GPT_TOKEN")


def gpt_summarise_sber(text):
    with GigaChat(credentials=GPT_TOKEN, verify_ssl_certs=False) as giga:
        print(text)
        response = giga.chat(text)
        print(response.choices[0].message.content)
        return response.choices[0].message.content
