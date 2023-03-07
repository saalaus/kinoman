from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views import View

from authorization.forms import UserLoginForm, NewUserForm


class RegisterView(View):
    def post(self, request: HttpRequest):
        redirect_url = request.GET.get('redirect', '/')
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            login(request, user)
            return redirect(redirect_url)
        else:
            for error in form.errors:
                messages.error(request, form.errors[error], extra_tags='auth')
        return redirect(redirect_url + '#register')


class LoginView(View):
    def post(self, request: HttpRequest):
        redirect_url = request.GET.get('redirect', '/')
        form = UserLoginForm(request.POST, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect(redirect_url)
        else:
            for error in form.errors:
                messages.error(request, form.errors[error], extra_tags='login')
        return redirect(redirect_url + '#login')


def logout_user(request: HttpRequest):
    redirect_url = request.GET.get('redirect', '/')
    logout(request)
    return redirect(redirect_url)
