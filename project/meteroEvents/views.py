from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import loginForm, registerForm
from .models import *

class FeedIndexView(View):

	def get(self, request):
 		events = Events.objects.all()
 		participants = Participants.objects.all()
 		users = Users.object.all()
 		context = {
 			'events': events,
 			'participants': participants,
 			'users': users	
 		}
 		return render(request,'feed.html', context )
	



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
 				#users =Users.objects.filter(firstName = 'Yanni').delete()
 			if a == True:
 				return render(request,'feed.html')
 			else:
 				return HttpResponse('Not Valid')
 			#form.save()

 			#return render(request,'login.html')
 		#else:
 			#print(form.errors)
 			#return HttpResponse('Not Valid')
	

			#return HttpResponse('Medicine Record Saved!')			
			#return render(request,'index.html')
			
			# except:
			# 	raise Http404
	
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

 			a = bool(Users.objects.filter(username = usern, pword = pword, firstName = fname, lastName = lname, mobileNum = mn,
						country = country, province = pro, city = city, street = st))
 				
 			if(a == True):
 				return HttpResponse('Account already exist')
 			else:
 				form = Users(username = usern, pword = pword, firstName = fname, lastName = lname, mobileNum = mn,
						country = country, province = pro, city = city, street = st)
 				form.save()
 				return redirect('meteroEvents:login')
 				
 		
 		else:
 			print(form.errors)
 			return HttpResponse('Not Valid')

class feed(View):
	def get(self, request):
		return render(request,'feed.html')