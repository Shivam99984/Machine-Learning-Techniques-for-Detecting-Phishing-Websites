from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from home1.models import User_wedsite
from django.contrib.auth.decorators import login_required



@login_required(login_url='Login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='Login')  # Apply login_required to home2
def home2(request):
    return render(request, 'home2.html')

@login_required(login_url='Login')  # Apply login_required to main



def Signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the email already exists
        if User_wedsite.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please choose a different one.")
            return render(request, 'sign-up10.html')

        try:
            my_user = User_wedsite.objects.create_user(email=email, password=password)
            my_user.save()
            print(email, password)
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('Login')  # Redirect to the login page after successful signup
        except Exception as e:
            messages.error(request, "An error occurred. Please try again.")
            return render(request, 'sign-up10.html')

    return render(request, 'sign-up10.html')


def Login(request):
    if request.method == 'POST':
        email1 = request.POST.get('email')
        password1 = request.POST.get('password')
        print(email1, password1)

        user = authenticate(request, email=email1, password=password1)

        if user is not None:
            login(request, user)
            return redirect('home2')
        else:
            messages.error(request, "Invalid email or password. Please try again.")

    return render(request, 'sign-in8.html')


def Logout(request):
    logout(request)
    return redirect('Login')


import warnings
import numpy as np
import pickle
from django.shortcuts import render
from django.http import JsonResponse
from .feature import FeatureExtraction
import os

# Load the model
warnings.filterwarnings('ignore')
model_path = os.path.join(os.path.dirname(__file__), 'pickle/model.pkl')
with open(model_path, 'rb') as file:
    gbc = pickle.load(file)



def index(request):
    if request.method == "POST":
        url = request.POST.get("url")
        obj = FeatureExtraction(url)
        x = np.array(obj.get_features_list()).reshape(1, 30)

        y_pred = gbc.predict(x)[0]
        y_pro_phishing = gbc.predict_proba(x)[0, 0]
        y_pro_non_phishing = gbc.predict_proba(x)[0, 1]

        # Return JSON response
        return JsonResponse({"xx": round(y_pro_non_phishing, 2), "url": url})

    return render(request, "index.html", {"xx": -1})
