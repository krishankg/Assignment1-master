from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display=['content','created_on','get_like','get_created']

	def get_like(self,obj):
		like=list()
		for element in obj.like.all():
			like.append(element)

		return like


	def get_created(self,obj):
		return obj.user.username




admin.site.register(Post,PostAdmin)

