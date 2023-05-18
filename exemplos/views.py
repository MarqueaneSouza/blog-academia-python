from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
import re

def get_bootstrap(request):
    return render(request, 'exemplos/16_forms_parte_i.html')

# Executa as seguintes validações:
'''
    1. ter tamanho mínimo 6 e no máximo 15 caracteres.
    2. Deves ter somente letras e numero e caractere especial(!#@$%&)
    3. Deve ter no mínimo uma letra maiúscula e minúscula.
    4. Deve ter no mínimo um numero.
    5. Deve ter no mínimo caractere especial(!#@$%&)
'''
def validou_senha(senha):
    regex = '^(?=.*[A-Z])(?=.*[!#@$%&])(?=.*[0-9])(?=.*[a-z]).{6,15}$'
    if (re.search(regex, senha)):
        return True
    else:
        return False

# Faz validação do email utilizando regex
def validou_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return True
    else:
        return False

# Caso email e senha tenha passado pela validação, retorna True
def validou_form(email, senha):
    if validou_email(email) and validou_senha(senha):
        return True
    else:
        return False

def processa_formulario_v1(request):
    email = request.POST.get("email")
    senha = request.POST.get("senha")

    email_st = 'is-valid'
    senha_st = 'is-valid'


    if validou_form(email, senha):
        return HttpResponseRedirect("/")
    else:
        if not validou_email(email):
            email_st = 'is-invalid'
        if not validou_senha(senha):
            senha_st = 'is-invalid'

        context = {
            "email": email,
            "senha": senha,
            "email_st": email_st,
            "senha_st": senha_st
        }

        return render(request, 'exemplos/16_forms_parte_i.html', context)
