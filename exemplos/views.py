from django.shortcuts import render


def get_bootstrap(request):
    return render(request, 'exemplos/15_display_flex.html')
