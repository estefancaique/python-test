#!/usr/bin/python3
#import io
#from itertools import permutation
from flask import Flask
cpf_lista ='blacklist.txt'

cpf_valido = False
#def validaCPF():
def validaCPF(entrada = str(input("Digite o CPF: "))):
    with open(cpf_lista ,'r') as c:
        linha = 1
        for cpf in c:
            if entrada == cpf.strip():
                cpf_valido = True
                break
            else:
                cpf_valido = False
            linha+=1
    c.close()

    if cpf_valido:
        print("Block")
    else:
        print("Livre") 


validaCPF()