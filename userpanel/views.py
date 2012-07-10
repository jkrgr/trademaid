# -*- coding: utf-8 -*-

"""
Lets the user to view and edit various user info.
"""
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from userpanel.forms import UserForm

def new_user_view(request):
    """ Displays a form where you can add a new user
    """
    user = User()
    form = UserForm(instance=user)

    return render_to_response('new_user_form', )

    return HttpResponse(__name__ + '1')

def save_user(request, user_id=None):
    """ Saves a new user or changes on an existing one.
    """

def userpanel_view(request):
    return HttpResponse(__name__ + '2')
