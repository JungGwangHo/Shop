# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from jgh.form import CreateUserForm
# Create your views here.
def login(request): 
     if request.method=='POST':
         return redirect('/') 
            
     else: 
       # if request.GET.has_key('password') == False:
       #      return HttpResponse('글 제목을 입력해야 한다우.')
        return render(request, 'jgh/login.html', {})        

def register(request):
       return render(request, 'jgh/register.html', {})
def register_done(request):
       return render(request, 'jgh/register_done.html', {})
def UserCreateView(request):
    if request.method == "POST":
        userform = CreateUserForm(request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect(
                redirect('register_done.html')
            )
    elif request.method == "GET":
        userform = CreateUserForm()
        return render(request, 'jgh/register.html', {'form':userform,})    
class UserCreateDone(TemplateView):
    template_name = 'jgh/register_done.html'    
        