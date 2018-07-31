from django.db import models

# Create your models here.
class userSignupModel(models.Model):
	name=models.CharField(max_length=30)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)


class Profile(models.Model):
   picture = models.ImageField(upload_to = 'pictures')

   class Meta:
      db_table = "Profile"

class UserLoginModel(models.Model):
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)      