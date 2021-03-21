from django.urls import path
from . import views

app_name = 'metroE'
urlpatterns = [
	path('', views.FeedIndexView.as_view(), name="feed_index_view"),
	path('login', views.login.as_view(), name = "login"),
	path('register', views.register.as_view(), name = "register"),
	#path('medicine/registration', views.RegistrationIndexView.as_view(), name="medicine_registration_view"),
	#path('customer/registration', views.CustomerRegistrationView.as_view(), name= "customer_registration_view"),
	#path('login', views.LandingView.as_view(), name= "landing_view"),
]