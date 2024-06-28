#***************************************#
# CENTRO DE BIOTECNOLOGIA AGROPECUARIA  #
# NOMBRE EMILIANO PERILLA AGUILAR       #
# VERSION : 4.0                         #
# Fecha: 24/06/2024                     #
#***************************************#

#Este programa se encuentra diseñado par demostrar la funcionalidad que resulta 
# del correcto manejo del POP, mediante super clases, subclases y clases logramos
# crear y modificar los atributos y metodos de un objeto. Super clase persona, Subclase docentes, administrativos y planta con las clases tiempo completo, ocacionales, hora catedra, OPS, auxiliar, tecnico y profesional o, 



from modules import clases  # Importo modulo clases donde esta la informacion principal del programa 
from random import randint # Importo randint para sacar valore aleatorios en algunos estados 
from modules import functions as Fun # Importo funciones donde se encuentran funciones de control de entrada 


while True:
  print("-----------------------")
  print("EJERCICIO RETO 3:")# Menu de control para hacer mas organizada la presentacion del programa 
  print("1. Datos Tiempo Completo") # Opcion 1 
  print("2. Datos Ocasionales")   # Opcion 2 datos 
  print("3. Datos Hora catedra") # Opcion 3 datos 
  print("4. Datos Auxiliar") # Opcion 4 datos 
  print("5. Datos Tecnico")   # Opcion 5 datos 
  print("6. Datos Profesional") # Opcion 6 datos 
  print("7. Datos OPS") # Opcion 7 datos
  print("0. Salir") # Opcion 5 para salir del progrma 
  print("-----------------------")
  
  while True:
      try:
          opcion = int(input("Escoge una opción: "))
          break  # Salimos del bucle si se ingresa un número válido
      except ValueError:
          print("Opción inválida. Inténtalo nuevamente.")
    # opcion = int(input("Escoge una opcion: ")) # El usuario escoge una opcion 


  if opcion == 1:
    completo = clases.TiempoCompleto ("", "", "", "", "", "", 0, "", "", "", 0, 0, 0) # Defino el espacio para almacenar los atributos

    completo.leer_datos()       # Esta funcion es para ingresar los datos del usuario por medio de inputs

    completo.informacion_Imprimir_Datos() # Esta funcion sirve para imprimir la funcion ingresada por los inputs 

    completo.estado1() # Esta funcion me imprime mostrar DG

    completo.estado2() # Esta funcion me imprime mostrar EPS 

    completo.estado3() # Esta funcion me imprime mostrar Pension

    completo.estado31() # Esta funcion me imprime mostrar ARL

    completo.estado4() # Esta funcion me imprime calculo SENA

    completo.estado5() # Esta funcion me imprime Caja Compensacion 

    completo.estado6() # Esta funcion me imprime ICBF

    completo.estado7() # Esta funcion me imprime Auxilio Transporte

    completo.estado8() # Esta funcion me imprime sueldo neto

    completo.estado9() # Esta funcion me imprime Mostrar liquidacion AT


  elif opcion== 2:
    
    ocacional = clases.Ocasionales ("", "", "", "", "", "", 0, "", "", "", "", 0, 0) # Defino el espacio para almacenar los atributos

    ocacional.leer_datos() # Esta funcion es para ingresar los datos del usuario por medio de inputs     

    ocacional.informacion_Imprimir_Datos() # Esta funcion 

    ocacional.estado1() # Esta funcion me imprime mostrar DG

    ocacional.estado2() # Esta funcion me imprime mostrar EPS 

    ocacional.estado3() # Esta funcion me imprime mostrar Pension

    ocacional.estado31() # Esta funcion me imprime mostrar ARL

    ocacional.estado4() # Esta funcion me imprime calculo SENA

    ocacional.estado5() # Esta funcion me imprime Caja Compensacion 

    ocacional.estado6() # Esta funcion me imprime ICBF

    ocacional.estado7() # Esta funcion me imprime Auxilio Transporte

    ocacional.estado8() # Esta funcion me imprime sueldo neto

    ocacional.estado9() # Esta funcion me imprime Mostrar liquidacion AT

  elif opcion== 3:

    catedra = clases.HoraCatedra ("", "", "", "", "", "", 0, "", "", 0, 0, 0, 0) # Defino el espacio para almacenar los atributos

    catedra.leer_datos() # Esta funcion es para ingresar los datos del usuario por medio de inputs

    catedra.informacion_Imprimir_Datos() # Esta funcion es para imprimir los datos ingresados  

    catedra.estado1() # Esta funcion me imprime mostrar DG

    catedra.estado2() # Esta funcion me imprime mostrar EPS

    catedra.estado3() # Esta funcion me imprime mostrar Pension

    catedra.estado31() # Esta funcion me imprime mostrar ARL

    catedra.estado4() # Esta funcion me imprime calculo SENA

    catedra.estado5() # Esta funcion me imprime Caja Compensacion 

    catedra.estado6() # Esta funcion me imprime ICBF

    catedra.estado7() # Esta funcion me imprime Auxilio Transporte

    catedra.estado8() # Esta funcion me imprime sueldo neto

    catedra.estado9() # Esta funcion me imprime Mostrar liquidacion AT

    

  elif opcion== 4:

    auxilia = clases.Auxiliar ("", "", "", "", "", "", 0, "", "", "", 0, 0) # Defino el espacio para almacenar los atributos

    auxilia.leer_datos() # Esta funcion es para ingresar los datos del usuario por medio de inputs

    auxilia.informacion_Imprimir_Datos()  # Esta funcion es para imprimir los datos ingresados 

    auxilia.estado1() # Esta funcion me imprime mostrar DG

    auxilia.estado2() # Esta funcion me imprime mostrar EPS

    auxilia.estado3() # Esta funcion me imprime mostrar Pension

    auxilia.estado31() # Esta funcion me imprime mostrar ARL

    auxilia.estado4() # Esta funcion me imprime calculo SENA

    auxilia.estado5() # Esta funcion me imprime Caja Compensacion

    auxilia.estado6() # Esta funcion me imprime ICBF

    auxilia.estado7() # Esta funcion me imprime  Auxilio Transporte

    auxilia.estado8() # Esta funcion me imprime sueldo neto

    auxilia.estado9() # Esta funcion me imprime Mostrar liquidacion AT

    auxilia.estado10() # Esta funcion me imprime Mostrar liquidacion años laborados 
    
  
  elif opcion== 5:

    tecnic = clases.Tecnico("", "", "", "", "", "", 0, "", "", "", 0, 0) # Defino el espacio para almacenar los atributos

    tecnic.leer_datos() # Esta funcion es para ingresar los datos del usuario por medio de inputs

    tecnic.informacion_Imprimir_Datos()  # Esta funcion es para imprimir los datos ingresados 

    tecnic.estado1() # Esta funcion me imprime mostrar DG

    tecnic.estado2() # Esta funcion me imprime mostrar EPS

    tecnic.estado3() # Esta funcion me imprime mostrar Pension

    tecnic.estado31() # Esta funcion me imprime mostrar ARL

    tecnic.estado4() # Esta funcion me imprime calculo SENA

    tecnic.estado5() # Esta funcion me imprime Caja Compensacion

    tecnic.estado6() # Esta funcion me imprime ICBF

    tecnic.estado7() # Esta funcion me imprime Auxilio Transporte

    tecnic.estado8() # Esta funcion me imprime sueldo neto

    tecnic.estado9() # Esta funcion me imprime Mostrar liquidacion AT

    tecnic.estado10() # Esta funcion me imprime Mostrar liquidacion años laborados


  elif opcion== 6:

    profes = clases.Profesional("", "", "", "", "", "", 0, "", "", "", 0, 0) # Defino el espacio para almacenar los atributoso

    profes.leer_datos() # Esta funcion es para ingresar los datos del usuario por medio de inputs

    profes.informacion_Imprimir_Datos()  # Esta funcion es para imprimir los datos ingresados 

    profes.estado1() # Esta funcion me imprime mostrar DG

    profes.estado2() # Esta funcion me imprime mostrar EPS

    profes.estado3() # Esta funcion me imprime mostrar Pension

    profes.estado31() # Esta funcion me imprime mostrar ARL

    profes.estado4() # Esta funcion me imprime calculo SENA

    profes.estado5() # Esta funcion me imprime Caja Compensacion

    profes.estado6() # Esta funcion me imprime ICBF

    profes.estado7() # Esta funcion me imprime Auxilio Transporte

    profes.estado8() # Esta funcion me imprime sueldo neto

    profes.estado9() # Esta funcion me imprime Mostrar liquidacion AT

    profes.estado10() # Esta funcion me imprime Mostrar liquidacion años laborados


  elif opcion== 7:

    prestadorService = clases.OPS("", "", "", "", "", "", 0, "", "", "", 0, 0)# Defino el espacio para almacenar los atributoso

    prestadorService.leer_datos() # Esta funcion es para ingresar los datos del usuario por medio de inputs

    prestadorService.informacion_Imprimir_Datos()  # Esta funcion es para imprimir los datos ingresados 

    prestadorService.estado1() # Esta funcion me imprime  mostrar DG

    prestadorService.estado2() # Esta funcion me imprime mostrar EPS

    prestadorService.estado3() # Esta funcion me imprime mostrar Pension

    prestadorService.estado31() # Esta funcion me imprime mostrar ARL

    prestadorService.estado4() # Esta funcion me imprime calculo SENA

    prestadorService.estado5() # Esta funcion me imprime Caja Compensacion

    prestadorService.estado6() # Esta funcion me imprime ICBF

    prestadorService.estado7() # Esta funcion me imprime Auxilio Transporte

    prestadorService.estado8() # Esta funcion me imprime  sueldo neto

    prestadorService.estado9() # Esta funcion me imprime Mostrar liquidacion AT

    prestadorService.estado10() # Esta funcion me imprime Mostrar liquidacion años laborados

  elif opcion== 0:
    print("Adios") # Al digitar tecla 5 el usuario sale del programa y aparece el letrero ADIOS 
    break          # Declaracion para la finalizacion del bucle while del menu 
  else:
    print("Opcion no valida") # Si se llegase a digitar un numero diferente de 1 a 5 aparece opcion no valida 
