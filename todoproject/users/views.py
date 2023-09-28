from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def homeUsers(request):
    # borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    return render(request, 'users/index.html')