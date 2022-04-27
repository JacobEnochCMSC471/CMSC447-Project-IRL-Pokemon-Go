from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo_Data

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. I am tired.")

#get the pet and question user
def get_pet(request):
    petset = Photo_Data.objects.filter(verified_status=False)

#create popup for user?

#Depending on what the user presses, increment strikes or passes