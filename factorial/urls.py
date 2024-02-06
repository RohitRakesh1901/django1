from django.urls import path
from factorial.views import fact
urlpatterns = [path("",fact)]