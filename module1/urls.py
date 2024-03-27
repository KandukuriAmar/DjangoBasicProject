from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('hello1/', hello, name='hello1'),
    path('', newhomepage, name='newhomepage'),
    path('travelpackage/',  travelpackage, name="travelpackage"),
    path('print/', print1, name="print"),
    path('print_to_console1/', print_to_console, name='print_to_console1'),
    path('cusoon/', abcd, name='under'),
    path('otp/',otp,name='otp'),
    path('otps/', otps,name='otpgenerator'),
    path('date/',get_date,name='get_date'),
    path('dateu/',getdate,name='getdate'),
    path('register/', registercall,name='register'),
    path('registers/', registerloginfunction,name='registers'),
    path('chart/',pie_chart,name='pie_chart'),
    path('car/',callcar,name='car'),
    path('weather/', weatherpagecall,name='weather'),
    path('weathers/', weatherlogic,name='weatherlogic'),
    path('feedbackcall/', feebackcall,name='feedbackcall'),
    path('feedbackcalls', feeback,name='feedbackcalls'),
    #calling
    path('login/', login,name='login'),
    path('signup/', signup,name='signup'),
    path('login1/', login1,name='login1'),
    path('signup1/', signup1,name='signup1'),
    path('out/', logoutt,name='logout')
]
