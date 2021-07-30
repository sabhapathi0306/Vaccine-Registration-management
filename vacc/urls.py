
from django import urls
from django.urls import path

from . import views
from .views import index, retrive,updation,register,login,delet,delition
from django.contrib.auth.views import LoginView
from django.views.generic import RedirectView

from.import views
urlpatterns = [
    path('',views.index,name='finaluser'),
    path('retrive.html', views.retrive, name='doctor'),
    path('edit.html/<int:id>',views.updation,name = "ud"),
    path('',RedirectView.as_view(url = '/edit.html/') ),
    path('register.html',views.register,name = "register"),
    path('login.html', views.login,name='login'),
    path('status.html', views.status,name = 'login'),
    path('/',views.index ),
    path('delet.html',views.delet,name = 'delet'),
    path('deletion.html/<int:id>',views.delition,name = "ud")

]