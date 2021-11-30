from django.http.response import HttpResponse
from django.shortcuts import render
from myapp.models import Userdetails
from myapp.forms import UserdetailsForm1,UserdetailsForm2


# Create your views here.

def userdetails1(request):
 if request.method == 'POST':
    fm = UserdetailsForm1(request.POST) or UserdetailsForm2(request.POST)
    if fm.is_valid():
        first_name = fm.cleaned_data['first_name']
        last_name = fm.cleaned_data['last_name']
        age = fm.cleaned_data['age']

        email = fm.cleaned_data['email']
        contact_number = fm.cleaned_data['contact_number']

        reg = Userdetails(first_name = first_name, last_name = last_name, age = age ,email = email, contact_number = contact_number)
        reg.save()
        return HttpResponse("Form Successfully Submitted")

    fm = UserdetailsForm1()
 else:
    fm = UserdetailsForm1()
      
  
 return render(request, 'userdetails1.html', {'form':fm})


def userdetails2(request,):

        return render(request, 'userdetails2.html')
