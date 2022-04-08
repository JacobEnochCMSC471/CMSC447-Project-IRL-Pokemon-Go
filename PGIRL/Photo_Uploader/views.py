from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import User_Image_Upload_Form


def index(request):
    return HttpResponse("You look nice today")


def upload_photo_to_db(request):
    if request.method == 'POST':
        form = User_Image_Upload_Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('Success!')
    else:
        form = User_Image_Upload_Form()
        return render(request, 'User_Image_Upload_Form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def upload_photo_to_iNaturalist(request, user_id):
    return HttpResponse("Not implemented Yet")
