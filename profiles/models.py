from django.db import models
from django.conf import settings 
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
	owner = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile')
	image = models.ImageField(upload_to='profiles/',null=True,blank=True)
	phone = PhoneNumberField(null=True,blank=True)
	address_line1 = models.CharField(max_length=200)
	address_line2 = models.CharField(max_length=200,null=True,blank=True)
		
	
	
	def __str__(self):
		return self._user.username
	
	
	