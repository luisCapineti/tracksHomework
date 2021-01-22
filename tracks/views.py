from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def table_view_items(request):
    return HttpResponse('We are in!')