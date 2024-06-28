#***************************************#
# CENTRO DE BIOTECNOLOGIA AGROPECUARIA  #
# NOMBRE EMILIANO PERILLA AGUILAR       #
# VERSION : 4.0                         #
# Fecha: 24/06/2024                     #
#***************************************#

#Este programa se encuentra diseñado par demostrar la funcionalidad que resulta 
# del correcto manejo del POP, mediante super clases, subclases y clases logramos
# crear y modificar los atributos y metodos de un objeto. Super clase persona, Subclase docentes, administrativos y planta con las clases tiempo completo, ocacionales, hora catedra, OPS, auxiliar, tecnico y profesional 


from random import randint # Importo randint para sacar valore aleatorios en algunos estados 
from modules import functions as Fun # Importo funciones donde se encuentran funciones de control de entrada 

#----------------------------PERSONA--------------------------
class Persona: # Definicion de la superclase 

    def __init__(self, idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato): # Definicion de la superclase 
        
        self.__idPersona = idPersona   #self argumento id persona            
        self.__nomPersona = nomPersona  # self argumento nomPersona
        self.__apePersona = apePersona # self argumento apPersona
        self.__fechaNacimiento = fechaNacimiento # self argumento FechaNacimiento
        self.__ciudadNacimiento = ciudadNacimiento # # self argumento ciudadNacimiento
        self.__genero = genero # # self argumento genero
        self.__estrato = estrato # # self argumento estrato
       

    def set_idPersona(self, value): # fun set idPersona
        self.__idPersona = value
    

    def get_idPersona(self):  ## fun get idPersona  
        return self.__idPersona
    

    def set_nomPersona(self, value): # fun set nomPersona
        self.__nomPersona = value


    def get_nomPersona(self): # fun get nomPersona
        return self.__nomPersona


    def set_apePersona(self, value): # fun set id apePersona
        self.__apePersona = value


    def get_apePersona(self):   # fun get id apePersona
        return self.__apePersona


    def set_fechaNacimiento(self, value): # fun set fechaNacimiento 
        self.__fechaNacimiento = value


    def get_fechaNacimiento(self):   # fun get fechaNacimiento 
        return self.__fechaNacimiento

    
    def set_ciudadNacimiento(self, value): # fun set ciudadNacimiento
        self.__ciudadNacimiento = value


    def get_ciudadNacimiento(self):   # fun get ciudadNacimiento
        return self.__ciudadNacimiento


    def set_genero(self, value): # fun set genero
        self.__genero = value


    def get_genero(self):   # fun get genero
        return self.__genero


    def set_estrato(self, value): # fun set estrato
        self.__estrato = value


    def get_estrato(self):    # fun get estrato
        return self.__estrato

#----------------------DOCENTES -------------------------------------

class Docentes (Persona): # Definicion de la subclase 


    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "", 
    genero = "", estrato = "", areaFormacion ="", tituloProfesional ="", unidadAcademica = ""):
    #Creacion del constructor y sus argumentos 

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato)
        # Definicion de los self de los argumentos que hereda de la super clase persona
        
        self.__areaFormacion = areaFormacion   
        self.__tituloProfesional = tituloProfesional # Definicion self de los argumentos nuevos
        self.__unidadAcademica = unidadAcademica
   

    def set_areaFormacion(self, value):  # Define el set area formacion
        self.__areaFormacion = value


    def get_areaFormacion(self):        # Define el get del argumento de area formacion
        return self.__areaFormacion


    def set_tituloProfesional(self, value):  # Define el set del argumento de titulo profesional
        self.__tituloProfesional = value


    def get_tituloProfesional(self):      # Define el get del argumento de titulo profesional
        return self.__tituloProfesional


    def set_unidadAcademica(self, value):  # Define el set del argumento de unidad academica
        self.__unidadAcademica = value

    def get_unidadAcademica(self):  # Define el get del argumento de unidad academica
        return self.__unidadAcademica 

#----------------------TIEMPO COMPLETO -------------------------------------

