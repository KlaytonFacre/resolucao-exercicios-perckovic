# -------------------------------------------------------------------------------#
# Program Name:     Exercício 4.14
# Description:      Resolução do problema livro Perkovic, capítulo 4, pág 129.
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
# History:          v1.0 15/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
txt_log = '128.0.0.1 - - [12/Feb/2011:10:31:08 -0600] "GET /docs/test.txt HTTP/1.0"'
endereco = str(txt_log.split()[0])
data = str(txt_log.split()[3] + ' ' + txt_log.split()[4])

print(txt_log)
print(endereco)
print(data)
