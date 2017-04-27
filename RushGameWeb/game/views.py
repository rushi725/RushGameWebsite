from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, UserLoginForm
from django.views.generic import View

def index(request):
	template = loader.get_template('game/first.html')
	return render(request,'game/first.html')


class UserFormView(View):
	form_class = UserForm
	template_name = 'game/registration_form.html'	

	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			#cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns user objects if credential are correct
			user = authenticate(username=username,password=password)

			if user is not None:

				if user .is_active:
					login(request, user)
					return redirect('game:gamelist:index')

		return render(request,self.template_name,{'form':form})


class UserLoginView(View):
	form_class = UserLoginForm
	template_name = 'game/form.html'	

	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():
			
			#cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			#returns user objects if credential are correct
			user = authenticate(username=username,password=password)

			if user is not None:

				if user .is_active:
					login(request, user)
					print(request.user.is_authenticated())
					return redirect('game:gamelist:index')


		return render(request,self.template_name,{'form':form})

def logout_view(request):
    logout(request)
    return redirect('game:login')


