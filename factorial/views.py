from django.http import HttpResponse
from django.shortcuts import render
from factorial.forms import input_form
# Create your views here.
def fact(request):
    if request.method == "POST":
        form = input_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get("input")
            result = 1
            for i in range(1,data+1,1):
                result = result*i
            return render(request,"factorial/index.html",{"param1":result,"param2":data})
    else: 
        form = input_form()
    return render(request,"factorial/index.html",{"form":form})


