from django.shortcuts import render
def second(request):
    d={'name':'Sandhya','age':23}
    return render(request,'second.html',context=d)

# Create your views here.
