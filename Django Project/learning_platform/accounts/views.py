from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser
import speech_recognition as sr

from django.shortcuts import render

from django.shortcuts import render

def dashboard(request):
    return render(request, "accounts/dashboard.html")  # Make sure this template exists


def login_selection(request):
    return render(request, 'accounts/login_selection.html')  # Make sure this template exists

# Blind Student Login (Voice-Based)
import speech_recognition as sr
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
def blind_login(request):
    if request.method == "POST":
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Adjusting for background noise... Speak now.")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for noise

            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)  # Increased timeout
                print("Processing speech...")

                spoken_password = recognizer.recognize_google(audio).strip()
                print("Recognized:", spoken_password)

                if spoken_password == "123":
                    user = authenticate(username="blind_user", password="123")
                    if user:
                        login(request, user)
                        return redirect(reverse("dashboard"))
                    return JsonResponse({"message": "Authentication failed"}, status=401)
                else:
                    return JsonResponse({"message": "Incorrect password"}, status=400)

            except sr.WaitTimeoutError:
                print("No speech detected. Try speaking again.")
                return JsonResponse({"message": "No speech detected. Please try again."}, status=400)
            except sr.UnknownValueError:
                print("Speech not understood. Speak more clearly.")
                return JsonResponse({"message": "Could not understand. Try again."}, status=400)
            except sr.RequestError:
                print("Speech recognition service unavailable.")
                return JsonResponse({"message": "Speech recognition service unavailable."}, status=500)

    return render(request, "accounts/blind_login.html")

# Mute Student Login (Secret Code)
def mute_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        secret_code = request.POST.get("secret_code")

        user = CustomUser.objects.filter(username=username, secret_code=secret_code, user_type="mute").first()
        if user:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            return render(request, "mute_login.html", {"error": "Invalid secret code"})

    return render(request, "mute_login.html")

# Deaf & Physically Disabled Student Login (Regular Login)
def regular_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user and user.user_type == "regular":
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            return render(request, "regular_login.html", {"error": "Invalid credentials"})

    return render(request, "regular_login.html")
