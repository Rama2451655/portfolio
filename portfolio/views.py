from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def resume(request):
    return render(request, 'portfolio/resume.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
from .models import Project

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': all_projects})
from .forms import ContactForm

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # process data (save/send email/etc.)
            print(form.cleaned_data)
            return render(request, 'portfolio/contact.html', {
                'form': ContactForm(),
                'success': True
            })
    return render(request, 'portfolio/contact.html', {'form': form})
from django.core.mail import send_mail

def contact(request):
    form = ContactForm()
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"Message from {name} ({email}):\n\n{message}"

            send_mail(
                subject="New Contact Form Message",
                message=full_message,
                from_email=email,
                recipient_list=['your_email@gmail.com'],  # Your email
            )
            success = True
            form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form, 'success': success})
from .models import Skill, Education, Certificate

def about(request):
    skills = Skill.objects.all()
    education = Education.objects.all()
    certs = Certificate.objects.all()
    return render(request, 'portfolio/about.html', {
        'skills': skills,
        'education': education,
        'certs': certs,
    })
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def download_resume(request):
    template_path = 'portfolio/resume_template.html'
    context = {'name': 'Your Name', 'skills': ['Python', 'Django']}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa.CreatePDF(html, dest=response)
    return response
from django.shortcuts import render

def resume_view(request):
    return render(request, 'resume.html')
