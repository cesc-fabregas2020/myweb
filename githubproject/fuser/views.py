from django.shortcuts import render

# Create your views here.
def fuser(request):
    return render(request,'index2.html',{})