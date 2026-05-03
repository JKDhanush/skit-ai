import requests

BASE_URL = "http://localhost:8000"

def generate_response(message, tone, length):
    res = requests.post(
        f"{BASE_URL}/generate",
        json={
            "customer_message": message,
            "tone": tone,
            "length": length
        }
    )

    if res.status_code == 200:
        return res.json()
    else:
        raise Exception(f"Backend error: {res.status_code} - {res.text}")