from django.shortcuts import render
from django.views.generic import ListView
from rooms.models import Room
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages




class DashboardListView(LoginRequiredMixin,ListView):
	models = Room
	template_name = 'dashboard/dashboard_list.html'
	paginate_by = 10
	def get_queryset(self):
		owner = self.request.user
		owner_rooms = Room.objects.filter(owner=owner)
		return owner_rooms
	
	def get_context_data(self,**kwargs):
		context = super(DashboardListView,self).get_context_data(**kwargs)
		my_rooms = self.get_queryset()
		available = my_rooms.filter(is_available=True).count()
		booked = my_rooms.filter(is_available=False).count()
		context['available'] = available
		context['booked'] = booked
		messages.info(self.request,"Note: please mark all booked rooms as booked by clicking the 'availabe' option on the room card ")
		return context


def mark_as_booked(request,pk):
	room = get_object_or_404(Room,pk=pk)
	if room.is_available :
		room.is_available = False
		room.save()
		messages.info(request,'You have successfully marked room {} as booked!'.format(room.room_id))
	else:
		room.is_available = True
		room.save()
		messages.info(request,'You have successfully marked room {} as available for booking!'.format(room.room_id))

	return redirect('dashboard')