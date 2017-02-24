from django.http import HttpResponse
from django.shortcuts import render

from teams.models import Team

# Index Page
def index(request, *args, **kwargs):
	return render(request, "pages/index.html", {"title": "ByteCamp '17"})

# About Page
def about(request, *args, **kwargs):
	return render(request, "pages/about.html", {"title": "About - ByteCamp '17"})

# Home Page
def home(request, *args, **kwargs):
	return render(request, "pages/home.html", {"title": "Home - ByteCamp '17"})

# Teams Page
def teams(request, *args, **kwargs):
	query = Team.objects.order_by('name')
	context = {
		"teams_list": query,
		"title": "Teams - ByteCamp '17"
	}
	return render(request, "pages/teams.html", context)

# Countdown Page
def countdown(request, *args, **kwargs):
	return render(request, "pages/countdown.html", {"title": "Countdown - ByteCamp '17"})

# Timer Page
def timer(request, *args, **kwargs):
	return render(request, "pages/timer.html", {"title": "Tick Tick - ByteCamp '17"})
