from django.http.response import Http404
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.contrib import messages

from .forms import  ContactForm
from .models import Razred,Naslov,Predmet
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
import json
# Create your views here.
#https://djangopackages.org/ - all django packages -- captcha,...
#https://docs.microsoft.com/hr-hr/learn/paths/django-create-data-driven-websites/?wt.mc_id=slides-content_13204_webinar_reactor&?WT.mc_id=WebWednesday-c9-niner
def home(request):
	predmeti = Predmet.objects.all()
	form = ContactForm(request.POST or None)
	context = {
		"predmeti":predmeti,
		"form":form
	}

	if form.is_valid():
		email = form.cleaned_data.get("email")
		poruka = form.cleaned_data.get("poruka")
		messages.add_message(request,
							messages.SUCCESS,
							"Your suggestion has been submitted successfully.We will check your message as soon as possible.Thank you!")
		form = ContactForm()
		
		send_mail(
			f"{email} - Matura",
			poruka,
			email,
			[settings.EMAIL_HOST_USER],
			
		)
		
		
		return HttpResponseRedirect(reverse("home"))

	
	return render(request,"main/home.html",context)




