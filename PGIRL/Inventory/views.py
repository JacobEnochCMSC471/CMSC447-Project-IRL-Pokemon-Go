from django.http import HttpResponse
from django.shortcuts import render

from .models import Item, Pet

# Create your views here.
def select_list(request):
    return render(request, 'Inventory/select_list.html')

def pet_list(request):
    pet_list = Pet.objects.order_by('-name')
    return render(request, 'Inventory/pet_list.html', {
        'pet_list': pet_list
    })

def item_list(request):
    item_list = Item.objects.order_by('-name')
    return render(request, 'Inventory/item_list.html', {
        'item_list': item_list
    })