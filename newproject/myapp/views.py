
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Result
import urllib
def index(request):
     return render(request, '') 
   # return HttpResponse('<p> Wellcome! Please add /admin to your url and check the data </p>')

#def edit(request):
   # return HttpResponse('<p>Edit page</p>')
#def scorepost(request):
#    if request.method == 'POST':        
#        name = str(request.POST.__getitem__(unicode('user_name')))
#        p = str(request.POST.__getitem__(unicode('password')))
#        e = str(request.POST.__getitem__(unicode('email')))
#        aModel = Result(user_name = name, result = p, difficulty = e)
 #       aModel.save()
 #       return HttpResponse("Score saved")
 #   else:
 #       return HttpResponse("Score not saved")
 #
   
