from django.shortcuts import render

# Create your views here.
def find_the_target(request):
    return render(request,'index.html',{})