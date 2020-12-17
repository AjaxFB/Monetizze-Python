#!/usr/bin/python
# Bruno Henrique Moraes D'Amato
# https://www.linkedin.com/in/brunodamato/
# https://www.python.org/dev/peps/pep-0008/
# Os 7 requisitos contidos PDF estão referenciados no comentários como R_número_do_requisito
# Este arquivo não possúi testes funcionais ou unitários

import random

class Loteria:
    def __init__(self,quantidade_de_dezenas=6,total_jogos=1): #R_1 #R_3
        self.__quantidade_de_dezenas = quantidade_de_dezenas #Valor padrão configurado para 6
        self.__resultado = [] #Valor padrão é uma lista vazia
        self.__total_jogos = total_jogos #Valor padrão configurado para 1
        self.__jogos = [] #Valor padrão é uma lista vazia
    
    def set_quantidade_de_dezenas(self,quantidade_de_dezenas): #R_2
        if quantidade_de_dezenas == 6:
            self.__quantidade_de_dezenas = quantidade_de_dezenas
        elif quantidade_de_dezenas == 7:
            self.__quantidade_de_dezenas = quantidade_de_dezenas
        elif quantidade_de_dezenas == 8:
            self.__quantidade_de_dezenas = quantidade_de_dezenas
        elif quantidade_de_dezenas == 9:
            self.__quantidade_de_dezenas = quantidade_de_dezenas
        elif quantidade_de_dezenas == 10:
            self.__quantidade_de_dezenas = quantidade_de_dezenas
        else:
            self.__quantidade_de_dezenas = 6
    
    def get_quantidade_de_dezenas(self): #R_2
        quantidade_de_dezenas = self.__quantidade_de_dezenas
        return quantidade_de_dezenas
    def set_quantidade_de_dezenas(self,quantidade_de_dezenas): #R_2
        self.__quantidade_de_dezenas = quantidade_de_dezenas
    
    def get_resultado(self): #R_2
        resultado = self.__resultado
        return resultado
    def set_resultado(self,resultado): #R_2
        self.__resultado = resultado
    
    def get_total_jogos(self): #R_2
        total_jogos = self.__total_jogos
        return total_jogos
    def set_total_jogos(self,total_jogos): #R_2
        self.__total_jogos = total_jogos
    
    def get_jogos(self): #R_2
        jogos = self.__jogos
        return jogos
    def set_jogos(self,jogos): #R_2
        self.__jogos = jogos
    
    def __gerar_array_de_jogo(self): #R_4 #No contexto de jogos de loteria, os números de 1 a 9 são consideradas dezenas
        array_temporario = []
        while len(array_temporario) < self.__quantidade_de_dezenas:
            numero_aleatorio = random.randint(1, 60)
            if numero_aleatorio not in array_temporario:
                array_temporario.append(numero_aleatorio)
        array_temporario.sort()
        return array_temporario
    
    def gerar_matriz_de_jogos(self): #R_5
        self.__jogos == []
        for jogo in range(self.__total_jogos):
            self.__jogos.append(self.__gerar_array_de_jogo())
    
    def gerar_resultado_de_6_dezenas(self): #R_6
        array_temporario = []
        while len(array_temporario) < 6:
            numero_aleatorio = random.randint(1, 60)
            if numero_aleatorio not in array_temporario:
                array_temporario.append(numero_aleatorio)
        array_temporario.sort()
        self.__resultado = array_temporario
    
    def gerar_html(self): # R_7
        html_temporario = '<table style="width:100%">\n'
        html_temporario += '  <tr>\n'
        html_temporario += '    <th>Jogo</th>\n'
        html_temporario += '    <th>Quantidade de dezenas sorteadas</th>\n'
        html_temporario += '  </tr>\n'
        for jogo in self.__jogos:
            html_temporario += '  <tr>\n'
            html_temporario += '    <td>'+str(jogo)+'</td>\n'
            html_temporario += '    <td>'+str(len(set(self.__resultado).intersection(set(jogo))))+'</td>\n'
            html_temporario += '  </tr>\n'
        html_temporario += '</table>'
        return html_temporario

""" Teste simples no modo interativo
l = Loteria()
#l = Loteria(quantidade_de_dezenas=6,total_jogos=6)
l.get_quantidade_de_dezenas()
l.get_resultado()
l.get_total_jogos()
l.get_jogos()
l.gerar_matriz_de_jogos()
l.get_quantidade_de_dezenas()
l.get_resultado()
l.get_total_jogos()
l.get_jogos()
l.gerar_resultado_de_6_dezenas()
l.get_quantidade_de_dezenas()
l.get_resultado()
l.get_total_jogos()
l.get_jogos()
print(l.gerar_html())
"""