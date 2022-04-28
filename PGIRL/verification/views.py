from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Photo_Uploader.models import Photo_Data
import random

pet = None #drastic measures

# Create your views here.
def index(request):
    global pet
    pet = None
    items = list(Photo_Data.objects.filter(verified_status=False))

    #only pick a random pet IF there's an image hehe
    if len(items) != 0:
        pet = random.choice(items)
        #seeing what this is stored as...
        print("pet.pet_name")
    else:
        #send to evil html boohoo
        return render(request, "verification/empty_error.html")

    image_name = str(pet.image)
    cont = {
        "image": "../../../media/" + image_name,
        "pet_name":pet.user_label,
    }
    return render(request, "verification/verify_pet.html", context=cont)

#if they pressed yes, increase passes
def answer_yes(request):
    global pet
    pet.increment_passes()
    if pet.get_passes() >= 3:
        #get a stat boost! :D
        pet.stat_hp+=5
        print("Increased health for that pet.")
        pass

    pet.save()
    print("Increased passes for that image.")
    return HttpResponseRedirect(reverse('index'))

#if they pressed no, increase strikes
def answer_no(request):
    #L :(
    global pet
    pet.increment_strikes()
    print("Increased strikes for that image.")

    pet.save()
    return HttpResponseRedirect(reverse('index'))
