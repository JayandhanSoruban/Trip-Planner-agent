from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

class LLMWrapper:
    def __init__(self):
        hf_token = os.getenv("HUGGINGFACE_API_TOKEN")
        self.client = InferenceClient(
            model="HuggingFaceH4/zephyr-7b-beta",  # lightweight, chat-friendly
            token=hf_token
        )

    def chat(self, prompt: str) -> str:
        response = self.client.text_generation(prompt, max_new_tokens=300)
        return response.strip()
