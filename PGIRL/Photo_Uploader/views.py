from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import User_Image_Upload_Form
from .models import Photo_Data
from datetime import datetime
# Tutorial: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page


def landing_page(request):

    return render(request, "base_generic.html")


def upload_photo_to_db(request):

    if request.method == 'POST':
        current_date_time = datetime.now()  # Get current date and time for the POST request from user
        form = User_Image_Upload_Form(request.POST, request.FILES, current_date_time)  # Supply info from POST and datetime to create new DB object

        if form.is_valid():
            print("Saved successfully")
            new_photo_object = form.save()  # Get a reference to the newly saved DB object that was just created and saved - add to verify queue
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

