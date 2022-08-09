from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Post
from django_tex.shortcuts import render_to_pdf
# Create your views here.

def myblog_list(request):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    return render(request,'docnotes/list.html',{'queryset':queryset})

def myblog_detail(request,slug):
    model = Post.objects.get(slug=slug)
    return render(request,'docnotes/detail.html',{'model':model})

def tex_test(request):
    template_name = 'docnotes/text.tex'
    content = {'foo':'Bar'}
    return render_to_pdf(request,template_name,content,filename='test.pdf')

def stability(request):
    template_name = 'docnotes/stability.tex'
    return render_to_pdf(request,template_name,{},filename='stability.pdf')

def tnik(request):
    template_name = 'docnotes/tnik.tex'
    return render_to_pdf(request,template_name,{},filename='tnik.pdf')

def vae(request):
    template_name = 'docnotes/vae.tex'
    return render_to_pdf(request,template_name,{},filename='vae.pdf')

def nlrp3(request):
    template_name = 'docnotes/nlrp3.tex'
    return render_to_pdf(request,template_name,{},filename='nlrp3.pdf')