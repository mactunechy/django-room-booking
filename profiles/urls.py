from django.urls import path, include
from .views import ProfileDetailView,ProfileUpdateView,ProfileCreateView
urlpatterns = [
    path('',ProfileCreateView.as_view(),name='profile_create'),
    path('update/<pk>/',ProfileUpdateView.as_view(),name='profile_update'),
    path('detail/<pk>/',ProfileDetailView.as_view(),name='profile_detail')
    
]