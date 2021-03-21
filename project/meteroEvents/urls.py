from django.urls import path
from . import views

app_name = 'metroE'
urlpatterns = [
	path('', views.FeedIndexView.as_view(), name="feed_index_view"),
	path('login', views.UserLogRegView.as_view(), name = "user_login_view"),
	#path('medicine/registration', views.RegistrationIndexView.as_view(), name="medicine_registration_view"),
	#path('customer/registration', views.CustomerRegistrationView.as_view(), name= "customer_registration_view"),
	#path('login', views.LandingView.as_view(), name= "landing_view"),
]