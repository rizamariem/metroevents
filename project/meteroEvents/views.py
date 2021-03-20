from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import UserForm
from .models import *

class FeedIndexView(View):
	def get(self, request):
		return render(request, 'wanto.html')

	def post(self, request):		
		form = UserForm(request.POST, request.FILES)		
	
		if form.is_valid():
			usern = request.POST.get("username")
			pword = request.POST.get("pword")
			fname = request.POST.get("firstName")
			lname = request.POST.get("lastName")
			email = request.POST.get("email")
			mn = request.POST.get("mobileNum")
			country = request.POST.get("country")
			pro = request.POST.get("province")
			city = request.POST.get("city")
			st = request.POST.get("street")


			form = Users( username = usern, pword = pword, firstName = fname, lastName = lname, email = email, mobileNum = mn,
						country = country, province = pro, city = city, street = st)

			form.save()

			#return HttpResponse('Medicine Record Saved!')			
			#return render(request,'index.html')
			return render(request,'wanto.html')
			# except:
			# 	raise Http404
		else:
			print(form.errors)
			return HttpResponse('Not Valid')