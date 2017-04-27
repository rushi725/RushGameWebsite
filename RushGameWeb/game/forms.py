from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','email','password']

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


	
	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get('password')
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("This User Does not exist")

			if not user.check_password(password):
				raise forms.ValidationError("Incorrect Password")
			if not user.is_active:
				raise forms.ValidationError("This User is no longer active")
	
