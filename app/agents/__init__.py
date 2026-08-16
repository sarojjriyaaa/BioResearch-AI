import os

def __init__(self):

    api_key = os.getenv("GEMINI_API_KEY")

    print("API KEY FOUND:", api_key is not None)

    if not api_key:
        raise ValueError("No GEMINI_API_KEY found")

    self.client = configure_gemini(api_key)