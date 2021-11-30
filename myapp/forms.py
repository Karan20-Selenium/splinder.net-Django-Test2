from myapp.models import Userdetails
from django import forms


class UserdetailsForm1(forms.ModelForm):
 
    class Meta:
        model = Userdetails
        fields = ['first_name','last_name','age']
        labels = {'first_name':'Enter First Name','last_name':'Enter Last Name','age':'Enter Age'}
        help_text = {'age':'Only 18 & above'}
        error_message = {'age':'Only 18 years & above are allowed'}


class UserdetailsForm2(forms.ModelForm):
 
    class Meta:
        model = Userdetails
        fields = ['email','contact_number']
        labels = {'email':'Enter Email','contact_number':'Enter Contact Number'}
        help_text = {'contact_number':'Enter without countrycode'}
        error_message = {'contact_number':'Please Enter the Contact number Without Country Code'}

  
  