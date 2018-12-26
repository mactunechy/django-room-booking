from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import DetailView,ListView,CreateView,DeleteView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Room
from .forms import RoomForm, EmailForm
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from .helpers import random_apha_numeric
from django.contrib import messages
from .filters import RoomFilter
from django_filters.views import FilterView
from django.conf import settings
from django.template.loader import render_to_string
UserModel = get_user_model()

#list view for of the rooms
class RoomListView(ListView):
	model = Room
	template_name = 'rooms/roomList.html'
	paginate_by = 10
	queryset = Room.objects.all().order_by('price')
	
	
#detail view of each rooms

class RoomDetailView(DetailView):
	model = Room
	template_name = 'rooms/room_detail.html'
	def post(self,*args,**kwargs):
		email_form = EmailForm(self.request.POST)
		if email_form.is_valid:
			fullname = self.request.POST.get('full_name')
			message = self.request.POST.get('message')
			reply_email = self.request.POST.get('email')  #to be saved into database for marketing
			phone = self.request.POST.get('phone').strip()
			print(phone) #to be saved in database
			from_email = settings.EMAIL_HOST_USER
			context= {
				'fullname':fullname,
				'message':message,
				'reply_email':reply_email,
				'phone':phone
			}
			msg_html = render_to_string('rooms/email.html',context)
			subject = "You're recieving this message from a client on HomeFineDer"
			
			pk = self.kwargs.get('pk')
			room =  get_object_or_404(Room,pk=pk)
			
			owner_email = room.owner.email
			print(owner_email)
			try:
				email = EmailMessage(subject,msg_html,to=[owner_email])
				email.content_subtype = 'html'
				email.send()
				messages.success(self.request,'Email sent Successfully')
				return redirect('room_detail',pk)
			except :
				messages.warning(self.request,'Failed to send Email, Try again later')
				return  redirect('room_detail',pk)
				
	def get_object(self,*args,**kwargs):
		object = super(RoomDetailView,self).get_object(*args,**kwargs)
		pk = kwargs.get('pk')
		have_viewed = self.request.session.get('viewed-{}'.format(pk),False)
		if not have_viewed:
			object.add_view()
			self.request.session['viewed-{}'.format(pk)] = True
		return object	

		
	
		
	def get_context_data(self,*args,**kwargs):
		context = super(RoomDetailView,self).get_context_data(*args,**kwargs)
		
		context['furniture'] = context['object'].furniture.split(',')
		context['email_form'] = EmailForm()
		return context




#Form View for entering a New room
class RoomFormView(LoginRequiredMixin,CreateView):
	model = Room
	form_class = RoomForm
	template_name = 'rooms/room_form.html'
	
	def form_valid(self,form):
		new_room = form.save(commit=False)
		new_room.owner = self.request.user
		new_room.room_id = random_apha_numeric()
		new_room.save()
		messages.info(self.request,'Room added Successfully,add room images')
		return redirect('photo_list',new_room.pk)	
	
class RoomUpdateView(UpdateView,LoginRequiredMixin):
	model = Room
	form_class = RoomForm
	template_name_suffix = '_update_form'
	
	
class RoomDeleteView(LoginRequiredMixin,DeleteView):
	template_name="rooms/room_confirm_delete.html"
	model = Room
	success_url = reverse_lazy('room_list')#to be changed to Dashboard		



class RoomSearchView(FilterView):
	filterset_class = RoomFilter
	template_name = 'rooms/room_search.html'



#liking a room
def room_liking(request,pk):
	have_liked = request.session.get('liked-{}'.format(pk),False)
	room = get_object_or_404(Room,pk=pk)
	if not have_liked:
		room.like()
		request.session['liked-{}'.format(pk)] = True
	else:
		room.unlike()
		del request.session['liked-{}'.format(pk)]
		
	return redirect('room_list')		

 