# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
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
    