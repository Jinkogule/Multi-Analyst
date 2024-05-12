import openai

openai.api_key = 'sk-proj-yr3h5dBAyOZv4GV0GWaqT3BlbkFJ7iYbVFpGvjVzw35fDwJj'

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content'].strip()
