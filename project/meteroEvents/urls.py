from django.urls import path
from . import views

app_name = 'meteroEvents'
urlpatterns = [
	#path('feed', views.FeedIndexView.as_view(), name="feed_index_view"),
	path('feed', views.login.as_view(), name = "feed"),
	path('register', views.register.as_view(), name = "register"),
	#path('feed', views.FeedIndexView.as_view(), name="feed"),
	#path('feed', views.feed.as_view(), name = "feed"),
	#path('medicine/registration', views.RegistrationIndexView.as_view(), name="medicine_registration_view"),
	#path('customer/registration', views.CustomerRegistrationView.as_view(), name= "customer_registration_view"),
	#path('login', views.LandingView.as_view(), name= "landing_view"),
]