# -*- coding: utf-8 -*-

"""
Lets the user to view and edit various user info.
"""
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from userpanel.forms import User
from userpanel.forms import RegisterForm
from django.contrib import auth

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/userpanel/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/userpanel/invalid/")
def new_user_view(request):
    """ Displays a form where you can add a new user
    """
    form = RegisterForm()
    
    return render(request, 'registration/register_user.html', {'form': form, })
    

def save_user_view(request, user_id=None):
    """ Saves a new user or changes on an existing one.
    """
    form = RegisterForm(request.POST)
    form.save()
    form = RegisterForm(request.POST)
    form.save()
    return HttpResponse('OKKKK')

def userpanel_view(request):
    return HttpResponse(__name__ + '2')
