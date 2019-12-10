from django.forms import ModelForm

from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField
# Next two lines are only used for generating the upload preset sample name
# from cloudinary.compat import to_bytes
# import cloudinary, hashlib

from .models import Photo

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

class PhotoDirectForm(PhotoForm):
    image = CloudinaryJsFileField(
        attrs = { 'style': "margin-top: 30px" }, 
        options = { 
          'tags': "Henri",
          'crop': 'limit', 'width': 500, 'height': 500},
          'eager': [{ 'crop': 'fit', 'width': 500, 'height': 500 }]
        })

class PhotoUnsignedDirectForm(PhotoForm):
    upload_preset_name = "sample_eaeb23440f"
    image = CloudinaryUnsignedJsFileField(upload_preset_name)
