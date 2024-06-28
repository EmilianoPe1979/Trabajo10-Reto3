#***************************************#
# CENTRO DE BIOTECNOLOGIA AGROPECUARIA  #
# NOMBRE EMILIANO PERILLA AGUILAR       #
# VERSION : 4.0                         #
# Fecha: 24/06/2024                     #
#***************************************#

#Este programa se encuentra diseñado par demostrar la funcionalidad que resulta 
# del correcto manejo del POP, mediante super clases, subclases y clases logramos
# crear y modificar los atributos y metodos de un objeto. Super clase persona, Subclase docentes, administrativos y planta con las clases tiempo completo, ocacionales, hora catedra, OPS, auxiliar, tecnico y profesional 



from modules import clases  # Importo modulo clases donde esta la informacion principal del programa 
from random import randint # Importo randint para sacar valore aleatorios en algunos estados 
from modules import functions as Fun # Importo funciones donde se encuentran funciones de control de entrada 
from modules import menu
# from colorama import Fore,Back # Importo colorama para color fondo y fuente


def main(): # Este el programa pricipal de app 

  print(Fore.BLACK + Back.BLUE)# Defino colores fondo y fuente 

  if __name__ == "__main__": # Declaracion que me indica que este es el modulo principal del programa 
    main()