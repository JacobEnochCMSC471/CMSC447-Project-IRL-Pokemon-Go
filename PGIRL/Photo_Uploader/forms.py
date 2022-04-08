from django import forms
from .models import *


class User_Image_Upload_Form(forms.ModelForm):
    class Meta:
        model = Photo_Data
        fields = ['user_id', 'image']