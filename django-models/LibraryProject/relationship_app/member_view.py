from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect, HttpResponse

userprofile = UserProfile

def is_member(user):
    if user.is_authenticated:
        return False
    
    try:
        return userprofile.role == 'admin'
    except userprofile.DoesNotExist:
        return False

@login_required 
@user_passes_test(is_member)
def member_dashboard(request):
    return HttpResponse("Members Dashboard")