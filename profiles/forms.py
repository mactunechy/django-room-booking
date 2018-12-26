from django import forms
from .models import Profile
from django.core.files import File
from PIL import Image
from django.shortcuts import reverse

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = [ 'image','phone','address_line1','address_line2']
		help_texts ={
			"phone": "prefix with a +XXX area code"
		}
	
	def save(self):
		profile  = super(ProfileForm,self).save()
		
		image = Image.open(profile.image)
		resized_image = image.resize((200,200),Image.ANTIALIAS)
		resized_image.save(profile.image.path)
		
		return profile