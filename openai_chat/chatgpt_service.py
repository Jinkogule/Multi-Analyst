import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1000,
        temperature=0.3,
    )
    return response['choices'][0]['message']['content'].strip()
