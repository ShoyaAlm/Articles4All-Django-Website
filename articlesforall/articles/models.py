from django.db import models

from django.contrib.auth.models import User

class Author(models.Model):
	name = models.CharField(max_length=40)
	age = models.CharField(max_length=3)
	email = models.EmailField(max_length=50)
	about = models.CharField(max_length=500)
	def __str__(self):
		return self.name



class Article(models.Model):
	title = models.CharField(max_length=50)
	body = models.CharField(max_length=400)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
