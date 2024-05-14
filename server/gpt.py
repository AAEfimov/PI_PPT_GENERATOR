"""
gpt_sber.py
wrapper to any GPT API
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2024, Planet Earth"

import gpt_ollama
import gpt_sber

SBER_LLM = 0
OLLAMA_LLM = 1


def gpt_summarise(text, llm_model=SBER_LLM):

    retval = ""
    if llm_model == SBER_LLM:
        retval = gpt_sber.gpt_summarise_sber(text)
    elif llm_model == OLLAMA_LLM:
        retval = gpt_ollama.gpt_summarise_ollama(text)
    else:
        retval = "Wrong Model"

    return retval
