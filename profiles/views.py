from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,UpdateView,DetailView,ListView
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from rooms.models import Room
from django.urls import reverse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
UserModel = get_user_model()



# Create your views here.
class ProfileCreateView(LoginRequiredMixin,CreateView):
	model = Profile
	form_class = ProfileForm
	template_name = 'profiles/profile_form.html'
	
	def form_valid(self,form):
		new_profile = form.save()
		user = self.request.user
		new_profile._user = user
		new_profile.save()
		return redirect('dashboard')
		
		
		
class ProfileUpdateView(LoginRequiredMixin,UpdateView):
	model = Profile
	form_class = ProfileForm
	template_name = 'profiles/profile_form.html'
	
	def get_success_url(self):
		pk = self.kwargs.get('pk')
		return reverse('profile_update',kwargs={'pk':pk})
	
		
		
		
class ProfileDetailView(DetailView):
	model = UserModel
	template_name = 'profiles/profile_detail.html'
	
		
	def get_context_data(self,**kwargs):
			context = super(ProfileDetailView,self).get_context_data(**kwargs)
			room_list = Room.objects.filter(owner=self.get_queryset().first())
			available = room_list.filter(is_available=True).count()
			booked = room_list.filter(is_available=False).count()
			context['available'] = available
			context['booked'] = booked
			page = self.request.GET.get('page', 1)
			paginator = Paginator(room_list, 10)
			try:
				rooms = paginator.page(page)
			except PageNotAnInteger:
				rooms = paginator.page(1)
			except EmptyPage:
				rooms = paginator.page(paginator.num_pages)
			context['rooms'] = rooms
			return context			
	





		
		