from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homeView(request):
	page_content = "<h1>Hello There!!</h1>"
	return HttpResponse(page_content)