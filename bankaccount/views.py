from django.shortcuts import render
from bankaccount.forms import inputform
def openaccount(request):
    accountnumber = 111111
    if request.method == "POST":
        form1 = inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            name=data.get("name")
            dateofbirth = data.get("dob")
            socialinsurancenumber = data.get("sin")
            accountnumber = accountnumber + 1
            return render(request,"html/index.html",{"param1":"Congratulations "+name+" your account has been created successfully", "param2":"account number:" +str(accountnumber)})
    else:
        form1=inputform()       
    return render(request,"html/index.html",{"form":form1})

