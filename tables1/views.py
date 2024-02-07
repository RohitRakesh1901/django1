from django.shortcuts import render
def home(request):
    list1 = []
    for j in range(3,21,1):
        for i in range(1,11,1):
            temp1 = str(j) +"*"+str(i)+"="+str(j*i)
            list1.append(temp1)
        list1.append(".")


    return render(request,'tables1/index.html',{'param1':list1})
# Create your views here.
