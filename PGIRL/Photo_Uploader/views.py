from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import User_Image_Upload_Form
from .models import Photo_Data
from datetime import datetime


def landing_page(request):
    return HttpResponse("This is the landing page")


def upload_photo_to_db(request):

    if request.method == 'POST':
        current_date_time = datetime.now()
        form = User_Image_Upload_Form(request.POST, request.FILES, current_date_time)

        if form.is_valid():
            print("Saved successfully")
            form.save()
            return redirect('success')

        else:
            return redirect('error')
    else:
        form = User_Image_Upload_Form()
        return render(request, 'User_Image_Upload_Form.html', {'form': form})


def success(request):  # Redirect page for when an image is successfully uploaded
    return HttpResponse('Image successfully uploaded!')


def error(request):
    return HttpResponse('Something went wrong!')

