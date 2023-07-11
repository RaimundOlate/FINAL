from django.shortcuts import render, redirect
from .models import Auto
from .forms import AutoForm


def index(request):
    return render(request, 'index.html')


def ingreso_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = AutoForm()
    return render(request, 'ingreso_auto.html', {'form': form})


def exito(request):
    return render(request, 'exito.html')
