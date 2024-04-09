import os

from gigachat import GigaChat

GPT_TOKEN = os.getenv("GPT_TOKEN")


def gpt_summarise(text):
    with GigaChat(credentials=GPT_TOKEN, verify_ssl_certs=False) as giga:
        print(text)
        response = giga.chat(text)
        print(response.choices[0].message.content)
        return response.choices[0].message.content
