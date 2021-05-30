from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
	name = models.CharField(max_length=255, blank=True)
	pic = models.ImageField(upload_to='path/to/img')
	date_posted = models.DateTimeField(default=timezone.now)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.name


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
 

class Comments(models.Model):
	post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
	username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
	comment = models.CharField(max_length=255)
	comment_date = models.DateTimeField(default=timezone.now)

class Like(models.Model):
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)	


class Contactus(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	subject = models.CharField(max_length=50)
	message = models.TextField()
	
