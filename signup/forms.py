from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


# Form for the form validation
class LoginForm(forms.Form):
	error_css_class = 'errors'
	required_css_class = 'required'
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control"}))
	password=forms.CharField( widget=forms.TextInput(attrs={'class': "form-control"}))

	def clean_password(self):
		password=self.cleaned_data.get("password")
		if len(password)<5:
			raise forms.ValidationError("The Password Must Be Greater Than Five")
		return password	
# Form For Pagination
class PaginateForm(forms.Form):
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control"}))
# Form For FileUpload	
class ProfileForm(forms.Form):
   picture=forms.FileField()

class UserLoginForm(forms.Form):
	required_css_class = 'required'
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control"}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"})) 

class AjaxForm(forms.Form):
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control"}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"})) 

class SimpleAjaxForm(forms.Form):
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder': 'Enter The Email','autofocus':'autofocus'}))
