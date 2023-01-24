# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 6.6
# Description:      Resolução do problema, livro Perkovic capítulo 6, pág 192.
#
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
# History:          v1.0 29/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
def sync(lista_agendas):
    resultado = set()
    for agenda in lista_agendas:
        for telefone in agenda:
            resultado.add(telefone)

    return resultado


agenda1 = {'(123)456-78-90', '(901)234-56-78', '(321)908-76-54'}
agenda2 = {'(125)452-76-20', '(501)264-96-18', '(361)302-70-84'}
agenda3 = {'(143)491-18-50', '(308)284-16-28', '(361)302-70-84'}
agendas = [agenda1, agenda2, agenda3]

sync(agendas)
