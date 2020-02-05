from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as view_login,authenticate,logout as view_logout

def login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user =authenticate(username=username,password=password)
		if user is not None:
			view_login(request,user)
			return redirect('post:list' )
	return render(request,'accounts/login.html')




def logout(request):
	view_logout(request)
	return redirect('post:list')
