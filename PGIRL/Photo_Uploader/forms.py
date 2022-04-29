from django import forms
from .models import Photo_Data


class User_Image_Upload_Form(forms.ModelForm):  # This creates a form the /image_upload url will use to gather user-input
    class Meta:
        model = Photo_Data
        exclude = ['date_added', 'verified_status', 'stat_hp', 'stat_attack', 'stat_defense', 'stat_speed', 'passes', 'strikes']
        # Include fields for image, user_id, user_label and pet_name only
