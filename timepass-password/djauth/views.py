from django.shortcuts import redirect
from django.urls import reverse_lazy


def home(request):
    if(request.user.is_authenticated):
        return redirect('dashboard:home')
    else:
        return redirect('login')