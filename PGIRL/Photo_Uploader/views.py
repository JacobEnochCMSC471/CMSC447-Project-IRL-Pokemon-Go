from django.shortcuts import render
from django.http import HttpResponse, Http404


def index(request):
    return HttpResponse("You look nice today")


def upload_photo_to_db(request, user_id):
    return HttpResponse("Not implemented Yet")


def upload_photo_to_iNaturalist(request, user_id):
    return HttpResponse("Not implemented Yet")
