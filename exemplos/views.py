from django.shortcuts import render


def get_bootstrap(request):
    return render(request, 'exemplos/12_utilitários.html')
