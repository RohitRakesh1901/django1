from django.shortcuts import render
def home(request):
    colorcode = "#ffff00"
    return render(request,'color1/index.html',{'param1':colorcode})
# Create your views here.
