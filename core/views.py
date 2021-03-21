from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos!</h1>'.format(nome, idade))

def soma(request, valor1, valor2):
    return HttpResponse('<h1>A Soma de  {} + {} = {} !</h1>'.format(valor1, valor2, valor1+valor2))

def subtracao(request, valor1, valor2):
    return HttpResponse('<h1>A Subtração de  {} - {} = {} !</h1>'.format(valor1, valor2, valor1-valor2))

def multiplicacao(request, valor1, valor2):
    return HttpResponse('<h1>A Multiplicação  de  {} * {} = {} !</h1>'.format(valor1, valor2, valor1*valor2))

def divisao(request, valor1, valor2):
    return HttpResponse('<h1>A Divisão de  {} / {} = {} !</h1>'.format(valor1, valor2, valor1/valor2))