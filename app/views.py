from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from rest_framework.authtoken.models import Token 
from django.contrib.auth.models import User


# Create your views here.



class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('cobertura')


    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispach(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(request.get_succes_url())
        else:
            return super (login,self).dispach(self, *args, **kwargs)
        
    def form_valid(self, form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token = Token.objects.get_or_create(user=user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)


class Registro(FormView):
    template_name = 'registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispach(self, request, *args, **kwargs):
        if request.POST['password1'] == request.POST['password2']:
            return HttpResponseRedirect(request.get_succes_url())
        else:
            return super (login,self).dispach(self, *args, **kwargs)
        
    def form_valid(self, form):
        user = User.objects.create_user(
                username= form.cleaned_data['username'], password = form.cleaned_data['password1'])
        #user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        user.save()
        return redirect('login')

            