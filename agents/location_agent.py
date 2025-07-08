from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1")

def extract_location_name(user_input: str) -> str:
    try:
        prompt = f"""Extract the destination city name from this sentence:
        "{user_input}"
        Only return the city name without any extra words."""

        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",  
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=20
        )

        city_name = response.choices[0].message.content.strip()
        return city_name

    except Exception as e:
        print("❌ Error:", str(e))
        return "unknown"
