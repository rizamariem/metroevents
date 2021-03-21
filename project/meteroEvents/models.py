from django.db import models
from datetime import datetime
#from django.utils import timezone


# Create your models here.
class Administrator(models.Model):
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	admin_id = models.IntegerField()

	class Meta:
		db_table = "Administrator"

class Events(models.Model):	
	organizer_id = models.ForeignKey('Organizers', on_delete=models.CASCADE)
	event_id = models.IntegerField()
	event_type = models.CharField(max_length = 45, null = False)
	event_name = models.CharField(max_length = 50)
	venue = models.CharField(max_length = 100)
	upvote = models.IntegerField()
	date_start = models.DateField(auto_now=True)
	date_end = models.DateField(auto_now=True)
	image = models.FileField(null=True)
	video = models.FileField(null=True)
	cancellation = models.BinaryField()
	cancellationDate = models.DateField(auto_now=True)
	description = models.CharField(max_length = 100)
	targetLocation = models.CharField(max_length = 20)

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
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	registered_date = models.DateField(auto_now=True)

	class Meta:
		db_table = "Organizers"

class Participants(models.Model):
	event_id = models.ForeignKey('Events', on_delete=models.CASCADE)
	participant_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	#participants_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	registered_date = models.DateField(auto_now=True)

	class Meta:
		db_table = "Participants"

class Requests(models.Model):
	
	user = models.ForeignKey('Users', on_delete=models.CASCADE)
	req_type = models.IntegerField()
	role = models.IntegerField(default = 0)
	description = models.CharField(max_length = 100)
	req_date = models.DateField(auto_now=True)

	class Meta:
		db_table = "Requests"

class Requesttoadmin(models.Model):
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	req_time = models.TimeField(auto_now=False, auto_now_add=False)
	description = models.CharField(max_length = 100)

	class Meta:
		db_table = "Requesttoadmin"

class Requesttoorg(models.Model):
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	req_time = models.TimeField(auto_now=False, auto_now_add=False)
	description = models.CharField(max_length = 100)

	class Meta:
		db_table = "Requesttoorg"

class Requesttopart(models.Model):
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	req_time = models.TimeField(auto_now=False, auto_now_add=False)
	description = models.CharField(max_length = 100)

	class Meta:
		db_table = "Requesttopart"

class Reviews(models.Model):
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
	event_id = models.ForeignKey('Events', on_delete=models.CASCADE)
	review = models.CharField(max_length = 100)

	class Meta:
		db_table = "Reviews"

class Users(models.Model):
	username = models.CharField(max_length = 50)
	pword = models.CharField(max_length = 50)
	firstName = models.CharField(max_length = 50)
	lastName = models.CharField(max_length = 50)
	gender = models.CharField(max_length = 5, default = 'Male')
	mobileNum = models.DecimalField(max_digits= 15, decimal_places = 0)
	country = models.CharField(max_length = 50)
	province = models.CharField(max_length = 50)
	city = models.CharField(max_length = 50)
	street = models.CharField(max_length = 50)
	role = models.IntegerField( default = 1)

	class Meta:
		db_table = "Users"


