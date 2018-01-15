from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Today is my birthday!")

# Create your views here.
