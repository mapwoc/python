#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 13:39:02 2020

@author: mapwoc
"""
print('************* DP CARTOLA FC *************')
nome_time = input("Nome do Time: ") 
arquivo = open(nome_time+".txt", 'w')
print ('INFORME GOLEIRO: ')
goleiro = input ('1- ')
arquivo.writ(goleiro+ "(G)" + "\n")
print('INFORME JWWWOGADORES: ')
for i in range (2,12)
    jogador = str(input(i+"- "))
    arquivo.write(jogador+ "(J)" +"\n")
print('INFORME TREINADOR: ')
tecnico = input("TÉCNICO: ")
arquivo.write(tecnico+ "(T)" +"\n")
print('ESCALAÇÃO GERAL: ')
arquivo = open(nome_time+".txt", ' ')
print(arquivo.reader())
print('ESCALAÇÃO POR POSIÇÃO: ');
opcao = input('Informe a posição: \n   1- Goleiro\n   2-Jogador\n   3- Técnico: \n   Opção: ')
arquivo = open(nome_time+".txt", 'r')
escalacao = arquivo.readlines()
 
if opcao = '1':
    print(escalacao[0])
elif opcao == '2':
    for i in range (1,10):
        print(escalacao[i])
else:
    print(escalacao[11])
 
arquivo.close()
input()
