from django.shortcuts import render
from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm

# Create your views here.
class HomeView(View):
    template_name='login/index.html'

    def get(self,request):
        return render(request,self.template_name)


class LoginView(View):
    template_name = 'login/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        form = LoginForm()
        return render(request, self.template_name,{'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('Success Login')
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login')
        return HttpResponse("This is Login View, Post Request")

class RegisterView(View):
    template_name = 'login/register.html'


    def get(self, request):
        if request.user.is_authenticated:
            print('already logged in. Redirecting.')
            print(request.user)
            return HttpResponseRedirect('/')
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            return HttpResponseRedirect('/login')

        return HttpResponse("This is Index View, POST request")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')