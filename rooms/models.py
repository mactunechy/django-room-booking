from django.db import models
from django.conf import settings




#model design of the room object
 
class Room(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='rooms')
  #to be created auto during the preSave signal
	room_id = models.CharField(max_length=500, unique=True)
	description = 		models.CharField(max_length=155,null=True,blank=True)#separate by comma
	price = 					models.DecimalField(max_digits=1000000,decimal_places=2)
	furniture = 			models.CharField(max_length=155,null=True,blank=True) #separate by comma
	address_line1 =  models.CharField(max_length=50)
	address_line2 =  models.CharField(max_length=50,null=True,blank=True)
	town					 =  models.CharField(max_length=255)
	is_available =   models.BooleanField(default=False)
	likes        =   models.IntegerField(default=0)
	views        =		 models.IntegerField(default=0)
	published_date = models.DateTimeField(auto_now=True)	
	
	def like(self):
		self.likes += 1 
		self.save()
		
	
		
	
		
	def unlike(self):
		likes = self.likes	
		float_likes = float(likes)
		float_likes = float_likes-1
		self.likes = float_likes
		self.save()
		
		
	def add_view(self):
		self.views +=1
		self.save() 

	def __str__(self):
		return self.room_id
		

	#Model for Photos
class Photo(models.Model):
	room 					=models.ForeignKey(Room,related_name='photos',on_delete=models.CASCADE)
	file = models.ImageField()
	description = models.CharField(max_length=255, blank=True)
	uploaded_at = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name = 'photo'
		verbose_name_plural = 'photos'	




			