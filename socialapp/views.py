
from django.views.generic import TemplateView

from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

# Create your views here.

class SocialView(TemplateView):
    template_name = 'social.html'

class LogoutView(TemplateView):
    template_name = 'social.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            logout(request)
        return redirect('social')

