from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Photo_Uploader.models import Photo_Data
import random

pet = NULL #drastic measures

# Create your views here.
def index(request):
    items = list(Photo_Data.objects.filter(verified_status=False))
    global pet
    pet = random.choice(items)

    cont = {
        "image":pet.image,
        "pet_name":pet.pet_name
    }
    return render(request, "verification/verify_pet.html", context=cont)

#if they pressed yes
def answer_yes(request):
    global pet
    pet.increment_passes()
    if pet.get_passes() >= 3:
        #get a stat boost! :D
        pet.stat_hp+=5
        print("Increased health for that pet.")
        pass

    print("Increased passes for that image.")
    return HttpResponseRedirect(reverse('index'))

#if they pressed no
def answer_no(request):
    #L :(
    global pet
    pet.increment_strikes()
    print("Increased strikes for that image.")
    return HttpResponseRedirect(reverse('index'))

#Depending on what the user presses, increment strikes or passes