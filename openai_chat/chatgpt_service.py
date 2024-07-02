import asyncio
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

async def generate_response(prompt, channel_layer, room_group_name):
    response = await openai.ChatCompletion.acreate(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1000,
        temperature=0.3,
        stream=True,
    )

    async for chunk in response:
        if 'choices' in chunk and len(chunk['choices']) > 0:
            content = chunk['choices'][0].get('delta', {}).get('content', '')
            if content:
                for char in content:
                    await channel_layer.group_send(
                        room_group_name,
                        {
                            'type': 'chat_message',
                            'message': char
                        }
                    )
                    await asyncio.sleep(0.01)