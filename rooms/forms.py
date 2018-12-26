from django import forms
from .models import Room 
from PIL import Image
from django.core.files import File


#form for adding a new room
class RoomForm(forms.ModelForm):
	
	class Meta:
		model = 		Room
		help_texts = {
			'description':'separate each description with a comma',
			'furniture':'separate each property by a comma',
			'price':'price per month'
		}
		fields = 		['description','furniture','price', 'is_available', 'address_line1','address_line2','town']
		def __init__(self, *args, **kwargs):
			super(ItemForm, self).__init__(*args, **kwargs)
			for field in self.fields:
				help_text = self.fields[field].help_text
				self.fields[field].help_text = None
				if help_text != '':
					self.fields[field].widget.attrs.update({'class':'has-popover', 'data-content':help_text, 'data-placement':'right', 'data-container':'body'})


		
#Form for sending an email
class EmailForm(forms.Form):
	full_name =   forms.CharField(max_length=200)
	email = 				forms.EmailField()
	message = 		  forms.CharField(max_length=1000)#to bec changed to textField
	phone =        forms.CharField(max_length=10)
	class Meta:
		help_texts = {
			"phone":"prefix with a +XXX area code"
		}
	