from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Item
from Photo_Uploader.models import Photo_Data

# Create your views here.
def select_list(request):
    return render(request, 'Inventory/select_list.html')

def pet_list(request):
    pet_list = Photo_Data.objects.order_by('-pet_name')
    return render(request, 'Inventory/pet_list.html', {
        'pet_list': pet_list,
    })

def item_list(request):
    item_list = Item.objects.order_by('-name')
    return render(request, 'Inventory/item_list.html', {
        'item_list': item_list
    })

def pet_view(request, user_id, pet_name):
    pet = get_object_or_404(Photo_Data, user_id=user_id, pet_name=pet_name)
    return render(request, 'Inventory/pet_view.html', {'pet': pet})