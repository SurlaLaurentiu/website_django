from django.http import HttpResponse, request
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    return render(request, "index.html", {})

def contact(request):
    if request.method == 'POST':
        
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

    
        message = f'''
        New message: {message}
        From: {email}
        Nume: {name}
        '''
        
        send_mail(subject, message, "", ['laurentiutestpy@gmail.com'])


    return render(request, "contact.html", {})


def aranjamente(request):
    return render(request, "aranjamente.html", {})

def evenimente(request):
    return render(request, "evenimente.html", {})   
