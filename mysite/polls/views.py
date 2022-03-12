from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# To call this view, we need to map it to URL.
def index(request):
    return HttpResponse("Hello, this is polls index.")
