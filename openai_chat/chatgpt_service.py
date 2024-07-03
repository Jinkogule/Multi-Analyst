import asyncio
from openai import AsyncOpenAI
from django.conf import settings

openai_client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

async def generate_response(prompt, channel_layer, room_group_name):
    stream = await openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1000,
        temperature=0.3,
        stream=True,
    )

    async for chunk in stream:
        if chunk.choices and len(chunk.choices) > 0:
            content = chunk.choices[0].delta.content
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