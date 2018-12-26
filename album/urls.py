from .views import photo_list,photo_delete
from django.urls import path


urlpatterns = [
    path('<pk>/', photo_list, name='photo_list')
]   