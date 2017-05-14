# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def login(request): 
     if request.method=='POST':
         return redirect('/') 
            
     else: 
       # if request.GET.has_key('password') == False:
       #      return HttpResponse('글 제목을 입력해야 한다우.')
        return render(request, 'jgh/login.html', {})        

def register(request):
       return render(request, 'jgh/register.jsp', {})
class UserCreateView(CreateView):
    template_name = 'jgh/register.jsp'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')
class UserCreateDone(TemplateView):
    template_name = 'jgh/register_done.html'    
        