from django.db import models
from rooms.models import Room



class Photo(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name='images',null=True,blank=True)
    file = models.ImageField(upload_to='rooms/')
    description = models.CharField(max_length=155, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'photo'
    
        verbose_name_plural = 'photos'
        
        
        
        