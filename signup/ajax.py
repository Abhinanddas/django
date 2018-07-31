from dajaxice.utils import deserialize_form
from signup.forms import AjaxForm
from dajax.core import Dajax
from signup.models import UserLoginModel
from dajaxice.decorators import dajaxice_register
from dajaxice.core import dajaxice_functions, Dajaxice
from dajax.core import Dajax


@dajaxice_register
def ajaxform(request, form):
   dajax = Dajax()
   form = AjaxForm(deserialize_form(form))
   if form.is_valid():
      dr = UserLoginModel()
      dr.email = form.cleaned_data.get('email')
      dr.password = form.cleaned_data.get('password')
      dr.save()
      
      dajax.alert("Entry %s was successfully saved." % 
         form.cleaned_data.get('email'))
   else:
      for error in form.errors:
         dajax.add_css_class('#id_%s' % error, 'error')
			
   return dajax.json()