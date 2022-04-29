from django.shortcuts import render,redirect,HttpResponse
from . models import *
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

# Create your views here.

def index(request):
    return render(request,"index.html")

def subscribe(request):
    if request.method == "POST":
        email = request.POST['email']
        content = Subscribe(email=email)
        content.save()
        messages.success(request,"Successfully Subscribed: Check your Email")
        try:
            send_mail(f'From (No Name)', f'Hi, someone Successfully subscribed using this email {email}',email, ['talhasarwar289@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        try:
            send_mail(f'From Admin', f'Hi you successfully subscribed using {email} email', 'talhasarwar289@gmail.com',[email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('index')
    return render(request,"index.html")

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        website = request.POST['website']
        message = request.POST['message']
        if len(phone) < 10 or len(phone) > 20:
            messages.error(request,"Invalid Number: Phone Number Length must be minimum to 10 and maximum to 20")
            return redirect('index')
        content = Signup(name=name,email=email,phone=phone,website=website,message=message)
        content.save()
        messages.success(request, "You have Successfully Signup")
        return redirect('index')
    return render(request,"index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        website = request.POST['website']
        company = request.POST['company']
        message = request.POST['message']
        budget = request.POST['budget']
        if len(phone) < 10 or len(phone) > 20:
            messages.error(request,"Invalid Number: Phone Number Length must be minimum to 10 and maximum to 20")
            return redirect('index')
        content = Contact(name=name,email=email,phone=phone,website=website,company=company,budget=budget,message=message)
        content.save()
        try:
            send_mail(f'From {name}', f'Hi, {name} wants to contact with you, \nMore Details are mentioned below: '
                                      f' \nEmail: "{email}",\nMessage: "{message}",\nWebsite: "{website}",\nPhone: "{phone}",\nCompany: "{company}",'
                                      f'\nBudget: "{budget}"',email, ['talhasarwar289@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        try:
            send_mail(f'From Admin', f'Hi {name}, Your Email has been successfully recieved to admin. we will contact with you soon. your details are mentioned below:'
                                      f' \nEmail: "{email}",\nMessage: "{message}",\nWebsite: "{website}",\nPhone: "{phone}",\nCompany: "{company}",'
                                      f'\nBudget: "{budget}"', 'talhasarwar289@gmail.com',[email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request, "Your email successfully recieved to admin! Check your email too")
        return redirect('index')
    return render(request,"index.html")