from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import loginForm, registerForm, regEventForm
from .models import *
from django.db import connection


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
				organizers = Organizers.objects.all()
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



class registerEvent(View):
	def get(self, request):
		organizers = Organizers.objects.all()
		context ={
			'organizers': organizers,
		}
		return render(request, 'wanto.html',context)

	def post(self, request):
		organizer = Organizers.objects.all()
		
		
		
		
		form = regEventForm(request.POST, request.FILES)

		if form.is_valid():
			c = connection.cursor()
			org_id = request.POST.get("org_id")
			pword = request.POST.get("type")
			fname = request.POST.get("name")
			lname = request.POST.get("venue")
			mn = request.POST.get("start")
			gender = request.POST.get("end")
			im_3 = request.FILES['image']
			#pro = request.POST.get("mobileNum")
			city = request.POST.get("description")
			st = request.POST.get("target")
			org = Organizers.objects.get(id = org_id)
			 
			form = Events( organizer_id = org , event_type = pword, event_name = fname, 
				venue = lname, date_start = mn,date_end= gender, image = im_3,
				description = city, targetLocation = st)
			form.save()
			#c.execute("INSERT INTO organizers(organizer_id, event_type, event_name, venue, date_start, date_end,image,description, targetLocation ) VALUES(  %d , %s, %s, %s, %s, %s, %s, %s, %s )", [org_id, pword,fname,lname,mn,gender,im_3,city,st] )
			#c.commit()
			#form.save()
			return HttpResponse( 'oten',org)
		else:
			return HttpResponse(' not Valid')


class organizerFeed(View):
	def get(self, request):
		return render(request,'organizerfeed.html')