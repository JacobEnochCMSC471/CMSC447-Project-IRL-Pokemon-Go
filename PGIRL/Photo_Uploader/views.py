from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import User_Image_Upload_Form
from .models import Photo_Data
from datetime import datetime
import os
import shutil


# Tutorial: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page

def remove_bad_photos(threshold):
    bad_photos = Photo_Data.objects.filter(strikes__gte=threshold)  # Get all photo objects with more than threshold strikes

    if bad_photos:  # If the query object exists, delete all photos from the database that exceed the threshold
        root_directory = 'media/'
        photo_list = []

        for photo in bad_photos.iterator():  # Get all image paths stored in the images
            photo_path = root_directory + str(photo.image)  # Append the root directory onto the photos
            photo_list.append(photo_path)

        bad_photos.delete()  # Delete all Photo_Data entries that go past the threshold

        for photo_path in photo_list:
            if os.path.exists(photo_path):  # Remove the photo from the media/uploads directory
                print("Removing photo from directory...")
                os.remove(photo_path)  # Call OS to remove this specific file
                print("Photo Removed")

        return 1

    else:
        return 0


def landing_page(request):
    return render(request, "landing_page.html")


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
    return render(request, 'success_image_upload.html')


def error(request):
    return render(request, 'error_image_upload.html')
