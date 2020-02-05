from django.db import models
from django.contrib.auth.models import User
		

class PostManager(models.Manager):
	def like_or_unlike(self,user,obj):
		if user in obj.like.all():
			is_liked=False
			obj.like.remove(user)
		else:
			is_liked=True
			obj.like.add(user)

		return is_liked



class Post(models.Model):
	user=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
	content=models.TextField()
	like=models.ManyToManyField(User,related_name='liked',blank=True)
	created_on=models.DateTimeField(auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True)

	objects=PostManager()

	def __str__(self):
		return self.content[:30]

	