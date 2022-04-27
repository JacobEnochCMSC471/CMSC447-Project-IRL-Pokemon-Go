from django.shortcuts import render
from django.http import HttpResponse
from Photo_Uploader.models import Photo_Data

# Create your views here.
def index(request):
    pet = Photo_Data.objects.filter(verified_status=False)[0]
    cont = {
        "image":pet.image,
        "pet_name":pet.pet_name
    }
    return render(request, "verification/verify_pet.html", context=cont)

#create popup for user?

#Depending on what the user presses, increment strikes or passes