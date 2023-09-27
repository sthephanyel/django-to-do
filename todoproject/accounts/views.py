from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #formulario do proprio django
from django.urls import reverse_lazy # é igual ao redirect, mas quando usa class precisa usar ele pra redirecionar o usuario
from django.views import generic # deixa criar uma class bazeadvil

# cadastro de novo usuario
class SignUp(generic.CreateView):
    # usa o formulario do proprio django para registro de novos usuarios
    form_class = UserCreationForm
    # caso tudo de certo, sera redirecionado para o login
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
