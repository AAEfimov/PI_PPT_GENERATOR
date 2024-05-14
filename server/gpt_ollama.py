"""
gpt_ollama.py
wrapper to any GPT API
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2024, Planet Earth"

import os

from ollama import Client


OLLAMA_HOST = os.getenv("OLLAMA_ADDR") 

client = Client(host=OLLAMA_HOST)


def gpt_summarise_ollama(text):
    response = client.chat(model="llama3", messages=[{"role": "user", "content": text}])
    return response["message"]["content"]
