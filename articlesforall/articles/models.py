from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE







class Author(models.Model):
	name = models.CharField(max_length=40)
	age = models.CharField(max_length=3)
	email = models.EmailField(max_length=50)
	about = models.CharField(max_length=500)
	
	def __str__(self):
		return self.name



class Topic(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name



class Article(models.Model):
	title = models.CharField(max_length=50)
	topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
	body = models.CharField(max_length=400)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-updated', 'created']
		
	def __str__(self):
		return self.title




class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-updated', 'created']

	def __str__(self):
		return self.body[0:30]