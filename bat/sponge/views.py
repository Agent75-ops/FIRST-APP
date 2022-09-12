from importlib.metadata import requires
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def sponge(request):
    if request.user.is_authenticated : 
        return render(request, "spb/spongebob.html")
    else:
        return HttpResponseRedirect(reverse("form:login"))