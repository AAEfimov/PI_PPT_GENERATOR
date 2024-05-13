"""
gpt_ollama.py
wrapper to any GPT API
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2024, Planet Earth"


from ollama import Client

client = Client(host="http://ollama:11434")


def gpt_summarise(text):
    response = client.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": text,
            },
        ],
    )
    return response["message"]["content"]
