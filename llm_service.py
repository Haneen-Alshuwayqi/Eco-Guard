import os
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def call_llm(prompt: str) -> str:
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system="You must respond with valid JSON only. No text before or after the JSON. No markdown. No code blocks. Pure JSON object.",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        return f'{{"status": "خطأ", "score": 0, "issues": ["خطأ: {str(e)}"], "notes": "فشل الاتصال"}}'