from django.shortcuts import render

# Create your views here.

def justcheck(request):
    table_val={'a':5,'b':2}
    return render(request,'check.html',{'table_val':table_val})