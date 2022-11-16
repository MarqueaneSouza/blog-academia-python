from django.shortcuts import render


def get_bootstrap(request):
    return render(request, 'exemplos/06_grid.html')
