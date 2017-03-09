from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import EntradaForm


def home(request):
    if (request.method == "POST"):
        entrada_form = EntradaForm(request.POST)
        if (entrada_form.is_valid()):
            return render(request, 'sucess.html', {})
    return render(request, 'index.html', {'form':EntradaForm()})
