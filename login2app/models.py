from django.db import models

class UserInfo(models.Model):
	username = models.CharField(max_length=40)
	phoneNum = models.CharField(max_length=11)
	password = models.CharField(max_length=40)