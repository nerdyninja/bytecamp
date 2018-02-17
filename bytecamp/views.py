from django.http import HttpResponse
from django.shortcuts import render

from teams.models import Team

# Index Page
def index(request, *args, **kwargs):
	return render(request, "pages/index.html", {"title": "ByteCamp '18"})

# About Page
def about(request, *args, **kwargs):
	return render(request, "pages/about.html", {"title": "About - ByteCamp '18"})

# Home Page
def home(request, *args, **kwargs):
	return render(request, "pages/home.html", {"title": "Home - ByteCamp '18"})

# Countdown Page
def countdown(request, *args, **kwargs):
	return render(request, "pages/countdown.html", {"title": "Countdown - ByteCamp '18"})

# Timer Page
def timer(request, *args, **kwargs):
	return render(request, "pages/timer.html", {"title": "Tick Tick - ByteCamp '18"})
