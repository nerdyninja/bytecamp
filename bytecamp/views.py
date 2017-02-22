from django.http import HttpResponse
from django.shortcuts import render

# Index Page
def index(request, *args, **kwargs):
	return render(request, "pages/index.html", {"title": "ByteCamp '17"})

# About Page
def about(request, *args, **kwargs):
	return render(request, "pages/about.html", {"title": "About - ByteCamp '17"})

# Help Page
def help(request, *args, **kwargs):
	return render(request, "pages/help.html", {"title": "Help - ByteCamp '17"})

# Home Page
def home(request, *args, **kwargs):
	return render(request, "pages/home.html", {"title": "Home - ByteCamp '17"})

# Teams Page
def teams(request, *args, **kwargs):
	return render(request, "pages/teams.html", {"title": "Teams - ByteCamp '17"})
