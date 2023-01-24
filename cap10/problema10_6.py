# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 10.6
# Description:      Resolução do problema livro Perkovic, capítulo 10, pág 376:
#                   Analisar o tempo de execução de funções desenvolvidas no
#                   capítulo.
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
# History:
#                   v1.0 05/06/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
import time
counter = 0


def build_input(n):
    'Retorna a entrada para as funções a serem testadas'
    return n


def timing(func, n):
    'Roda func() sobre a entrada retornada por build_input'
    # Obtém a entrada para func()
    func_input = build_input(n)

    # Obtém a hora de início da execução da função
    inicio = time.time()
    # Inicia a execução da função a ser testada
    func(func_input)
    # Obtém a hora de término da execução da função
    termino = time.time()

    # Retorna o tempo decorrido entre o término da execução e o início
    return termino - inicio


def timing_analysis(func, start, stop, inc, runs):
    'Exibe os tempos de execução da função func() sobre um range de entradas pré-definido'
    # Para cada tamanho de entrada n
    for n in range(start, stop, inc):
        # Inicializa o acumulador
        acumulador = 0.0

        # Repete runs vezes
        for i in range(runs):
            # Roda func() sobre uma entrada de tamanho n e acumula os tempos de execução
            acumulador += timing(func, n)

        texto = 'Tempo de execução de {} ({}) é {:.7f} segundos.'
        # Exibe os tempos de execução médios para a entrada de tamanho n
        print(texto.format(func.__name__, n, acumulador/runs))


def rpower(a, n):
    global counter

    if n == 0:
        return 1
    else:
        tmp = rpower(a, n//2)

        if n % 2 == 0:
            counter += 1
            return tmp*tmp
        else:
            counter += 2
            return a*tmp*tmp


def pow2(n):
    return 2**n


def rpower2(n):
    return rpower(2, n)


timing_analysis(rpower2, 20000, 80000, 20000, 5)
timing_analysis(pow2, 20000, 80000, 20000, 5)
