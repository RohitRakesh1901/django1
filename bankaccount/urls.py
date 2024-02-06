from django.urls import path
from bankaccount.views import openaccount
urlpatterns = [path('',openaccount),]