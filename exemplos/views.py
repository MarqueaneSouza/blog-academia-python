from django.shortcuts import render


def get_bootstrap(request):
    return render(request, 'exemplos/11_alinhamentos.html')
