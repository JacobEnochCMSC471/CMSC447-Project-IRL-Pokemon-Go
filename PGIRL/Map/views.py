from django.shortcuts import render

def map(request):
    return render(request, 'Map/map.html')

def shop(request):
    return render(request, 'Map/shop.html')

def training(request):
    return render(request, 'Map/training.html')

def challenges(request):
    return render(request, 'Map/challenges.html')