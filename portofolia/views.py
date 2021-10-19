
# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.core.mail import message, send_mail
from django.conf import settings

########################################################################## EMAIL FOR

def home(request):
	return render(request, 'site/sayt.html')



def contact(request):
	if request.method != "POST":
		return render(request, '/site/site.html')
	message_name = request.POST['message-name']
	message_email = request.POST['message-email']
	message = request.POST['message']


	send_mail(
		message_name, #subject
		message, #message
		message_email, #'from eamil'
		['tarjimatv1@gmail.com'], # to email
	)
	return render(request, 'site/site.html',{'message_name':message_name})