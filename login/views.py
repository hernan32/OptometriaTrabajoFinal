from django import forms
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms import CharField
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def login(request):
    return render(request, "login.html")


class BootstrapAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label="",
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeHolder': 'Usuario'})
    )
    password = CharField(
        label="",
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeHolder': 'Contraseña'})
    )


def login(request):
    form = BootstrapAuthenticationForm()
    if request.method == "POST":
        form = BootstrapAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                if request.user.groups.filter(name='Secretaria').exists():
                    return HttpResponseRedirect('/secretaria/turnos/')
                elif request.user.groups.filter(name="Medico").exists():
                    return HttpResponseRedirect('/medico/mis_pacientes/')
                elif request.user.groups.filter(name="Vendedor").exists():
                    return HttpResponseRedirect('/vendedor/pedidos/')
                elif request.user.groups.filter(name="Taller").exists():
                    return HttpResponseRedirect('/tallerista/pedidos/')
                elif request.user.groups.filter(name="Gerencia").exists():
                    return HttpResponseRedirect('/gerente/vista_general/turnos')
                return redirect('/login')

    return render(request, "login.html", {'form': form})


def logout(request):
    do_logout(request)
    return redirect('/login')
