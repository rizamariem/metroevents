from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import loginForm, registerForm
from .models import *


class login(View):
	def get(self,request):
		events = Events.objects.all()
		participants = Participants.objects.all()
		return render(request,'login.html')

	def post(self, request):
		form = loginForm(request.POST, request.FILES)
		if form.is_valid():
			usern = request.POST.get("username")
			password = request.POST.get("password")
			a = bool(Users.objects.filter(username = usern, pword = password))
			user_info = Users.objects.filter(username = usern, pword = password)

			if (a == True):
				users = Users.objects.all()
				organizers = Organizer.objects.all()
				participants = Participants.objects.all()
				events = Events.objects.all()
				context = {
				'events': events,
				'participants': participants,
				'users': users,
				'user_info': user_info,
				'organizers': organizers
				}

				return render(request, 'feed.html', context)
			else:
	 			return HttpResponse('Not Valid')
	

			
	
class register(View):
	def get(self, request):
		return render(request,'register.html')

	def post(self, request):
 		form = registerForm(request.POST, request.FILES)
 		if form.is_valid():
 			usern = request.POST.get("username")
 			pword = request.POST.get("password")
 			fname = request.POST.get("firstname")
 			print(fname)
 			lname = request.POST.get("lastname")
 			mn = request.POST.get("number")
 			gender = request.POST.get("gender")
 			country = request.POST.get("country")
 			pro = request.POST.get("province")
 			city = request.POST.get("city")
 			st = request.POST.get("street")

 			a = bool(Users.objects.filter(username = usern, pword = pword, firstname = fname, lastname = lname, mobile = mn,
						country = country, province = pro, city = city, street = st))
 				
 			if(a == True):
 				return HttpResponse('Account already exist')
 			else:
 				form = Users(username = usern, pword = pword, firstname = fname, lastname = lname, mobile = mn,
						country = country, province = pro, city = city, street = st)
 				form.save()
 				return redirect('meteroEvents:feed')
 				
 		
 		else:
 			print(form.errors)
 			return HttpResponse('Not Valid')

