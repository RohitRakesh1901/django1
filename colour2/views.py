from django.shortcuts import render
def home(request):
    colourlist = ["#ff0000","#00ff00","#0000ff","#ffff00"]
    return render(request,'colour2/index.html',{'param1':colourlist})
# Create your views here.
