from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,"index.html")

def subscribe(request):
    if request.method == "POST":
        email = request.POST['email']
        content = Subscribe(email=email)
        content.save()
        messages.success(request,"Successfully Subscribed")
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
        messages.success(request, "Your email successfully recieved to admin! Check your email too")
        return redirect('index')
    return render(request,"index.html")