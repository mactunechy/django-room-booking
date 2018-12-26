from rooms.forms import EmailForm
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def contact(request):
	if request.method == 'POST':
		
		email_form = EmailForm(request.POST)
		if email_form.is_valid:
			fullname = request.POST.get('full_name')
			message = request.POST.get('message')
			reply_email = request.POST.get('email')  #to be saved into database for marketing
			phone = request.POST.get('phone').strip()
			print(phone) #to be saved in database
			from_email = reply_email
			context= {
				'fullname':fullname,
				'message':message,
				'reply_email':reply_email,
				'phone':phone
			}
			msg_html = render_to_string('rooms/email.html',context)
			subject = "You're recieving this message from a user on HomeFineDer"
			
			admin_email = settings.EMAIL_HOST_USER
			email = EmailMessage(subject,msg_html,to=[admin_email])
			email.content_subtype = 'html'
				
			try:
				email.send()
				messages.success(request,'Email sent Successfully')
				return redirect('contact')
			except :
				messages.warning(request,'Failed to send Email, Try again later')
				return  redirect('contact')
	else:
		form = EmailForm()
		context = {
			"form":form
		}			
		return render(request,'landing/contact.html',context)		
		
def about_view(request):
	template_name = 'landing/about.html'
	admin = UserModel.objects.filter(is_superuser=True).first()
	context = {
		'admin':admin
	}
	return render(request,template_name,context)		
						