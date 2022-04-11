from django import forms
from .models import Photo_Data


class User_Image_Upload_Form(forms.ModelForm):
    class Meta:
        model = Photo_Data
        exclude = ['date_added', 'verified_status', 'stat_hp', 'stat_attack', 'stat_defense', 'stat_speed']
        # Include all fields except stats and verified status (done later)
