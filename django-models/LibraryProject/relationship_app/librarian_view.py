from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import HttpResponse

userprofile = UserProfile

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile == 'librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return HttpResponse("Librarian Dashboard")