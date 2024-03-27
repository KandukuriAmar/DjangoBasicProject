import random
import string

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("<center>Welcome to TTM Homepage</center>")


def abcd(request):
    return HttpResponse("<center>Site Under Maintaince</center>")


def newhomepage(request):
    return render(request, 'newHomepage.html')


def travelpackage(request):
    return render(request, 'travelpackage123.html')


def print1(request):
    return render(request, 'print_to_console1.html')


def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'Use input:{user_input}')
        # return HttpResponse('From submitted successfully')
        a1 = {'user_input': user_input}
        return render(request, 'print_to_console1.html', a1)


def otp(request):
    return render(request, 'otpgenerator.html')


def otps(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'Use input:{user_input}')
        a2 = int(user_input)
        ran1 = ''.join(random.sample(string.digits, k=a2))
        a1 = {'ran1': ran1}
        return render(request, 'otpgenerator.html', a1)


import datetime
from django.shortcuts import render
from .forms import *


def getdate(request):
    return render(request, 'get_date.html')


def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request, 'get_date.html', {'updated_date': updated_date})
        else:
            form = IntegerDateForm()
        return render(request, 'get_date.html', {'form': form})
#regidster
def registercall(request):
    return render(request,'register.html')

from .models import *
from django.shortcuts import render,redirect
def registerloginfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')

        # Check for existing email
        if Amar.objects.filter(email=email).exists():
            return HttpResponse("Email already registered")
        
        # Create new user
        Amar.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('newhomepage')
    
    return render(request, 'register.html')

#------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})
class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')

#-----------------------------------------------
def callcar(request):
    return render(request, 'Cards.html')

#weather app
import requests
def weatherpagecall(request):
    return render(request,'weatherappinput.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '2798835ff2448357b977cb95f3038106'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})

def feebackcall(request):
    return render(request,'feedback.html')
#feed back
# def feeback(request):
#     if request.method =='POST':
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         email = request.POST.get('email')
#         comment = request.POST.get('comment')
#         Feed.objects.create(fname=fname,lname=lname,email=email,comment=comment)
#         return redirect('newhomepage')
#     return render(request, 'feedback.html')

#feedback with mail
def feeback(request):
    if request.method =='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        Feed.objects.create(fname=fname,lname=lname,email=email,comment=comment)
        send_mail(
            'Thank you for your feedback',
            comment,
            '2200030959cseh@gmail.com',
            [email],
            fail_silently=False,
        )
    print(f'Message sent to: {email}')
    return HttpResponse("<h1><center>Thank You For Your FeedBack a Mail has sent to You!</center></h1>")
    

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')

from django.contrib.auth import login as auth_login  # Renaming login to avoid conflicts

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Use the imported login function
            return redirect('newhomepage')
        else:
            return redirect('login')  # Display an error message
    else:
        return redirect('login')
    
def signup1(request):
 if request.method=="POST":
    username=request.POST['username']
    pass1=request.POST['password']
    pass2=request.POST['password1']
    if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Usename already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'login.html')
    else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')
    
from django.contrib.auth import logout

def logoutt(request):
    logout(request)
    # return render(request,'newHomePage.html')
    return redirect("newhomepage")
