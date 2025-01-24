from django.shortcuts import render, redirect
from django.http import JsonResponse
import google.generativeai as genai

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.contrib.auth.decorators import login_required

from django.utils import timezone
import re
import markdown
import textwrap
from chatbot.forms import UploadFileForm
from PyPDF2 import PdfReader

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from decouple import config

gemini_apikey=  config('gemini_apikey')


def home(request):
    return render(request, 'index.html')


def to_markdown(text):
  text = text.replace('•', '  *')
  return markdown.markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# Create your views here.
def ask_geminiAi(message):
    genai.configure(api_key = gemini_apikey)
    model = genai.GenerativeModel("gemini-1.5-flash", system_instruction="You are Jobify, You help people with searching for job")
    response = model.generate_content (message)
  

    return to_markdown(response.text)


@login_required(login_url='login')
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

def analyze():

    pass
def analyse_cv(request):
    uploadform = UploadFileForm()
    if request.method == 'POST':
        resume = UploadFileForm(request.POST, request.FILES)
                # Get the uploaded file
        pdf_file = request.FILES['resume']
        pdf_reader = PdfReader(pdf_file)
        
        extracted_text = " "
        for page in pdf_reader.pages:
            extracted_text += page.extract_text()

        genai.configure(api_key = gemini_apikey)
        model = genai.GenerativeModel("gemini-1.5-flash", system_instruction="You are Jobify, You help people with searching for job")
        response = model.generate_content (f"please analyze this text {extracted_text}")
    
        edited_response =  to_markdown(response.text)
        context = {"edited_response" : edited_response}
        request.session['pdf_context'] = context
        
        return render(request, 'resume_analysis_result.html', {"edited_response": edited_response})

    else:
        context = {"file_form": UploadFileForm()}
        return render(request, "cv_analyser.html", context)



def download_pdf(request):
    # Load the template and context
   # Dynamically generate the same data
    # Retrieve context stored in the session
    context = request.session.get('pdf_context', {})
    
    # Check if the context is available
    if not context or "edited_response" not in context:
        return HttpResponse("No data available to generate PDF.", status=400)
    
    # Render the template to an HTML string
    html_content = render_to_string('resume_analysis_result.html', context)

    # Create a response to attach the PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="jobify_result.pdf"'

    # Generate PDF
    pisa_status = pisa.CreatePDF(html_content, dest=response)

    # If an error occurs
    if pisa_status.err:
        return HttpResponse(f'Error generating PDF: {pisa_status.err}', status=500)
    
    return response