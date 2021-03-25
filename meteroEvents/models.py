from django.db import models
from datetime import datetime
#from django.utils import timezone


class Users(models.Model):
	username = models.CharField(max_length = 50)
	pword = models.CharField(max_length = 50, null = True)
	firstname = models.CharField(max_length = 50, null = True)
	lastname = models.CharField(max_length = 50, null = True)
	gender = models.CharField(max_length = 5, default = 'Male')
	mobile = models.DecimalField(max_digits= 15, decimal_places = 0, null = True)
	country = models.CharField(max_length = 50)
	province = models.CharField(max_length = 50)
	city = models.CharField(max_length = 50)
	street = models.CharField(max_length = 50)
	role = models.IntegerField( default = 1)
	date_registered = models.DateField(auto_now=True)
	class Meta:
		db_table = "Users"


class Administrator(models.Model):
	user = models.ForeignKey('Users', on_delete=models.CASCADE, null = True)
	registered_date = models.DateField(auto_now=True)
	
	class Meta:
		db_table = "Administrator"

class Events(models.Model):	
	organizer_id = models.ForeignKey('Organizers', on_delete=models.CASCADE, default =111)
	etype = models.CharField(max_length = 45, null = False)
	name = models.CharField(max_length = 50)
	venue = models.CharField(max_length = 100)
	upvote = models.IntegerField(default = 0)
	date_start = models.DateField(auto_now=True)
	date_end = models.DateField(auto_now=True)
	image = models.FileField(upload_to ='media', default= 'default.jpg', blank = True, null = True)
	video = models.FileField(upload_to ='media', default= 'default.jpg', blank = True, null = True)
	isApproved = models.IntegerField(default = 0)
	cancellationDate = models.DateField(auto_now=False, null = True)
	description = models.CharField(max_length = 100, null = True)
	targetLocation = models.CharField(max_length = 20,null = True)

	class Meta:
		db_table = "Events"

class Notification(models.Model):
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	organizer_id = models.ForeignKey('Organizers', on_delete=models.CASCADE)
	admin_id = models.ForeignKey('Administrator', on_delete=models.CASCADE)
	notification = models.CharField(max_length = 100)
	notif_type = models.IntegerField()

	class Meta:
		db_table = "Notification"

class Organizers(models.Model):
	user_id	 = models.ForeignKey('Users', on_delete=models.CASCADE)
	registered_date = models.DateField(auto_now=True)

	class Meta:
		db_table = "Organizers"

class Participants(models.Model):
	event_id = models.ForeignKey('Events', on_delete=models.CASCADE)
	participant_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	registered_date = models.DateField(auto_now=True)

	class Meta:
		db_table = "Participants"

class Requests(models.Model):
	
	user = models.ForeignKey('Users', on_delete=models.CASCADE)
	event = models.ForeignKey('Events',on_delete=models.CASCADE, null = True)
	req_type = models.IntegerField()
	req_role = models.IntegerField(default = 0)
	description = models.CharField(max_length = 100, null = True)
	req_date = models.DateField(auto_now=True)
	response = models.IntegerField(default = 2)

	class Meta:
		db_table = "Requests"


class Reviews(models.Model):
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	event_id = models.ForeignKey('Events', on_delete=models.CASCADE)
	review = models.CharField(max_length = 100)

	class Meta:
		db_table = "Reviews"



