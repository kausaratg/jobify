from django.shortcuts import render, redirect
from django.http import JsonResponse
import google.generativeai as genai

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone
import re

gemini_apikey= "AIzaSyAgLVpWzWKiNWKcqo1ADNzrLwtaGSbxZJ0"

# Create your views here.
def ask_geminiAi(message):
    genai.configure(api_key = gemini_apikey)
    model = genai.GenerativeModel("gemini-1.5-flash", system_instruction="You are Jobify, You help people with searching for job")
    response = model.generate_content (message)
    response = re.sub(r"(\*\*|\*)", "", response.text)
    
    # Add line breaks after punctuation marks (., !, ?, ;)
    response = re.sub(r"([!:?;]) ", r"\1<br>", response)
    
    # Remove extra spaces
    response = re.sub(r"\s+", " ", response).strip()
    
    # Ensure line breaks are spaced appropriately
    response_lines = response.split("<br>")
    formatted_response = "<br>".join(line.strip() for line in response_lines if line.strip())
    
    return formatted_response
 



def chatbot(request):
    chats = Chat.objects.filter(user = request.user)
    if request.method == "POST":
        message = request.POST.get('message')
        response = ask_geminiAi(message)
       
        chat = Chat (user = request.user, message = message, response = response, created_at = timezone.now()
        )
        chat.save()

        return JsonResponse({'message':message, 'response': response})
    return render(request, "chatbot.html", {'chats':chats})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = "Invalid username or password"
            return render(request,  'login.html', {'error_message':error_message})
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
               error_message ="Error creating account"
               return render(request, 'register.html', {'error_message':error_message})
        else:
            error_message = "Password don't match"
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('login')