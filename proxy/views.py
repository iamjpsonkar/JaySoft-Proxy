from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.views import View
from django.http import HttpResponse


page_args = {
    "title":"ProxyHome",
    "title_url":"/proxy"
}

class ProxyView(View):
    def get(self, request):
        return render(request,'proxy/index.html', page_args)

class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        page_args.update({
            'form': form
        })
        return render(request, 'proxy/signup.html', page_args)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home', page_args)
        else:
            page_args.update({
                'form': form
            })
            return render(request, 'proxy/signup.html', page_args)

class SigninView(View):
    def get(self, request):
        form = AuthenticationForm()
        page_args.update({
            'form': form
        })
        return render(request, 'proxy/signin.html', page_args)
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home', page_args)
        else:
            page_args.update({
                'form': form
            })
            return render(request, 'proxy/signin.html', page_args)
