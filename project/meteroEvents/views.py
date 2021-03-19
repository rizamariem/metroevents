from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
#from .forms import UserForm
from .models import *
# Create your views here.
class FeedIndexView(View):
	def get(self, request):
		return render(request, 'wanto.html')