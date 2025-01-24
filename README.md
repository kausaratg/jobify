# **Jobify**

Jobify is a Django-based web application that helps users navigate job-related issues with ease. It features an AI chatbot for job advice, a CV analyzer for personalized feedback, and tips to improve resumes for better job opportunities.

---

## **Features**

- 🌟 **AI Chatbot**: Engage with an AI-powered chatbot to ask job-related questions and receive expert advice.
- 📄 **CV Analyzer**: Upload your CV to analyze its strengths and weaknesses, and get actionable suggestions for improvement.
- 📄 **PDF Download**:Download your CV analysis result as PDF.
- 🛠 **Resume Tips**: Get personalized recommendations to improve your resume for specific industries or roles.

---

## **Technologies Used**

- **Backend**: Django, Python  
- **Frontend**: HTML, CSS, JavaScript  
- **Database**: SQLite (default, can be switched to PostgreSQL)  
- **AI Integration**: Gemini Model 
- **PDF Handling**: PyPDF2  
- **File Storage**: Django's default media file system  

---

## **Installation**

Follow these steps to set up Jobify locally on your machine.

## To install and run the project
1. Create a django environment 
2. clone the Repository
 ```bash
 git clone https://github.com/kausaratg/jobify.git
 ``` 
3  Enter into the directory
```bash
cd jobify
```
4.  Pull any recent change from main branch
   ```bash
 git pull origin main
```
5.  create a virtual env
  ```bash
python -m venv env
```
6. Activate the virtual env
```bash
env/Scripts/activate
```
7. Install dependencies
 ```bash
pip install -r requirements.txt
```
8. Make migration
```bash
python manage.py makemigration
```
9. Migrate the project
```bash
python manage.py migrate
```
10. Run local Server
```bash
python manage.py runserver
```

## **Usage**
### **1. Upload Your CV**
- Go to the "CV Analyzer" section.
- Upload your CV in PDF format.
- View detailed analysis and suggestions to improve your CV. 
### **2. Chat with the AI**
- Visit the "Jobify Chatbot" section.
- Ask the chatbot job-related questions like:
- "How can I improve my CV for a software engineering role?"
- "What certifications should I take for data analysis?"
### **3. Download CV Feedback**
- After analyzing your CV, you can download the feedback as a PDF document.

### Home Page
![Screenshot 2025-01-24 131136](https://github.com/user-attachments/assets/27942376-1830-4f75-b369-11a0dcb8bb6f)

### Chat with AI
![Screenshot 2025-01-23 195707](https://github.com/user-attachments/assets/6c3fd8d3-6c49-466d-9e96-4856e2b8fa67)

### Analyze your CV
![Screenshot 2025-01-24 131156](https://github.com/user-attachments/assets/97d94578-b2e1-4c9b-8913-ce4e396365eb)

### Built with 🤍 Jobify by <a href="">Kausarat Giwa</a>
