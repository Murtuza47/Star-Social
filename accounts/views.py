from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserSignupForm
# Create your views here.


class UserSignupView(CreateView):
    """Form of the user """
    form_class = UserSignupForm
    success_url = reverse_lazy('login')
    template_name = "accounts/signup.html"
