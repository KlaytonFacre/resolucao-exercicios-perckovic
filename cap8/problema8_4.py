# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 8.4
# Description:      Resolução do problema livro Perkovic, capítulo 8, pág 266:
#                   Modifique a classe Animal de modo que aceite um construtor
#                   com dois ou nenhum argumento de entrada
# Site:
# Linkedin:         www.linkedin.com/in/klaytonfacre
# Escrito por:      Klayton Facre
# Mantido por:      Klayton Facre
# -------------------------------------------------------------------------------#
# Usage:
# -------------------------------------------------------------------------------#
# Python Version:
#                   3.0 ou superior
# -------------------------------------------------------------------------------#
# History:          v1.0 24/05/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
class Animal:
    nome = ''
    especie = ''
    linguagem = ''
    quantidade_patas = 0

    def setNome(self, string_argumento):
        'Define um nome para o Animal'
        self.nome = string_argumento

    def setEspecie(self, string_argumento):
        'Define a espécie do Animal'
        self.especie = string_argumento

    def setLinguagem(self, string_argumento):
        'Define o tipo de fala do animal (latir, miar, etc)'
        self.linguagem = string_argumento

    def falar(self):
        'Faz o animal exibir uma mensagem de saudação'
        if self.nome == '':
            print('Eu sou um {} e sei {}.'.format(
                self.especie, self.linguagem))
        else:
            print('Olá! Eu sou o {}, sou um {} e sei {}.'.format(
                self.nome, self.especie, self.linguagem))

    def __init__(self, name='', species='', action=''):
        self.nome = name
        self.especie = species
        self.linguagem = action
