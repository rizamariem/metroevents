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
		if request.method == 'POST':
			if 'btnLogin' in request.POST:
				form = loginForm(request.POST, request.FILES)
				if form.is_valid():
					usern = request.POST.get("username")
					password = request.POST.get("password")
					a = bool(Users.objects.filter(username = usern, pword = password))
					user_info = Users.objects.filter(username = usern, pword = password)
					if (a == True):
						for b in Users.objects.filter(username = usern, pword = password):
							if b.role == 1:
								users = Users.objects.all()
								organizers = Organizers.objects.all()
								participants = Participants.objects.all()
								events = Events.objects.all()
								reviews = Reviews.objects.all()
								context = {
								'events': events,
								'participants': participants,
								'users': users,
								'user_info': user_info,
								'organizers': organizers,
								'reviews': reviews
								}
								return render(request, 'feed.html', context)
							elif b.role == 3:
								users = Users.objects.all()
								organizers = Organizers.objects.all()
								participants = Participants.objects.all()
								events = Events.objects.all()
								reviews = Reviews.objects.all()
								requests = Requests.objects.all()
								context = {
								'events': events,
								'participants': participants,
								'users': users,
								'user_info': user_info,
								'organizers': organizers,
								'reviews': reviews,
								'requests' : requests,
								}
								return render(request, 'organizerfeed.html', context)
							
					else:
						return HttpResponse('invalid input')
				else:
					return HttpResponse('please enter fields')

			elif 'btnUpvote' in request.POST:
				form = loginForm(request.POST, request.FILES)
				e_id = request.POST.get("eventid")
				uv = request.POST.get("upvote")
				upvote = Events.objects.values_list('upvote', flat=True).filter(id =e_id)
				event = Events.objects.filter(id = e_id).update(upvote = uv)
				return HttpResponse('upvoted')


			elif 'btnPublish' in request.POST:
				form = loginForm(request.POST, request.FILES)
				review = request.POST.get("review")
				e_id = request.POST.get("eventid")
				u_id = request.POST.get("userid")
				event = Events.objects.get(id = e_id)
				user = Users.objects.get(id = u_id)
				form = Reviews(event_id = event, review = review, user_id = user)
				form.save()
				return HttpResponse('Review published')

			elif 'btnJoin' in request.POST:
				form = loginForm(request.POST, request.FILES)
				e_id = request.POST.get("eventid")
				u_id = request.POST.get("userid")
				event = Events.objects.get(id = e_id)
				user = Users.objects.get(id = u_id)
				form = Requests(event = event, req_type = 1, user = user)
				form.save()
				return HttpResponse('Request to join sent')

			elif 'btnCancel' in request.POST:
				form = loginForm(request.POST, request.FILES)
				e_id = request.POST.get("eventid")
				u_id = request.POST.get("userid")
				event = Events.objects.get(id = e_id)
				user = Users.objects.get(id = u_id)
				cancel = Requests.objects.filter(user = user, event = event).delete()
				return HttpResponse('Request cancelled')

			elif 'btnReqOrg' in request.POST:
				form = loginForm(request.POST, request.FILES)
				u_id = request.POST.get("userid")
				user = Users.objects.get(id = u_id)
				a = bool(Requests.objects.filter(user = u_id, req_role = 1, response = 2))
				if a == False:
					form = Requests(req_type = 1, user = user, req_role = 1)
					form.save()
					return HttpResponse('Request for becoming organizer sent')
				else:
					return HttpResponse('Request already sent, please send again after 24 hours')

			elif 'btnReqAdmin' in request.POST:
				form = loginForm(request.POST, request.FILES)
				u_id = request.POST.get("userid")
				user = Users.objects.get(id = u_id)
				a = bool(Requests.objects.filter(user = u_id, req_role = 2, response = 2))
				if a == False:
					form = Requests(req_type = 1, user = user, req_role = 2)
					form.save()
					return HttpResponse('Request for becoming administrator sent')
				else:
					return HttpResponse('Request already sent, please send again after 24 hours')
			
			elif 'btnAcceptRole' in request.POST:
				form = loginForm(request.POST, request.FILES)
				req_id = request.POST.get("requestid")
				user = request.POST.get("userid")
				r = Requests.objects.get(id = req_id)
				u = Users.objects.get(id = user)
				req = Requests.objects.filter(id = req_id).delete()
				if r.req_role == 1:
					form = Organizers(user_id = u)
					form.save
					u = Users.objects.filter(id = user).update(role = 2)
				else:
					form = Administrator(user = u)
					form.save
					u = Users.objects.filter(id = user).update(role = 3)

				return HttpResponse('Promotion approved')

			elif 'btnDeclineRole' in request.POST:
				form = loginForm(request.POST, request.FILES)
				req_id = request.POST.get("requestid")
				user = request.POST.get("userid")
				r = Requests.objects.filter(id = req_id).update(response = 0)
				return HttpResponse('Promotion declined')

			elif 'btnAcceptEvent' in request.POST:
				form = loginForm(request.POST, request.FILES)
				req_id = request.POST.get("requestid")
				user = request.POST.get("userid")
				req = Requests.objects.filter(id = req_id).update(response = 1)
				return HttpResponse('Event approved')

			elif 'btnDeclineEvent' in request.POST:
				form = loginForm(request.POST, request.FILES)
				req_id = request.POST.get("requestid")
				user = request.POST.get("userid")
				req = Requests.objects.filter(id = req_id).update(response = 1)
				return HttpResponse('Event declined')

			elif 'btnAddEvent' in request.POST:
				form = loginForm(request.POST, request.FILES)
				if form.is_valid():
					org = request.POST.get("org_id")
					name = request.POST.get("name")
					etype = request.POST.get("type")
					venue = request.POST.get("venue")
					startdate = request.POST.get("startdate")
					enddate = request.POST.get("enddate")
					description = request.POST.get("description")
					image = request.FILES["image"]

					event = Events.objects.get(id = e_id)
					user = Users.objects.get(id = u_id)
					form = Events( organizer_id = org , etype = pword, name = fname, 
					venue = lname, date_start = mn,date_end= gender, image = im_3,
					description = city, targetLocation = st)
					form.save()
		




				
	
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
			 
			form = Events( organizer_id = org , etype = pword, name = fname, 
				venue = lname, date_start = mn,date_end= gender, image = im_3,
				description = city, targetLocation = st)
			form.save()
			#c.execute("INSERT INTO organizers(organizer_id, event_type, event_name, venue, date_start, date_end,image,description, targetLocation ) VALUES(  %d , %s, %s, %s, %s, %s, %s, %s, %s )", [org_id, pword,fname,lname,mn,gender,im_3,city,st] )
			#c.commit()
			#form.save()
			return HttpResponse( 'register successful')
		else:
			return HttpResponse(' not Valid')


class adminFeed(View):
	def get(self, request):
		return render(request,'admin.html')