from django.contrib import admin

from myapp.models import Userdetails

# Register your models here.
@admin.register(Userdetails)
class UserdetailsAdmin(admin.ModelAdmin):

    list_display = ('first_name','last_name','age','email','contact_number')