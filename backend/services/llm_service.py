import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_llm_response(customer_message, tone, length):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Write a debt collection message.

    Tone: {tone}
    Length: {length}
    Customer message: {customer_message}
    """

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {
                "role": "system",
                "content": "You are a debt collection AI assistant. Be compliant, polite, and strategic."
            },
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        print("Status Code:", response.status_code)

        if response.status_code != 200:
            return f"LLM API Error: {response.status_code} - {response.text}"

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Exception in LLM call: {str(e)}"