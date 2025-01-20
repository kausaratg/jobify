from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai

gemini_apikey= "AIzaSyAgLVpWzWKiNWKcqo1ADNzrLwtaGSbxZJ0"

# Create your views here.
def ask_geminiAi(message):
    genai.configure(api_key = gemini_apikey)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content (message)
    return response.text


def chatbot(request):
    if request.method == "POST":
        message = request.POST.get('message')
        response = ask_geminiAi(message)
        return JsonResponse({'message':message, 'response': response})
    return render(request, "chatbot.html")
