
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.userdetails1,name='Userdetails1'),
    path('/userdetails',views.userdetails2 ,name='Userdetails2'),
]
