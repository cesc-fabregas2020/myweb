from django.urls import path
from . import views
 
app_name = 'docnotes'

urlpatterns = [
    path('blog_list/',views.myblog_list,name='blog_list'),
    path('blog_detail/<slug:slug>/',views.myblog_detail,name='blog_detail'),
    path('blog_tex/',views.tex_test,name='tex_text'),
    path('blog_stability/',views.stability,name='stability'),
    path('blog_tnik/',views.tnik,name='tnik'),
    path('blog_vae/',views.vae,name='vae'),
    path('blog_nlrp3/',views.nlrp3,name='nlrp3'),
]