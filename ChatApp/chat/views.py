from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages, auth



def chatPage(request, *args, **kwargs):
	if request.user.is_authenticated:
		context = {}
		return render(request, "chat/chatPage.html", context)
	else:
		return redirect("/login/")

def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/chat/')  # Replace 'home' with the name of your home view or URL
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'chat/LoginPage.html')


def logout(request,*args, **kwargs):
	auth.logout(request)
	return redirect('/login/')
      

def login(request,*args, **kwargs):
    return render(request, 'chat/LoginPage.html')