class TiempoCompleto (Docentes):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "", 
    genero = "", estrato = "", areaFormacion ="", tituloProfesional ="", unidadAcademica = "", categoria = "", puntos = "" 
    , salario = ""):  #Creacion del constructor y sus argumentos 

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, 
        areaFormacion, tituloProfesional, unidadAcademica)
        # Definicion de los self de los argumentos que hereda de la super clase persona
        
        self.__categoria = categoria   
        self.__puntos = puntos # Definicion self de los argumentos nuevos
        self.__salario = salario


    def set_categoria(self, value): # Defino set categoria
        self.__categoria = value


    def get_categoria(self): # Defino get categoria
        return self.__categoria


    def set_puntos(self, value): # Defino set puntos
        self.__puntos = value


    def get_puntos(self): # Defino get puntos 
        return self.__puntos

    
    def set_salario(self, value): # Defino set salario
        self.__salario = value


    def get_salario(self): # Defino get salario
        return self.__salario


    def leer_datos(self): # Funcion para leer datos 

        print("___________INGRESO DE DATOS________________")
        self.set_idPersona (Fun.control_numeros_letras("Digite el ID de la persona: ")) # input id persona 
        self.set_nomPersona (Fun.control_letras("Digite el nombre: ")) # input nombre persona 
        self.set_apePersona (Fun.control_letras("Digite el apellido: ")) # input apellido persona 
        self.set_fechaNacimiento (Fun.control_numeros_letras("Digite la fecha de nacimiento: ")) # input fecha nacimiento
        self.set_ciudadNacimiento (Fun.control_letras("Escriba la ciudad de nacimiento: ")) # input lugar nacimiento
        self.set_genero (Fun.control_letras("Digite el genero de la persona: ")) # imput genero
        self.set_estrato(Fun.control_numeros("Digite el estrato del docente: ")) # input estrato
        self.set_areaFormacion (Fun.control_letras("Digite el area de formacion del docente: ")) # input area formacion 
        self.set_tituloProfesional (Fun.control_letras("Digite el titulo profesional del docente: ")) # input titulo
        self.set_unidadAcademica (Fun.control_letras("Digite la unidad academica del docente: ")) # input unidad academica
        self.set_categoria (Fun.control_letras("Digite la categoria del docente: ")) # input categoria
        self.set_puntos (Fun.control_numeros("Digite la cantidad de puntos del docente: ")) # input puntos
        self.set_salario(Fun.control_numeros("Digite el salario del docente: ")) # Input salario del docente
    # Funcion para el ingreso de datos de la clase 


    def informacion_Imprimir_Datos(self): # Esta funcion muestra los datos ingresados por el usuario en los inputs

        print("---------DATOS INGRESADOS------------\n"
        "ID personal: {0}\n" 
        "Nombre :  {1}\n" 
        "Apellido : {2}\n" 
        "Fecha de nacimiento: {3}\n"       
        "Ciudad de nacimiento : {4}\n"  # Datos ingresados por el usuario en los inputs
        "Genero de la persona: {5}\n"
        "Estrato socio-economico:{6}\n" 
        "Area de formacion del docente es:{7}\n"
        "Titulo profesional del docente es:{8}\n"
        "Unidad academica es: {9}\n"
        "Categoria del docente es: {10}\n"
        "Cantidad de puntos del docente es: {11}\n"
        "Salario basico del docente es: {12}". format( self.get_idPersona(), self.get_nomPersona(), self.get_apePersona (), 
        self.get_fechaNacimiento(), self.get_ciudadNacimiento(), self.get_genero(), self.get_estrato() , self.get_areaFormacion(), 
        self.get_tituloProfesional(), self.get_unidadAcademica(), self.get_categoria(), self.get_puntos(), self.get_salario() ,end =""))
        # Con los self get llamamos los datos para la impresion. 


    def estado1(self):
        estados = ["En DG1", "En DG2", "En DG3", "En DG4"] # funcion con randit para mostrar los datos 
        emi= randint(0,len(estados) -1)
        print("Aporte DG : {0}".format(estados[emi]))

    def estado2(self):
        estados = ["150mil", "200mil", "300mil", "50mil"] # funcion con randint para mostrar aportes EPS 
        emi= randint(0,len(estados) -1)
        print("Aporte de EPS : {0}".format(estados[emi]))

    def estado3(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                     # funcion con randint para mostrar aporte pension
        print("Aporte de PENSION: {0}".format(estados[emi]))


    def estado31(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                 # funcion con randint para mostrar aporte ARL
        print("Aporte de ARL: {0}".format(estados[emi]))

    def estado4(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                 # funcion con randint para mostrar parafiscal SENA 
        print("Parafiscal SENA: {0}".format(estados[emi]))

    def estado5(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                 # funcion con randint para mostrar aporte caja compesacion
        print("Valor aporte caja de compensacion : {0}".format(estados[emi]))

    def estado6(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)         # funcion con randint para mostrar aporte parafiscal ICBF
        print("Parafiscal ICBF: {0}".format(estados[emi]))

    def estado7(self):
        estados = ["120mil", "100mil", "150mil", "115mil"]
        emi= randint(0,len(estados) -1)         # funcion con randint para mostrar auxilio transporte
        print("Auxilio de transporte: {0}".format(estados[emi]))

    def estado8(self):
        estados = ["1.500.000", "2.000.000", "3.000.000", "2.500.000"]
        emi= randint(0,len(estados) -1)         # funcion con randint parta mostar sueldo neto devengado
        print("Sueldo Neto devengado: {0}".format(estados[emi]))

    def estado9(self):
        estados = ["12 millones", "10 millones", "20 millones", "42 millones"]
        emi= randint(0,len(estados) -1)             # funcion con randint para mostrar liquidacion tiempo completo 
        print("Liquidacion Tiempo completo : {0}".format(estados[emi]))

   

#----------------------OCASIONALES -------------------------------------

class Ocasionales (Docentes):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
     genero = "", estrato = "", areaFormacion ="", tituloProfesional ="", unidadAcademica = "", ultimoTitulo = "", numMeses = "" 
     , salario = ""):  #Creacion del constructor y sus argumentos 

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, 
        areaFormacion, tituloProfesional, unidadAcademica)
        # Definicion de los self de los argumentos que hereda de la super clase persona
        
        self.__ultimoTitulo = ultimoTitulo 
        self.__numMeses = numMeses # Definicion self de los argumentos nuevos
        self.__salario = salario


    def set_ultimoTitulo(self, value): # Defino set ultimoTitulo
        self.__ultimoTitulo = value


    def get_ultimoTitulo(self): # Defino get ultimoTitulo
        return self.__ultimoTitulo


    def set_numMeses(self, value): # Defino set numMeses
        self.__numMeses = value


    def get_numMeses(self): # Defino get numMes
        return self.__numMeses

    
    def set_salario(self, value): # Defino set salario
        self.__salario = value


    def get_salario(self): # Defino get salario
        return self.__salario


    def leer_datos(self):  # Funcion para leer datos 

        print("___________INGRESO DE DATOS________________")
        self.set_idPersona (Fun.control_numeros_letras("Digite el ID de la persona: ")) # input id persona 
        self.set_nomPersona (Fun.control_letras("Digite el nombre: ")) # input nom persona
        self.set_apePersona (Fun.control_letras("Digite el apellido: "))    # input apellido
        self.set_fechaNacimiento (Fun.control_numeros_letras("Digite la fecha de nacimiento: "))    # input fecha nacimiento
        self.set_ciudadNacimiento (Fun.control_letras("Escriba la ciudad de nacimiento: ")) # input lugar nacimiento 
        self.set_genero (Fun.control_letras("Digite el genero de la persona: ")) # input genero persona
        self.set_estrato(Fun.control_numeros("Digite el estrato del docente: ")) # input estrato docente 
        self.set_areaFormacion (Fun.control_letras("Digite el area de formacion del docente: "))  # input titulo docente 
        self.set_tituloProfesional (Fun.control_letras("Digite el titulo profesional del docente: ")) # input titulo profesional 
        self.set_unidadAcademica (Fun.control_letras("Digite la unidad academica del docente: ")) # input unidad academica 
        self.set_ultimoTitulo (Fun.control_letras("Digite el ultimo titulo obtenido: ")) # input ultimo titulo
        self.set_numMeses (Fun.control_numeros("Digite la cantidad de meses trabajados: ")) # input num mesese trabajados 
        self.set_salario(Fun.control_numeros("Digite el salario del docente: ")) # input salario docente 


    def informacion_Imprimir_Datos(self): # Esta funcion muestra los datos ingresados por el usuario en los inputs

        print("---------DATOS INGRESADOS------------\n"
        "ID personal: {0}\n" 
        "Nombre :  {1}\n" 
        "Apellido : {2}\n" 
        "Fecha de nacimiento: {3}\n"
        "Ciudad de nacimiento : {4}\n"
        "Genero de la persona: {5}\n"              
        "Ciudad de nacimiento : {4}\n"  # Datos ingresados por el usuario en los inputs
        "Estrato socio-economico:{6}\n" 
        "Area de formacion del docente es:{7}\n"
        "Titulo profesional del docente es:{8}\n"
        "Unidad academica es: {9}\n"
        "El ultimo titulo del docente es: {10}\n"
        "Cantidad de meses de trabajo del docente es: {11}\n"
        "Salario basico del docente es: {12}". format( self.get_idPersona(), self.get_nomPersona(), self.get_apePersona (), 
        self.get_fechaNacimiento(), self.get_ciudadNacimiento(), self.get_genero(), self.get_estrato() , self.get_areaFormacion(), 
        self.get_tituloProfesional(), self.get_unidadAcademica(), self.get_ultimoTitulo(), self.get_numMeses(), self.get_salario() ,end =""))  # Con los self get llamamos los datos para la impresion. 

    def estado1(self):
        estados = ["En DG1", "En DG2", "En DG3", "En DG4"] # funcion con randit para mostrar los datos 
        emi= randint(0,len(estados) -1)
        print("Aporte DG : {0}".format(estados[emi]))

    def estado2(self):
        estados = ["150mil", "200mil", "300mil", "50mil"] # funcion con randit para mostrar EPS
        emi= randint(0,len(estados) -1)
        print("Aporte de EPS : {0}".format(estados[emi]))

    def estado3(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]  # funcion con randint para mostrar aporte pension 
        emi= randint(0,len(estados) -1)
        print("Aporte de PENSION: {0}".format(estados[emi]))


    def estado31(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                    # funcion con randint para mostrar aportes ARL
        print("Aporte de ARL: {0}".format(estados[emi]))

    def estado4(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                     # funcion con randint para mostrar aportes SENA
        print("Parafiscal SENA: {0}".format(estados[emi]))

    def estado5(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                    # funcion con randint  aportes caja compensacion 
        print("Valor aporte caja de compensacion : {0}".format(estados[emi]))

    def estado6(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                 # funcion con randint para mostrar  parafiscal ICBF
        print("Parafiscal ICBF: {0}".format(estados[emi]))

    def estado7(self):
        estados = ["120mil", "100mil", "150mil", "115mil"]
        emi= randint(0,len(estados) -1)                     # funcion con randint para mostrar auxilio transporte 
        print("Auxilio de transporte: {0}".format(estados[emi]))

    def estado8(self):
        estados = ["1.500.000", "2.000.000", "3.000.000", "2.500.000"]
        emi= randint(0,len(estados) -1)                     # funcion con randint para mostrar sueldo neto devengado
        print("Sueldo Neto devengado: {0}".format(estados[emi]))

    def estado9(self):
        estados = ["12 millones", "10 millones", "20 millones", "42 millones"]
        emi= randint(0,len(estados) -1)                     # funcion con randint para liquidacion tiempo completo 
        print("Liquidacion Tiempo completo : {0}".format(estados[emi]))

#----------------------HORA CATEDRA-------------------------------------

class HoraCatedra (Docentes):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
    genero = "", estrato = "", areaFormacion ="", tituloProfesional ="", unidadAcademica = "", ultimoTitulo = "", numHoras = "" 
    ,ValorContrato = "", salario = ""): #Creacion del constructor y sus argumentos 

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, 
        areaFormacion, tituloProfesional, unidadAcademica)
        # Definicion de los self de los argumentos que hereda de la super clase persona
        
        self.__ultimoTitulo = ultimoTitulo 
        self.__numHoras = numHoras
        self.__valorContrato = ValorContrato # Definicion self de los argumentos nuevos
        self.__salario = salario

    def set_ultimoTitulo(self, value): # Defino set ultimoTitulo
        self.__ultimoTitulo = value


    def get_ultimoTitulo(self): # Defino get ultimoTitulo
        return self.__ultimoTitulo


    def set_numHoras(self, value): # Defino set numHoras
        self.__numHoras = value


    def get_numHoras(self): # Defino get numHoras
        return self.__numHoras


    def set_valorContrato(self, value): # Defino set valorContrato
        self.__valorContrato = value


    def get_valorContrato(self): # Defino get valorContrato
        return self.__valorContrato

    
    def set_salario(self, value): # Defino set salario
        self.__salario = value


    def get_salario(self): # Defino get salario 
        return self.__salario

    def leer_datos(self):  # Funcion para leer datos 

        print("___________INGRESO DE DATOS________________")
        self.set_idPersona (Fun.control_numeros_letras("Digite el ID de la persona: "))  # input id persona 
        self.set_nomPersona (Fun.control_letras("Digite el nombre: "))  # input nom persona
        self.set_apePersona (Fun.control_letras("Digite el apellido: "))  # input apellido
        self.set_fechaNacimiento (Fun.control_numeros_letras("Digite la fecha de nacimiento: ")) # input fecha nacimiento
        self.set_ciudadNacimiento (Fun.control_letras("Escriba la ciudad de nacimiento: ")) # input lugar nacimiento 
        self.set_genero (Fun.control_letras("Digite el genero de la persona: ")) # input genero persona
        self.set_estrato(Fun.control_numeros("Digite el estrato del docente: ")) # input estrato docente 
        self.set_areaFormacion (Fun.control_letras("Digite el area de formacion del docente: "))  # input titulo docente 
        self.set_tituloProfesional (Fun.control_letras("Digite el titulo profesional del docente: ")) # input titulo profesional 
        self.set_unidadAcademica (Fun.control_letras("Digite la unidad academica del docente: "))  # input unidad academica 
        self.set_ultimoTitulo (Fun.control_letras("Digite el ultimo titulo obtenido: "))  # input ultimo titulo
        self.set_numHoras (Fun.control_numeros("Digite la cantidad de horas catedras dictadas: ")) # input num mesese trabajados 
        self.set_valorContrato (Fun.control_numeros("Digite el valor global neto del contrato acordado: "))# input salario global 
        self.set_salario(Fun.control_numeros("Digite el salario basico sin horas catedra del docente: ")) # input salario basico


    def informacion_Imprimir_Datos(self):  # Esta funcion muestra los datos ingresados por el usuario en los inputs

        print("---------DATOS INGRESADOS------------\n"
        "ID personal: {0}\n" 
        "Nombre :  {1}\n" 
        "Apellido : {2}\n" 
        "Fecha de nacimiento: {3}\n"
        "Ciudad de nacimiento : {4}\n"
        "Genero de la persona: {5}\n"       # Datos ingresados por el usuario en los inputs
        "Estrato socio-economico:{6}\n" 
        "Area de formacion del docente es:{7}\n"
        "Titulo profesional del docente es:{8}\n"
        "Unidad academica es: {9}\n"
        "El ultimo titulo del docente es: {10}\n"
        "Cantidad de horas catedra del docente es: {11}\n"
        "Valor del contrato docente hora catedra {12}"
        "Valor del salario basico docente hora catedra {13}". format( self.get_idPersona(), self.get_nomPersona(), self.get_apePersona (), 
        self.get_fechaNacimiento(), self.get_ciudadNacimiento(), self.get_genero(), self.get_estrato() , self.get_areaFormacion(), 
        self.get_tituloProfesional(), self.get_unidadAcademica(), self.get_ultimoTitulo(), self.get_numHoras(), self.get_valorContrato(), self.get_salario() ,end =""))  
        # Con los self get llamamos los datos para la impresion. 


    def estado1(self):
        estados = ["En DG1", "En DG2", "En DG3", "En DG4"] # funcion con randit para mostrar los datos 
        emi= randint(0,len(estados) -1)
        print("Aporte DG : {0}".format(estados[emi]))


    def estado2(self):
        estados = ["150mil", "200mil", "300mil", "50mil"] # funcion con randit para mostrar EPS
        emi= randint(0,len(estados) -1)
        print("Aporte de EPS : {0}".format(estados[emi]))


    def estado3(self):
        estados = ["150mil", "200mil", "300mil", "50mil"] # funcion con randint para mostrar aporte pension 
        emi= randint(0,len(estados) -1)
        print("Aporte de PENSION: {0}".format(estados[emi]))


    def estado31(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]  # funcion con randint para mostrar aportes ARL
        emi= randint(0,len(estados) -1)
        print("Aporte de ARL: {0}".format(estados[emi]))


    def estado4(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                      # funcion con randint para mostrar aportes SENA
        print("Parafiscal SENA: {0}".format(estados[emi]))


    def estado5(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)         # funcion con randint  aportes caja compensacion 
        print("Valor aporte caja de compensacion : {0}".format(estados[emi]))


    def estado6(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)           # funcion con randint para mostrar  parafiscal ICBF
        print("Parafiscal ICBF: {0}".format(estados[emi]))


    def estado7(self):
        estados = ["120mil", "100mil", "150mil", "115mil"]
        emi= randint(0,len(estados) -1)              # funcion con randint para mostrar auxilio transporte 
        print("Auxilio de transporte: {0}".format(estados[emi]))


    def estado8(self):
        estados = ["1.500.000", "2.000.000", "3.000.000", "2.500.000"]
        emi= randint(0,len(estados) -1)             # funcion con randint para mostrar sueldo neto devengado
        print("Sueldo Neto devengado: {0}".format(estados[emi]))


    def estado9(self):
        estados = ["12 millones", "10 millones", "20 millones", "42 millones"]
        emi= randint(0,len(estados) -1)    # funcion con randint para liquidacion tiempo completo 
        print("Liquidacion Tiempo completo : {0}".format(estados[emi]))

#----------------------ADMINISTRATIVOS-------------------------------------

class Administrativos (Persona):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
    genero = "", estrato = "", dependencia ="", titulo=""): #Creacion del constructor y sus argumentos 


        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato)
       # Definicion de los self de los argumentos que hereda de la super clase persona


        self.__dependencia = dependencia # Definicion self de los argumentos nuevos
        self.__titulo = titulo

    def set_dependencia(self, value): # Defino set dependencia
        self.__dependencia = value 


    def get_dependencia(self): # Defino get dependencia
        return self.__dependencia


    def set_titulo(self, value): # Defino set titulo
        self.__titulo = value


    def get_titulo(self):   # Defino get titulo
        return self.__titulo

#----------------------OPS-------------------------------------

class OPS (Administrativos):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
    genero = "", estrato = "", dependencia = "", titulo = "", fechaVinculacion ="", numMeses="", ValorContrato ="", salario=""):  #Creacion del constructor y sus argumentos 

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo)  # Definicion de los self de los argumentos que hereda de la sub clase administrativos

        self.__fechaVinculacion = fechaVinculacion 
        self.__numMeses = numMeses      # Definicion self de los argumentos nuevos
        self.__valorContrato = ValorContrato
        self.__salario = salario


    def set_fechaVinculacion(self, value): # Defino set fecha vinculacion 
        self.__fechaVinculacion = value


    def get_fechaVinculacion(self): # Defino get fecha vinculacion 
        return self.__fechaVinculacion


    def set_numMeses(self, value): # Defino Set numMeses
        self.__numMeses = value


    def get_numMeses(self): # Defino Get numMeses  
        return self.__numMeses


    def set_valorContrato(self, value): # Defino Set valor Contrato
        self.__valorContrato = value


    def get_valorContrato(self): # Defino Get valor Contrato
        return self.__valorContrato


    def set_salario(self, value): # Defino Set salario
        self.__salario = value


    def get_salario(self): # Defino get salario 
        return self.__salario


    def leer_datos(self):
        print("___________INGRESO DE DATOS________________")
        self.set_idPersona (Fun.control_numeros_letras("Digite el ID de la persona: ")) # input id persona
        self.set_nomPersona (Fun.control_letras("Digite el nombre: "))  # input nom persona
        self.set_apePersona (Fun.control_letras("Digite el apellido: "))  # input apellido
        self.set_fechaNacimiento (Fun.control_numeros_letras("Digite la fecha de nacimiento: "))  # input fecha nacimiento
        self.set_ciudadNacimiento (Fun.control_letras("Escriba la ciudad de nacimiento: ")) # input lugar nacimiento 
        self.set_genero (Fun.control_letras("Digite el genero de la persona: "))  # input genero persona
        self.set_estrato(Fun.control_numeros("Digite el estrato socioeconomico: "))  # input estrato docent
        self.set_dependencia (Fun.control_letras("Digite la dependencia donde labora el OPS: ")) # input dependencia 
        self.set_titulo (Fun.control_letras("Digite el titulo academico del OPS: ")) # input dependencia
        self.set_fechaVinculacion (Fun.control_letras("Digite la fecha de vinculacion del OPS: ")) # input fecha de vinculacion del OPS
        self.set_numMeses (Fun.control_numeros("Digite el numero de meses del contrato del prestador de servicios: ")) # input numMeses 
        self.set_valorContrato (Fun.control_numeros("Digite el valor global total del contrato acordado: ")) # input valor contrato
        

    def informacion_Imprimir_Datos(self):

        print("---------DATOS INGRESADOS------------\n"
        "ID personal: {0}\n" 
        "Nombre :  {1}\n" 
        "Apellido : {2}\n" 
        "Fecha de nacimiento: {3}\n"
        "Ciudad de nacimiento : {4}\n"            # Datos ingresados por el usuario en los inputs
        "Genero de la persona: {5}\n"
        "Estrato socio-economico:{6}\n" 
        "La dependencia donde labora el OPS es :{7}\n"
        "Titulo academico del OPS :{8}\n"
        "La fecha de vinculacio del OPS es: {9}\n"
        "La cantidad de meses del contrato del OPS es : {10}\n"
        "El valor del contrato global del OPS es : {11}\n"
        "Valor del salario neto mensual del OPS es: {12}". format( self.get_idPersona(), self.get_nomPersona(), self.get_apePersona (), 
        self.get_fechaNacimiento(), self.get_ciudadNacimiento(), self.get_genero(), self.get_estrato() , self.get_dependencia(), 
        self.get_titulo(), self.get_fechaVinculacion(), self.get_numMeses(), self.get_valorContrato(), self.get_salario(), end =""))
         # Con los self get llamamos los datos para la impresion.

    def estado1(self):
        estados = ["En DG1", "En DG2", "En DG3", "En DG4"] # funcion con randit para mostrar los datos 
        emi= randint(0,len(estados) -1)
        print("Aporte DG : {0}".format(estados[emi]))


    def estado2(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                 # funcion con randit para mostrar aportes EPS
        print("Aporte de EPS : {0}".format(estados[emi]))


    def estado3(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                 # funcion con randint para mostrar aporte pension 
        print("Aporte de PENSION: {0}".format(estados[emi]))


    def estado31(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                  # funcion con randint para mostrar aportes ARL
        print("Aporte de ARL: {0}".format(estados[emi]))

    def estado4(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                    # funcion con randint para mostrar aportes SENA
        print("Parafiscal SENA: {0}".format(estados[emi]))

    def estado5(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                    # funcion con randint  aportes caja compensacion 
        print("Valor aporte caja de compensacion : {0}".format(estados[emi]))

    def estado6(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)             # funcion con randint para mostrar  parafiscal ICBF
        print("Parafiscal ICBF: {0}".format(estados[emi]))

    def estado7(self):
        estados = ["120mil", "100mil", "150mil", "115mil"]
        emi= randint(0,len(estados) -1) # funcion con randint para mostrar auxilio transporte 
        print("Auxilio de transporte: {0}".format(estados[emi]))

    def estado8(self):
        estados = ["1.500.000", "2.000.000", "3.000.000", "2.500.000"]
        emi= randint(0,len(estados) -1)                   # funcion con randint sueldo neto devengado
        print("Sueldo Neto devengado: {0}".format(estados[emi]))

    def estado9(self):
        estados = ["1 millon", "2 millones", "3 millones", "4 millones"]
        emi= randint(0,len(estados) -1)             # funcion con randint para liquidacion por un año de trabajo 
        print("Liquidacion por año de trabajo: {0}".format(estados[emi]))

    def estado10(self):
        estados = ["12 millones", "10 millones", "20 millones", "42 millones"]
        emi= randint(0,len(estados) -1)  # funcion con randint para liquidacion por todos los años de trabajo 
        print("Liquidacion del Prestador de Servicios por todos los años laborados : {0}".format(estados[emi]))

#----------------------PLANTA-------------------------------------

class Planta (Administrativos):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
    genero = "", estrato = "", dependencia = "", titulo = "", fechaVinculacion =""):  #Creacion del constructor y sus argumentos 

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo)
           # Definicion de los self de los argumentos que hereda de la super clase persona


        self.__fechaVinculacion = fechaVinculacion  # Definicion self de los argumentos nuevos
       

    def set_fechaVinculacion(self, value):  # Defino set fechaVinculacion
        self.__fechaVinculacion = value


    def get_fechaVinculacion(self):     # Defino get fechaVinculacion
        return self.__fechaVinculacion


#----------------------AUXILIAR------------------------------------- 

class Auxiliar (Planta):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
    genero = "", estrato = "", dependencia = "", titulo = "", fechaVinculacion ="", nivel = "", salario = ""):#Creacion del constructor y sus argumentos

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo, fechaVinculacion,)
        # Definicion de los self de los argumentos que hereda de la super clase persona


        self.__nivel = nivel    # Definicion self de los argumentos nuevos
        self.__salario = salario


    def set_nivel(self, value): # Defino set nivel
        self.__nivel = value


    def get_nivel(self):    # Defino get nivel
        return self.__nivel


    def set_salario(self, value): # Defino set salario
        self.__salario = value


    def get_salario(self):  # Defino get salario
        return self.__salario



    def leer_datos(self):
        print("___________INGRESO DE DATOS________________")
        self.set_idPersona (Fun.control_numeros_letras("Digite el ID de la persona: "))  # input id persona
        self.set_nomPersona (Fun.control_letras("Digite el nombre: ")) # input nom persona
        self.set_apePersona (Fun.control_letras("Digite el apellido: "))  # input apellido
        self.set_fechaNacimiento (Fun.control_numeros_letras("Digite la fecha de nacimiento: "))  # input fecha nacimiento
        self.set_ciudadNacimiento (Fun.control_letras("Escriba la ciudad de nacimiento: ")) # input lugar nacimiento 
        self.set_genero (Fun.control_letras("Digite el genero de la persona: ")) # input genero persona
        self.set_estrato(Fun.control_numeros("Digite el estrato socioeconomico: "))  # input estrato docente 
        self.set_dependencia (Fun.control_letras("Digite la dependencia donde labora el auxiliar: "))  # input dependencia
        self.set_titulo (Fun.control_letras("Digite el titulo academico del auxiliar: ")) # input titulo
        self.set_fechaVinculacion (Fun.control_letras("Digite la fecha de vinculacion del auxiliar: ")) # input fecha de vinculacion
        self.set_nivel (Fun.control_numeros("Evalue su nivel de desempeño laboral de 1 a 5: ")) # input nivel de desempeño
        self.set_salario(Fun.control_numeros("Digite el salario basico mensual recibido: ")) # input salario


    def informacion_Imprimir_Datos(self):

        print("---------DATOS INGRESADOS------------\n"
        "ID personal: {0}\n" 
        "Nombre :  {1}\n" 
        "Apellido : {2}\n" 
        "Fecha de nacimiento: {3}\n"                    # Datos ingresados por el usuario en los inputs
        "Ciudad de nacimiento : {4}\n"
        "Genero de la persona: {5}\n"
        "Estrato socio-economico:{6}\n" 
        "La dependencia donde labora el auxiliar es :{7}\n"
        "Titulo academico del auxiliar :{8}\n"
        "La fecha de vinculacio del auxiliar es: {9}\n"
        "El nivel de desempeño laboral del auxiliar: {10}\n"
        "Valor del salario neto del auxiliar es: {11}". format( self.get_idPersona(), self.get_nomPersona(), self.get_apePersona (), 
        self.get_fechaNacimiento(), self.get_ciudadNacimiento(), self.get_genero(), self.get_estrato() , self.get_dependencia(), 
        self.get_titulo(), self.get_fechaVinculacion(), self.get_nivel(), self.get_salario(), end =""))
        # Con los self get llamamos los datos para la impresion.



    def estado1(self):
        estados = ["En DG1", "En DG2", "En DG3", "En DG4"] # funcion con randit para mostrar los datos 
        emi= randint(0,len(estados) -1)
        print("Aporte DG : {0}".format(estados[emi]))


    def estado2(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                 # funcion con randit para mostrar aportes  EPS
        print("Aporte de EPS : {0}".format(estados[emi]))


    def estado3(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                 # funcion con randint para mostrar aporte pension
        print("Aporte de PENSION: {0}".format(estados[emi]))


    def estado31(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                  # funcion con randint para mostrar aportes ARL
        print("Aporte de ARL: {0}".format(estados[emi]))

    def estado4(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)              # funcion con randint para mostrar aportes SENA
        print("Parafiscal SENA: {0}".format(estados[emi]))

    def estado5(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                  # funcion con randint  aportes caja compensacion 
        print("Valor aporte caja de compensacion : {0}".format(estados[emi]))

    def estado6(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                 # funcion con randint para mostrar  parafiscal ICBF
        print("Parafiscal ICBF: {0}".format(estados[emi]))

    def estado7(self):
        estados = ["120mil", "100mil", "150mil", "115mil"]
        emi= randint(0,len(estados) -1)                 # funcion con randint para mostrar auxilio transporte
        print("Auxilio de transporte: {0}".format(estados[emi]))

    def estado8(self):
        estados = ["1.500.000", "2.000.000", "3.000.000", "2.500.000"]
        emi= randint(0,len(estados) -1)                   # funcion con randint sueldo neto devengado
        print("Sueldo Neto devengado: {0}".format(estados[emi]))

    def estado9(self):
        estados = ["1 millon", "2 millones", "3 millones", "4 millones"]
        emi= randint(0,len(estados) -1)                # funcion con randint para liquidacion por un año de trabajo 
        print("Liquidacion por año de trabajo: {0}".format(estados[emi]))

    def estado10(self):
        estados = ["12 millones", "10 millones", "20 millones", "42 millones"]
        emi= randint(0,len(estados) -1)# funcion con randint para liquidacion por todos los años de trabajo 
        print("Liquidacion Auxiliar administrativo por todos los años laborados : {0}".format(estados[emi]))

#----------------------ADMINISTRATIVOS-------------------------------------

class Tecnico (Planta):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
    genero = "", estrato = "", dependencia ="", titulo="", fechaVinculacion ="", nivel = "", salario = ""): #Creacion del constructor y sus argumentos

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo, fechaVinculacion)
         # Definicion de los self de los argumentos que hereda de la super clase persona


        self.__nivel = nivel         # Definicion self de los argumentos nuevos
        self.__salario = salario


    def set_nivel(self, value): # Defino set nivel
        self.__nivel = value


    def get_nivel(self): # Definir get nivel
        return self.__nivel


    def set_salario(self, value): # Definir set salario
        self.__salario = value


    def get_salario(self): # Definir get salario
        return self.__salario


    def leer_datos(self):
        print("___________INGRESO DE DATOS________________")
        self.set_idPersona (Fun.control_numeros_letras("Digite el ID de la persona: ")) # input id persona
        self.set_nomPersona (Fun.control_letras("Digite el nombre: ")) # input nom persona
        self.set_apePersona (Fun.control_letras("Digite el apellido: "))  # input apellido
        self.set_fechaNacimiento (Fun.control_numeros_letras("Digite la fecha de nacimiento: ")) # input fecha nacimiento
        self.set_ciudadNacimiento (Fun.control_letras("Escriba la ciudad de nacimiento: "))  # input lugar nacimiento 
        self.set_genero (Fun.control_letras("Digite el genero de la persona: ")) # input genero persona
        self.set_estrato(Fun.control_numeros("Digite el estrato socioeconomico: "))  # input estrato docente 
        self.set_dependencia (Fun.control_letras("Digite la dependencia donde labora el tecnico: ")) # input dependencia
        self.set_titulo (Fun.control_letras("Digite el titulo academico del tecnico: "))  # input titulo
        self.set_fechaVinculacion (Fun.control_letras("Digite la fecha de vinculacion del tecnico: ")) # input fecha de vinculacion
        self.set_nivel (Fun.control_numeros("Evalue su nivel de desempeño laboral de 1 a 5: ")) # input nivel de desempeño
        self.set_salario(Fun.control_numeros("Digite el salario basico mensual recibido: "))  # input salario


    def informacion_Imprimir_Datos(self):

        print("---------DATOS INGRESADOS------------\n"
        "ID personal: {0}\n" 
        "Nombre :  {1}\n" 
        "Apellido : {2}\n" 
        "Fecha de nacimiento: {3}\n"
        "Ciudad de nacimiento : {4}\n"                   # Datos ingresados por el usuario en los inputs
        "Genero de la persona: {5}\n"
        "Estrato socio-economico:{6}\n" 
        "La dependencia donde labora el tecnico es :{7}\n"
        "Titulo academico del tecnico :{8}\n"
        "La fecha de vinculacio del tecnico es: {9}\n"
        "El nivel de desempeño laboral del tecnico: {10}\n"
        "Valor del salario neto del tecnico es: {11}". format( self.get_idPersona(), self.get_nomPersona(), self.get_apePersona (), 
        self.get_fechaNacimiento(), self.get_ciudadNacimiento(), self.get_genero(), self.get_estrato() , self.get_dependencia(), 
        self.get_titulo(), self.get_fechaVinculacion(), self.get_nivel(), self.get_salario(), end =""))


    def estado1(self):
        estados = ["En DG1", "En DG2", "En DG3", "En DG4"] # funcion con randit para mostrar los datos 
        emi= randint(0,len(estados) -1)
        print("Aporte DG : {0}".format(estados[emi]))


    def estado2(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                  # funcion con randit para mostrar aportes  EPS
        print("Aporte de EPS : {0}".format(estados[emi]))


    def estado3(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)             # funcion con randint para mostrar aporte pension
        print("Aporte de PENSION: {0}".format(estados[emi]))


    def estado31(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)      # funcion con randint para mostrar aportes ARL
        print("Aporte de ARL: {0}".format(estados[emi]))

    def estado4(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                 # funcion con randint para mostrar aportes SENA
        print("Parafiscal SENA: {0}".format(estados[emi]))

    def estado5(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)              # funcion con randint  aportes caja compensacion 
        print("Valor aporte caja de compensacion : {0}".format(estados[emi]))

    def estado6(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)           # funcion con randint para mostrar  parafiscal ICBF
        print("Parafiscal ICBF: {0}".format(estados[emi]))

    def estado7(self):
        estados = ["120mil", "100mil", "150mil", "115mil"]
        emi= randint(0,len(estados) -1)         # funcion con randint para mostrar auxilio transporte
        print("Auxilio de transporte: {0}".format(estados[emi]))

    def estado8(self):
        estados = ["1.500.000", "2.000.000", "3.000.000", "2.500.000"]
        emi= randint(0,len(estados) -1)          # funcion con randint sueldo neto devengado
        print("Sueldo Neto devengado: {0}".format(estados[emi]))

    def estado9(self):
        estados = ["1 millon", "2 millones", "3 millones", "4 millones"]
        emi= randint(0,len(estados) -1)      # funcion con randint para liquidacion por un año de trabajo 
        print("Liquidacion por año de trabajo: {0}".format(estados[emi]))

    def estado10(self):
        estados = ["12 millones", "10 millones", "20 millones", "42 millones"]
        emi= randint(0,len(estados) -1) # funcion con randint para liquidacion por todos los años de trabajo 
        print("Liquidacion tecnico administrativo por todos los años laborados : {0}".format(estados[emi]))


#----------------------PROFESIONAL-------------------------------------

class Profesional (Planta):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
    genero = "", estrato = "", dependencia = "", titulo = "", fechaVinculacion ="", nivel="",  salario=""): #Creacion del constructor y sus argumentos

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo, fechaVinculacion)
        # Definicion de los self de los argumentos que hereda de la super clase persona


        self.__nivel = nivel  # Definicion self de los argumentos nuevos
        self.__salario = salario


    def set_nivel(self, value): # Defino set nivel
        self.__nivel = value


    def get_nivel(self):      # Defino get nivel 
        return self.__nivel


    def set_salario(self, value): # Defino set salario
        self.__salario = value


    def get_salario(self):  # Defino get salario
        return self.__salario

    def leer_datos(self):
        print("___________INGRESO DE DATOS________________")
        self.set_idPersona (Fun.control_numeros_letras("Digite el ID de la persona: ")) # input id persona
        self.set_nomPersona (Fun.control_letras("Digite el nombre: ")) # input nom persona
        self.set_apePersona (Fun.control_letras("Digite el apellido: ")) # input apellido
        self.set_fechaNacimiento (Fun.control_numeros_letras("Digite la fecha de nacimiento: "))  # input fecha nacimiento
        self.set_ciudadNacimiento (Fun.control_letras("Escriba la ciudad de nacimiento: "))  # input lugar nacimiento 
        self.set_genero (Fun.control_letras("Digite el genero de la persona: ")) # input genero persona
        self.set_estrato(Fun.control_numeros("Digite el estrato socioeconomico: "))  # input estrato docente 
        self.set_dependencia (Fun.control_letras("Digite la dependencia donde labora el profesional: ")) # input dependencia
        self.set_titulo (Fun.control_letras("Digite el titulo academico del profesional: ")) # input titulo
        self.set_fechaVinculacion (Fun.control_letras("Digite la fecha de vinculacion del profesional: ")) # input fecha de vinculacion
        self.set_nivel (Fun.control_numeros("Evalue su nivel de desempeño laboral de 1 a 5: ")) # input nivel de desempeño
        self.set_salario(Fun.control_numeros("Digite el salario basico mensual recibido: "))  # input salario


    def informacion_Imprimir_Datos(self):

        print("---------DATOS INGRESADOS------------\n"
        "ID personal: {0}\n" 
        "Nombre :  {1}\n" 
        "Apellido : {2}\n" 
        "Fecha de nacimiento: {3}\n"              # Datos ingresados por el usuario en los inputs
        "Ciudad de nacimiento : {4}\n"      
        "Genero de la persona: {5}\n"
        "Estrato socio-economico:{6}\n" 
        "La dependencia donde labora el profesional es :{7}\n"
        "Titulo academico del profesional :{8}\n"
        "La fecha de vinculacio del profesional es: {9}\n"
        "El nivel de desempeño laboral del profesional: {10}\n"
        "Valor del salario neto del profesional es: {11}". format( self.get_idPersona(), self.get_nomPersona(), self.get_apePersona (), 
        self.get_fechaNacimiento(), self.get_ciudadNacimiento(), self.get_genero(), self.get_estrato() , self.get_dependencia(), 
        self.get_titulo(), self.get_fechaVinculacion(), self.get_nivel(), self.get_salario(), end =""))


    def estado1(self):
        estados = ["En DG1", "En DG2", "En DG3", "En DG4"] # funcion con randit para mostrar los datos
        emi= randint(0,len(estados) -1)
        print("Aporte DG : {0}".format(estados[emi]))


    def estado2(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                     # funcion con randit para mostrar aportes  EPS
        print("Aporte de EPS : {0}".format(estados[emi]))


    def estado3(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                 # funcion con randint para mostrar aporte pension
        print("Aporte de PENSION: {0}".format(estados[emi]))


    def estado31(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)             # funcion con randint para mostrar aportes ARL
        print("Aporte de ARL: {0}".format(estados[emi]))

    def estado4(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)             # funcion con randint para mostrar aportes SENA
        print("Parafiscal SENA: {0}".format(estados[emi]))

    def estado5(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)                 # funcion con randint  aportes caja compensacion 
        print("Valor aporte caja de compensacion : {0}".format(estados[emi]))

    def estado6(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)         # funcion con randint para mostrar  parafiscal ICBF
        print("Parafiscal ICBF: {0}".format(estados[emi]))

    def estado7(self):
        estados = ["120mil", "100mil", "150mil", "115mil"]
        emi= randint(0,len(estados) -1)                  # funcion con randint para mostrar auxilio transporte
        print("Auxilio de transporte: {0}".format(estados[emi]))

    def estado8(self):
        estados = ["1.500.000", "2.000.000", "3.000.000", "2.500.000"]
        emi= randint(0,len(estados) -1)                  # funcion con randint sueldo neto devengado
        print("Sueldo Neto devengado: {0}".format(estados[emi]))

    def estado9(self):
        estados = ["1 millon", "2 millones", "3 millones", "4 millones"]
        emi= randint(0,len(estados) -1)                     # funcion con randint para liquidacion por un año de trabajo 
        print("Liquidacion por año de trabajo: {0}".format(estados[emi]))

    def estado10(self):
        estados = ["12 millones", "10 millones", "20 millones", "42 millones"]
        emi= randint(0,len(estados) -1) # funcion con randint para liquidacion por todos los años de trabajo 
        print("Liquidacion tecnico administrativo por todos los años laborados : {0}".format(estados[emi]))  


#----------------------FIN ARBOL ------------------------------------- 