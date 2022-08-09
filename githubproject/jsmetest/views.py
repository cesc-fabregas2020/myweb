from django.shortcuts import render

# Create your views here.
def drawpic(request):
    return render(request,'jsmetest/test.html',{})