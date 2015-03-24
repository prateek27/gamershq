from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank = True)
	picture = models.ImageField(upload_to = 'profile_images',blank=True)

	def __str__(self):
		return self.user.username

