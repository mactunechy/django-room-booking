from django.urls import path
from .views import contact,about_view


urlpatterns = [
	path('',contact,name='contact'),
	path('about/',about_view,name='about')

]