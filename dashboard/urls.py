from django.urls import path
from .views import DashboardListView, mark_as_booked

urlpatterns = [
	path('',DashboardListView.as_view(),name='dashboard'),
	path('booked/<pk>/',mark_as_booked,name='booked')


]