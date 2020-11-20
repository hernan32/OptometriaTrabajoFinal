from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def panel(request):
    if request.user.is_authenticated:
        return render(request, "panel.html")
    return redirect('/login')


def login(request):
    return render(request, "login.html")


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
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
                return redirect('/panel')

    return render(request, "login.html", {'form': form})


def logout(request):
    do_logout(request)
    return redirect('/')
