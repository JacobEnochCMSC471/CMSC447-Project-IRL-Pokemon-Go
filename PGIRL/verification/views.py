from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Photo_Uploader.models import Photo_Data
from django.urls import reverse
from Photo_Uploader.views import remove_bad_photos
import random

pet = None #drastic measures
THRESHOLD = 5

# Create your views here.
def verify(request):
    global pet
    pet = None
    items = list(Photo_Data.objects.filter(verified_status=False))

    #only pick a random pet IF there's an image hehe
    if len(items) != 0:
        pet = random.choice(items)
        #seeing what this is stored as...
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
    print("___`*`*`*`*`**`*`*`**`*`*`*`**`*`*`*`*`*`**`*`*`*`_______got here lmao__________________________________________________")
    pet.increment_passes()
    if pet.get_passes() >= 3:
        pet.verified_status = True
        #get a stat boost! :D
        pet.stat_hp+=5
        print("Increased health for that pet.")
        pass

    pet.save()
    print("Increased passes for that image.")
    return redirect('verify')

#if they pressed no, increase strikes
def answer_no(request):
    #L :(
    global pet
    pet.increment_strikes()
    print("----------^^-^----^---^Increased strikes for that image.----^-------------^^----------^---^--^^")

    #remove pet from directory and DB if strikes reached
    if pet.get_strikes() >= THRESHOLD:
        remove_bad_photos(THRESHOLD+1)
        pet.delete()
        return redirect('verify')

    pet.save()
    return redirect('verify')
