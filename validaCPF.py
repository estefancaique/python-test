#!/usr/bin/python3
#from flask import Flask

#def validaCPF():
def validaCPF(entrada = str(input("Digite o CPF: "))):
    with open('blacklist.txt' ,'r') as a:
        for cpf in a:
            print(a)

#   with open('blacklist.txt' ,'r') as f:
#        cpf = f.readlines()
#        print(cpf)
#    while cpf == entrada:
#        print('Block')
#    else:
#         print('Livre')
#    for linha in cpf:
#        print(linha)
#        if linha == entrada:


validaCPF()