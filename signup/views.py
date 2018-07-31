from django.shortcuts import render
from django.http import HttpResponse
from .models import userSignupModel
from .models import Profile
from signup.forms import LoginForm
from signup.forms import PaginateForm
from signup.forms import SimpleAjaxForm
from django.core.paginator import Paginator
from signup.forms import ProfileForm
from signup.forms import AjaxForm
from signup.forms import UserLoginForm
from .models import UserLoginModel
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from django.http import JsonResponse
from pprint import pprint
import simplejson as json
from django.core.serializers import serialize
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.

def UserSignUp(request):
	if request.method=='POST':
		if request.POST.get('name') and request.POST.get('email') and request.POST.get('password'):
			Name=request.POST['name']
			Email=request.POST['email']
			password=request.POST['password']
			b=userSignupModel(name=Name,email=Email,password=password)
			# post=userSignupModel()
			# post.name=Name
			# post.email=Email
			# post.password=password
			b.save()

			return render(request,'UserSignup.html')
	else:	
		return render(request,'UserSignup.html')

def SelectData(request):
	if request.method=="POST":
		name=request.POST['name']
		results=userSignupModel.objects.filter(name=name)
		return render(request,"DisplayResults.html",{'results':results,})
	else:
		return render(request,'DisplayData.html')

def UpdateData(request):
	if request.method=="POST":
		id=request.POST['id']
		userSignupModel.objects.filter(id='5').update(name='Kiran')
		return render(request,"Update.html")
	else:
		return render(request,"Update.html")

def DeleteData(request):
	if request.method=="POST":
		id=request.POST['id']
		userSignupModel.objects.filter(id=id).delete()
		return render(request,"DeleteData.html")
	else:
		return render(request,"DeleteData.html")	

def loginUser(request):
	form =LoginForm(request.POST)
	if request.method=="POST":
		if form.is_valid():
			return render(request,"Success.html")
		else:
			return render(request,"LoginUser.html",{"form":form})				
	else:
		return render(request,"LoginUser.html",{"form":form})			



def pagination(request):
	results=userSignupModel.objects.all()
	paginator=Paginator(results,2)
	page=request.GET.get('page')
	contacts=paginator.get_page(page)
	return render(request,"Paginate.html",{'results':results,'contacts':contacts})

def SaveProfile(request):
   if request.method == "POST":
      MyProfileForm = ProfileForm(request.POST, request.FILES)
      if MyProfileForm.is_valid():
         profile = Profile()
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         return render(request,"Success.html")
      else:
       	return render(request,"Failure.html")  
   else:
   	form = ProfileForm()	
   	return render(request,'File.html',{'form':form})    


def UserLogin(request):
	form=UserLoginForm(request.POST)				
	if request.method=="POST":
		if form.is_valid():
			email=request.POST['email']
			password=request.POST['password']
			results=UserLoginModel.objects.filter(password=password).count()
			if results>0:
				request.session['email']=email
				return redirect(UserDashboard)
			else:	
				return render(request,"Failure.html")
		else:
			return render(request,"Failure.html")	
	else:
		form=UserLoginForm(request.POST)				
		return render(request,"UserLoginSession.html",{'form':form})


def UserDashboard(request):
	if request.session.has_key('email'):
		return render(request,"LoginSuccess.html")
	else:
		response=redirect(UserLogin)
		response.set_cookie('msg','You Must Login To See The Dashboard!!')	
		return response

def sendMail(request):
	res = send_mail("hello paul", "comment tu vas?", "paul@polo.com", ['zantyabhi123@gmail.com'])
	return HttpResponse('%s'%res)

def logout(request):
	 del request.session['email']
	 return redirect(UserLogin)

def test(request):
	data=UserLoginModel.objects.all()
	return render(request,"DisplayResults.html",{'results':data})

def userAjax(request):
	form=AjaxForm(request.POST)
	return render(request,"Ajax.html",{'form':form})

def simpleAjax(request):
	form=SimpleAjaxForm(request.POST)
	return render(request,"SimpleAjax.html",{'form':form})

def validate(request):
	username = request.GET.get('username', None)
	data = {'is_taken': UserLoginModel.objects.filter(email=username).exists()}
	return JsonResponse(data)	

def listdata(request):
	if request.is_ajax():
		results=UserLoginModel.objects.all()
		number=results.count
		results_serialized=serialize('json',results)
		return JsonResponse(results_serialized,safe=False)
	else:	
		return render(request,"ListData.html")
