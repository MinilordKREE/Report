# utils.py
import pandas as pd
from io import StringIO
import openai
import time
from sklearn.preprocessing import LabelEncoder
import csv
import numpy as np
import os
import functools
import logging

logging.basicConfig(level=logging.INFO)

def retry_on_exception(exceptions, retries=5, delay=10):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = retries
            while attempts > 0:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logging.warning(f"{e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    attempts -= 1
            raise RuntimeError("Maximum retries exceeded.")
        return wrapper
    return decorator

@retry_on_exception((openai.error.RateLimitError, openai.error.ServiceUnavailableError, OSError, TimeoutError), retries=3, delay=30)
def decoder_for_gpt(input, max_length):
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {"role": "user", "content": input}
        ],
        max_tokens=max_length,
        temperature=1,
    )
    return response["choices"][0]['message']['content']

def openai_key_config(api_key=None, key_file = '../api_keys.txt'):
    if api_key is not None:
        print(f'api_key: {api_key}')
        openai.api_key = api_key.strip()
        return
    if not os.path.exists(key_file):
        raise FileNotFoundError(f"Please enter your API key in {key_file}")
    api_key = open(key_file).readlines()[0].strip()
    print(f'api_key: {api_key}')
    openai.api_key = api_key