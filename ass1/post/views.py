from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
	http_method_names = ['get','post']
	model=Post
	context_object_name='objects'
	template_name='post/list.html'
	ordering = ['-created_on']

	def get_context_data(self,*args,**kwargs):
		context=super(PostListView,self).get_context_data(*args,**kwargs)
		context['form']=PostForm
		return context

	def post(self,*args,**kwargs):
		form=PostForm(self.request.POST,None)
		if form.is_valid():
			if self.request.user.is_authenticated:
				user=self.request.user
				content=form.cleaned_data.get('content')
				obj=Post.objects.create(content=content,user=user)
				obj.save()
				return redirect('post:list')
			else:
				return redirect('accounts:login')

		return render(self.request,'post/list.html')

# class PostDetailView(DetailView):
# 	model=Post
# 	template_name='post/list.html'



def like(request,id):
	qs=Post.objects.filter(id=id)
	if request.user.is_authenticated:
		is_liked=Post.objects.like_or_unlike(request.user,qs.first())
		return redirect('post:list')
	else:
		return redirect('accounts:login')

	return render(request,'post/list.html')


def dashboard(request):
	if request.user.is_authenticated:
		qs=Post.objects.filter(like=request.user).prefetch_related('like')
		context={
		 'objects':qs
		}
		return render(request,'post/dashboard.html',context)

	return redirect('accounts:login')



