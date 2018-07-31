from django.urls import path
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from . import views
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
dajaxice_autodiscover()

urlpatterns = [
    path('signup', views.UserSignUp, name='signup'),
    path('select',views.SelectData,name='Select'),
    path('update',views.UpdateData,name='update'),
    path('delete',views.DeleteData,name='delete'),
    path('login',views.loginUser,name='login'),
    path('paginate',views.pagination,name='pagination'),
    path('profile',views.SaveProfile,name='FileUpload'),
    path('userlogin',views.UserLogin,name='Session'),
    path('logout',views.logout,name='Logout'),
    path('sendmail',views.sendMail,name='Mail'),
    path('test',views.test,name='test'),
    path('dashboard',views.UserDashboard,name='dashboard'),
    path('ajax',views.userAjax,name='Ajax'),
    path('simpleajax',views.simpleAjax,name='SimpleAjax'),
    path('validate',views.validate,name='validate'),
    path('list-data',views.listdata,name='list-data'),
    ]
