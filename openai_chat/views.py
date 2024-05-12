from django.shortcuts import render

from .chatgpt_service import generate_response

def chat_view(request):
    context = {}

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        chat_history = request.POST.get('chat_history', '')
        prompt = f'{chat_history}\nUser: {user_input}\nChatGPT:'
        response = generate_response(prompt)
        context['chat_history'] = f'{chat_history}\nUser: {user_input}\nChatGPT: {response}'
    return render(request, 'openai_chat/chat.html', context)

