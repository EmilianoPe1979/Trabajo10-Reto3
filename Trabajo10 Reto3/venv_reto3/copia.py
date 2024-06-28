#***************************************#
# CENTRO DE BIOTECNOLOGIA AGROPECUARIA  #
# NOMBRE EMILIANO PERILLA AGUILAR       #
# VERSION : 4.0                         #
# Fecha: 09/06/2024                     #
#***************************************#

#Este programa se encuentra diseñado par demostrar la funcionalidad que resulta 
# del correcto manejo del POP, mediante super clases, subclases y clases logramos
# crear y modificar los atributos y metodos de un objeto. Super clase persona, subclases
# docentes, administrativos y clases tiempo completo, ocacionales,
# hora catedra, planta,OPS, auxiliar, tecnico, profesional 


from random import randint 
from modules import functions as Fun

#----------------------------PERSONA--------------------------
class Persona: # Definicion de la superclase 

    def __init__(self, idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato): # Definicion de la superclase 
        
        self.__idPersona = idPersona   # Definicion self de los argumentos             
        self.__nomPersona = nomPersona
        self.__apePersona = apePersona
        self.__fechaNacimiento = fechaNacimiento 
        self.__ciudadNacimiento = ciudadNacimiento 
        self.__genero = genero 
        self.__estrato = estrato  
       

    def set_idPersona(self, value): # Funcion que define el set del 
        self.__idPersona = value
    

    def get_idPersona(self):  # Funcion que define el get del      
        return self.__idPersona
    

    def set_nomPersona(self, value): 
        self.__nomPersona = value


    def get_nomPersona(self):   
        return self.__nomPersona


    def set_apePersona(self, value): 
        self.__apePersona = value


    def get_apePersona(self):   
        return self.__apePersona


    def set_fechaNacimiento(self, value): 
        self.__fechaNacimiento = value


    def get_fechaNacimiento(self):   
        return self.__fechaNacimiento

    
    def set_ciudadNacimiento(self, value): 
        self.__ciudadNacimiento = value


    def get_ciudadNacimiento(self):   
        return self.__ciudadNacimiento


    def set_genero(self, value): 
        self.__genero = value


    def get_genero(self):   
        return self.__genero


    def set_estrato(self, value): 
        self.__estrato = value


    def get_estrato(self):   
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
   

    def set_areaFormacion(self, value):  # Define el set del argumento de  
        self.__areaFormacion = value


    def get_areaFormacion(self):        # Define el get del argumento de 
        return self.__areaFormacion


    def set_tituloProfesional(self, value):  # Define el set del argumento de 
        self.__tituloProfesional = value


    def get_tituloProfesional(self):      # Define el get del argumento de 
        return self.__tituloProfesional


    def set_unidadAcademica(self, value):
        self.__unidadAcademica = value

    def get_unidadAcademica(self):
        return self.__unidadAcademica 

#----------------------TIEMPO COMPLETO -------------------------------------

class TiempoCompleto (Docentes):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "", 
    genero = "", estrato = "", areaFormacion ="", tituloProfesional ="", unidadAcademica = "", categoria = "", puntos = "" 
    , salario = ""):

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, 
        areaFormacion, tituloProfesional, unidadAcademica)
        # Definicion de los self de los argumentos que hereda de la super clase persona
        
        self.__categoria = categoria   
        self.__puntos = puntos # Definicion self de los argumentos nuevos
        self.__salario = salario


    def set_categoria(self, value):
        self.__categoria = value


    def get_categoria(self):
        return self.__categoria


    def set_puntos(self, value):
        self.__puntos = value


    def get_puntos(self):
        return self.__puntos

    
    def set_salario(self, value):
        self.__salario = value


    def get_salario(self):
        return self.__salario


    def leer_datos(self):

        print("___________INGRESO DE DATOS________________")
        self.set_idPersona (Fun.control_numeros_letras("Digite el ID de la persona: "))
        self.set_nomPersona (Fun.control_letras("Digite el nombre: "))
        self.set_apePersona (Fun.control_letras("Digite el apellido: "))
        self.set_fechaNacimiento (Fun.control_numeros_letras("Digite la fecha de nacimiento: "))
        self.set_ciudadNacimiento (Fun.control_letras("Escriba la ciudad de nacimiento: "))
        self.set_genero (Fun.control_letras("Digite el genero de la persona: "))
        self.set_estrato(Fun.control_numeros("Digite el estrato del docente: ")) 
        self.set_areaFormacion (Fun.control_letras("Digite el area de formacion del docente: "))
        self.set_tituloProfesional (Fun.control_letras("Digite el titulo profesional del docente: "))
        self.set_unidadAcademica (Fun.control_letras("Digite la unidad academica del docente: "))
        self.set_categoria (Fun.control_letras("Digite la categoria del docente: "))
        self.set_puntos (Fun.control_numeros("Digite la cantidad de puntos del docente: "))
        self.set_salario(Fun.control_numeros("Digite el salario del docente: ")) 
    # Funcion para el ingreso de datos de la clase 


    def informacion_Imprimir_Datos(self):

        print("---------DATOS INGRESADOS------------\n"
        "ID personal: {0}\n" 
        "Nombre :  {1}\n" 
        "Apellido : {2}\n" 
        "Fecha de nacimiento: {3}\n"
        "Ciudad de nacimiento : {4}\n"
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

    def estado1(self):
        estados = ["En DG1", "En DG2", "En DG3", "En DG4"]
        emi= randint(0,len(estados) -1)
        print("Aporte DG : {0}".format(estados[emi]))

    def estado2(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de EPS : {0}".format(estados[emi]))

    def estado3(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de PENSION: {0}".format(estados[emi]))


    def estado31(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de ARL: {0}".format(estados[emi]))

    def estado4(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Parafiscal SENA: {0}".format(estados[emi]))

    def estado5(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Valor aporte caja de compensacion : {0}".format(estados[emi]))

    def estado6(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Parafiscal ICBF: {0}".format(estados[emi]))

    def estado7(self):
        estados = ["120mil", "100mil", "150mil", "115mil"]
        emi= randint(0,len(estados) -1)
        print("Auxilio de transporte: {0}".format(estados[emi]))

    def estado8(self):
        estados = ["1.500.000", "2.000.000", "3.000.000", "2.500.000"]
        emi= randint(0,len(estados) -1)
        print("Sueldo Neto devengado: {0}".format(estados[emi]))

    def estado9(self):
        estados = ["12 millones", "10 millones", "20 millones", "42 millones"]
        emi= randint(0,len(estados) -1)
        print("Liquidacion Tiempo completo : {0}".format(estados[emi]))

    # Funcion para definir el estado de la revista (publicaion/impresion/diagramacion)

#----------------------OCASIONALES -------------------------------------

class Ocasionales (Docentes):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
     genero = "", estrato = "", areaFormacion ="", tituloProfesional ="", unidadAcademica = "", ultimoTitulo = "", numMeses = "" 
     , salario = ""):

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, 
        areaFormacion, tituloProfesional, unidadAcademica)
        # Definicion de los self de los argumentos que hereda de la super clase persona
        
        self.__ultimoTitulo = ultimoTitulo 
        self.__numMeses = numMeses # Definicion self de los argumentos nuevos
        self.__salario = salario


    def set_ultimoTitulo(self, value):
        self.__ultimoTitulo = value


    def get_ultimoTitulo(self):
        return self.__ultimoTitulo


    def set_numMeses(self, value):
        self.__numMeses = value


    def get_numMeses(self):
        return self.__numMeses

    
    def set_salario(self, value):
        self.__salario = value


    def get_salario(self):
        return self.__salario


    def leer_datos(self):

        print("___________INGRESO DE DATOS________________")
        self.set_idPersona (Fun.control_numeros_letras("Digite el ID de la persona: "))
        self.set_nomPersona (Fun.control_letras("Digite el nombre: "))
        self.set_apePersona (Fun.control_letras("Digite el apellido: "))
        self.set_fechaNacimiento (Fun.control_numeros_letras("Digite la fecha de nacimiento: "))
        self.set_ciudadNacimiento (Fun.control_letras("Escriba la ciudad de nacimiento: "))
        self.set_genero (Fun.control_letras("Digite el genero de la persona: "))
        self.set_estrato(Fun.control_numeros("Digite el estrato del docente: ")) 
        self.set_areaFormacion (Fun.control_letras("Digite el area de formacion del docente: "))
        self.set_tituloProfesional (Fun.control_letras("Digite el titulo profesional del docente: "))
        self.set_unidadAcademica (Fun.control_letras("Digite la unidad academica del docente: "))
        self.set_ultimoTitulo (Fun.control_letras("Digite el ultimo titulo obtenido: "))
        self.set_numMeses (Fun.control_numeros("Digite la cantidad de meses trabajados: "))
        self.set_salario(Fun.control_numeros("Digite el salario del docente: ")) 


    def informacion_Imprimir_Datos(self):

        print("---------DATOS INGRESADOS------------\n"
        "ID personal: {0}\n" 
        "Nombre :  {1}\n" 
        "Apellido : {2}\n" 
        "Fecha de nacimiento: {3}\n"
        "Ciudad de nacimiento : {4}\n"
        "Genero de la persona: {5}\n"
        "Estrato socio-economico:{6}\n" 
        "Area de formacion del docente es:{7}\n"
        "Titulo profesional del docente es:{8}\n"
        "Unidad academica es: {9}\n"
        "El ultimo titulo del docente es: {10}\n"
        "Cantidad de meses de trabajo del docente es: {11}\n"
        "Salario basico del docente es: {12}". format( self.get_idPersona(), self.get_nomPersona(), self.get_apePersona (), 
        self.get_fechaNacimiento(), self.get_ciudadNacimiento(), self.get_genero(), self.get_estrato() , self.get_areaFormacion(), 
        self.get_tituloProfesional(), self.get_unidadAcademica(), self.get_ultimoTitulo(), self.get_numMeses(), self.get_salario() ,end =""))

    def estado1(self):
        estados = ["En DG1", "En DG2", "En DG3", "En DG4"]
        emi= randint(0,len(estados) -1)
        print("Aporte DG : {0}".format(estados[emi]))

    def estado2(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de EPS : {0}".format(estados[emi]))

    def estado3(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de PENSION: {0}".format(estados[emi]))


    def estado31(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de ARL: {0}".format(estados[emi]))

    def estado4(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Parafiscal SENA: {0}".format(estados[emi]))

    def estado5(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Valor aporte caja de compensacion : {0}".format(estados[emi]))

    def estado6(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Parafiscal ICBF: {0}".format(estados[emi]))

    def estado7(self):
        estados = ["120mil", "100mil", "150mil", "115mil"]
        emi= randint(0,len(estados) -1)
        print("Auxilio de transporte: {0}".format(estados[emi]))

    def estado8(self):
        estados = ["1.500.000", "2.000.000", "3.000.000", "2.500.000"]
        emi= randint(0,len(estados) -1)
        print("Sueldo Neto devengado: {0}".format(estados[emi]))

    def estado9(self):
        estados = ["12 millones", "10 millones", "20 millones", "42 millones"]
        emi= randint(0,len(estados) -1)
        print("Liquidacion Tiempo completo : {0}".format(estados[emi]))

#----------------------HORA CATEDRA-------------------------------------

class HoraCatedra (Docentes):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
    genero = "", estrato = "", areaFormacion ="", tituloProfesional ="", unidadAcademica = "", ultimoTitulo = "", numHoras = "" 
    ,ValorContrato = "", salario = ""):

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, 
        areaFormacion, tituloProfesional, unidadAcademica)
        # Definicion de los self de los argumentos que hereda de la super clase persona
        
        self.__ultimoTitulo = ultimoTitulo 
        self.__numHoras = numHoras
        self.__valorContrato = ValorContrato # Definicion self de los argumentos nuevos
        self.__salario = salario

    def set_ultimoTitulo(self, value):
        self.__ultimoTitulo = value


    def get_ultimoTitulo(self):
        return self.__ultimoTitulo


    def set_numHoras(self, value):
        self.__numHoras = value


    def get_numHoras(self):
        return self.__numHoras


    def set_valorContrato(self, value):
        self.__valorContrato = value


    def get_valorContrato(self):
        return self.__valorContrato

    
    def set_salario(self, value):
        self.__salario = value


    def get_salario(self):
        return self.__salario

    def leer_datos(self):

        print("___________INGRESO DE DATOS________________")
        self.set_idPersona (Fun.control_numeros_letras("Digite el ID de la persona: "))
        self.set_nomPersona (Fun.control_letras("Digite el nombre: "))
        self.set_apePersona (Fun.control_letras("Digite el apellido: "))
        self.set_fechaNacimiento (Fun.control_numeros_letras("Digite la fecha de nacimiento: "))
        self.set_ciudadNacimiento (Fun.control_letras("Escriba la ciudad de nacimiento: "))
        self.set_genero (Fun.control_letras("Digite el genero de la persona: "))
        self.set_estrato(Fun.control_numeros("Digite el estrato del docente: ")) 
        self.set_areaFormacion (Fun.control_letras("Digite el area de formacion del docente: "))
        self.set_tituloProfesional (Fun.control_letras("Digite el titulo profesional del docente: "))
        self.set_unidadAcademica (Fun.control_letras("Digite la unidad academica del docente: "))
        self.set_ultimoTitulo (Fun.control_letras("Digite el ultimo titulo obtenido: "))
        self.set_numHoras (Fun.control_numeros("Digite la cantidad de horas catedras dictadas: "))
        self.set_valorContrato (Fun.control_numeros("Digite el valor global neto del contrato acordado: "))
        self.set_salario(Fun.control_numeros("Digite el salario basico sin horas catedra del docente: ")) 


    def informacion_Imprimir_Datos(self):

        print("---------DATOS INGRESADOS------------\n"
        "ID personal: {0}\n" 
        "Nombre :  {1}\n" 
        "Apellido : {2}\n" 
        "Fecha de nacimiento: {3}\n"
        "Ciudad de nacimiento : {4}\n"
        "Genero de la persona: {5}\n"
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


    def estado1(self):
        estados = ["En DG1", "En DG2", "En DG3", "En DG4"]
        emi= randint(0,len(estados) -1)
        print("Aporte DG : {0}".format(estados[emi]))


    def estado2(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de EPS : {0}".format(estados[emi]))


    def estado3(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de PENSION: {0}".format(estados[emi]))


    def estado31(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de ARL: {0}".format(estados[emi]))

    def estado4(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Parafiscal SENA: {0}".format(estados[emi]))

    def estado5(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Valor aporte caja de compensacion : {0}".format(estados[emi]))

    def estado6(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Parafiscal ICBF: {0}".format(estados[emi]))

    def estado7(self):
        estados = ["120mil", "100mil", "150mil", "115mil"]
        emi= randint(0,len(estados) -1)
        print("Auxilio de transporte: {0}".format(estados[emi]))

    def estado8(self):
        estados = ["1.500.000", "2.000.000", "3.000.000", "2.500.000"]
        emi= randint(0,len(estados) -1)
        print("Sueldo Neto devengado: {0}".format(estados[emi]))

    def estado9(self):
        estados = ["12 millones", "10 millones", "20 millones", "42 millones"]
        emi= randint(0,len(estados) -1)
        print("Liquidacion Tiempo completo : {0}".format(estados[emi]))

#----------------------ADMINISTRATIVOS-------------------------------------

class Administrativos (Persona):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
    genero = "", estrato = "", dependencia ="", titulo=""):

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato)

        self.__dependencia = dependencia 
        self.__titulo = titulo

    def set_dependencia(self, value):
        self.__dependencia = value


    def get_dependencia(self):
        return self.__dependencia


    def set_titulo(self, value):
        self.__titulo = value


    def get_titulo(self):
        return self.__titulo

#----------------------OPS-------------------------------------

class OPS (Administrativos):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
    genero = "", estrato = "", dependencia = "", titulo = "", fechaVinculacion ="", numMeses="", ValorContrato ="", salario=""):

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo)

        self.__fechaVinculacion = fechaVinculacion 
        self.__numMeses = numMeses
        self.__valorContrato = ValorContrato
        self.__salario = salario


    def set_fechaVinculacion(self, value):
        self.__fechaVinculacion = value


    def get_fechaVinculacion(self):
        return self.__fechaVinculacion


    def set_numMeses(self, value):
        self.__numMeses = value


    def get_numMeses(self):
        return self.__numMeses


    def set_valorContrato(self, value):
        self.__valorContrato = value


    def get_valorContrato(self):
        return self.__valorContrato


    def set_salario(self, value):
        self.__salario = value


    def get_salario(self):
        return self.__salario


    def leer_datos(self):
        print("___________INGRESO DE DATOS________________")
        self.set_idPersona (Fun.control_numeros_letras("Digite el ID de la persona: "))
        self.set_nomPersona (Fun.control_letras("Digite el nombre: "))
        self.set_apePersona (Fun.control_letras("Digite el apellido: "))
        self.set_fechaNacimiento (Fun.control_numeros_letras("Digite la fecha de nacimiento: "))
        self.set_ciudadNacimiento (Fun.control_letras("Escriba la ciudad de nacimiento: "))
        self.set_genero (Fun.control_letras("Digite el genero de la persona: "))
        self.set_estrato(Fun.control_numeros("Digite el estrato socioeconomico: ")) 
        self.set_dependencia (Fun.control_letras("Digite la dependencia donde labora el OPS: "))
        self.set_titulo (Fun.control_letras("Digite el titulo academico del OPS: "))
        self.set_fechaVinculacion (Fun.control_letras("Digite la fecha de vinculacion del OPS: "))
        self.set_numMeses (Fun.control_numeros("Digite el numero de meses del contrato del prestador de servicios: "))
        self.set_valorContrato (Fun.control_numeros("Digite el valor global total del contrato acordado: "))
        self.set_salario(Fun.control_numeros("Digite el salario basico acordado para el OPS: ")) 
        

    def informacion_Imprimir_Datos(self):

        print("---------DATOS INGRESADOS------------\n"
        "ID personal: {0}\n" 
        "Nombre :  {1}\n" 
        "Apellido : {2}\n" 
        "Fecha de nacimiento: {3}\n"
        "Ciudad de nacimiento : {4}\n"
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


    def estado1(self):
        estados = ["En DG1", "En DG2", "En DG3", "En DG4"]
        emi= randint(0,len(estados) -1)
        print("Aporte DG : {0}".format(estados[emi]))


    def estado2(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de EPS : {0}".format(estados[emi]))


    def estado3(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de PENSION: {0}".format(estados[emi]))


    def estado31(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de ARL: {0}".format(estados[emi]))

    def estado4(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Parafiscal SENA: {0}".format(estados[emi]))

    def estado5(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Valor aporte caja de compensacion : {0}".format(estados[emi]))

    def estado6(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Parafiscal ICBF: {0}".format(estados[emi]))

    def estado7(self):
        estados = ["120mil", "100mil", "150mil", "115mil"]
        emi= randint(0,len(estados) -1)
        print("Auxilio de transporte: {0}".format(estados[emi]))

    def estado8(self):
        estados = ["1.500.000", "2.000.000", "3.000.000", "2.500.000"]
        emi= randint(0,len(estados) -1)
        print("Sueldo Neto devengado: {0}".format(estados[emi]))

    def estado9(self):
        estados = ["1 millon", "2 millones", "3 millones", "4 millones"]
        emi= randint(0,len(estados) -1)
        print("Liquidacion por año de trabajo: {0}".format(estados[emi]))

    def estado10(self):
        estados = ["12 millones", "10 millones", "20 millones", "42 millones"]
        emi= randint(0,len(estados) -1)
        print("Liquidacion del Prestador de Servicios por todos los años laborados : {0}".format(estados[emi]))

#----------------------PLANTA-------------------------------------

class Planta (Administrativos):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
    genero = "", estrato = "", dependencia = "", titulo = "", fechaVinculacion =""):

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo)

        self.__fechaVinculacion = fechaVinculacion 
       

    def set_fechaVinculacion(self, value):
        self.__fechaVinculacion = value


    def get_fechaVinculacion(self):
        return self.__fechaVinculacion


#----------------------AUXILIAR------------------------------------- 

class Auxiliar (Planta):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
    genero = "", estrato = "", dependencia = "", titulo = "", fechaVinculacion ="", nivel = "", salario = ""):

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo, fechaVinculacion,)

        self.__nivel = nivel 
        self.__salario = salario


    def set_nivel(self, value):
        self.__nivel = value


    def get_nivel(self):
        return self.__nivel


    def set_salario(self, value):
        self.__salario = value


    def get_salario(self):
        return self.__salario



    def leer_datos(self):
        print("___________INGRESO DE DATOS________________")
        self.set_idPersona (Fun.control_numeros_letras("Digite el ID de la persona: "))
        self.set_nomPersona (Fun.control_letras("Digite el nombre: "))
        self.set_apePersona (Fun.control_letras("Digite el apellido: "))
        self.set_fechaNacimiento (Fun.control_numeros_letras("Digite la fecha de nacimiento: "))
        self.set_ciudadNacimiento (Fun.control_letras("Escriba la ciudad de nacimiento: "))
        self.set_genero (Fun.control_letras("Digite el genero de la persona: "))
        self.set_estrato(Fun.control_numeros("Digite el estrato socioeconomico: ")) 
        self.set_dependencia (Fun.control_letras("Digite la dependencia donde labora el auxiliar: "))
        self.set_titulo (Fun.control_letras("Digite el titulo academico del auxiliar: "))
        self.set_fechaVinculacion (Fun.control_letras("Digite la fecha de vinculacion del auxiliar: "))
        self.set_nivel (Fun.control_numeros("Evalue su nivel de desempeño laboral de 1 a 5: "))
        self.set_salario(Fun.control_numeros("Digite el salario basico mensual recibido: ")) 


    def informacion_Imprimir_Datos(self):

        print("---------DATOS INGRESADOS------------\n"
        "ID personal: {0}\n" 
        "Nombre :  {1}\n" 
        "Apellido : {2}\n" 
        "Fecha de nacimiento: {3}\n"
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


    def estado1(self):
        estados = ["En DG1", "En DG2", "En DG3", "En DG4"]
        emi= randint(0,len(estados) -1)
        print("Aporte DG : {0}".format(estados[emi]))


    def estado2(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de EPS : {0}".format(estados[emi]))


    def estado3(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de PENSION: {0}".format(estados[emi]))


    def estado31(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de ARL: {0}".format(estados[emi]))

    def estado4(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Parafiscal SENA: {0}".format(estados[emi]))

    def estado5(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Valor aporte caja de compensacion : {0}".format(estados[emi]))

    def estado6(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Parafiscal ICBF: {0}".format(estados[emi]))

    def estado7(self):
        estados = ["120mil", "100mil", "150mil", "115mil"]
        emi= randint(0,len(estados) -1)
        print("Auxilio de transporte: {0}".format(estados[emi]))

    def estado8(self):
        estados = ["1.500.000", "2.000.000", "3.000.000", "2.500.000"]
        emi= randint(0,len(estados) -1)
        print("Sueldo Neto devengado: {0}".format(estados[emi]))

    def estado9(self):
        estados = ["1 millon", "2 millones", "3 millones", "4 millones"]
        emi= randint(0,len(estados) -1)
        print("Liquidacion por año de trabajo: {0}".format(estados[emi]))

    def estado10(self):
        estados = ["12 millones", "10 millones", "20 millones", "42 millones"]
        emi= randint(0,len(estados) -1)
        print("Liquidacion Auxiliar administrativo por todos los años laborados : {0}".format(estados[emi]))

#----------------------ADMINISTRATIVOS-------------------------------------

class Tecnico (Planta):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
    genero = "", estrato = "", dependencia ="", titulo="", fechaVinculacion ="", nivel = "", salario = ""):

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo, fechaVinculacion)

        self.__nivel = nivel 
        self.__salario = salario


    def set_nivel(self, value):
        self.__nivel = value


    def get_nivel(self):
        return self.__nivel


    def set_salario(self, value):
        self.__salario = value


    def get_salario(self):
        return self.__salario


    def leer_datos(self):
        print("___________INGRESO DE DATOS________________")
        self.set_idPersona (Fun.control_numeros_letras("Digite el ID de la persona: "))
        self.set_nomPersona (Fun.control_letras("Digite el nombre: "))
        self.set_apePersona (Fun.control_letras("Digite el apellido: "))
        self.set_fechaNacimiento (Fun.control_numeros_letras("Digite la fecha de nacimiento: "))
        self.set_ciudadNacimiento (Fun.control_letras("Escriba la ciudad de nacimiento: "))
        self.set_genero (Fun.control_letras("Digite el genero de la persona: "))
        self.set_estrato(Fun.control_numeros("Digite el estrato socioeconomico: ")) 
        self.set_dependencia (Fun.control_letras("Digite la dependencia donde labora el tecnico: "))
        self.set_titulo (Fun.control_letras("Digite el titulo academico del tecnico: "))
        self.set_fechaVinculacion (Fun.control_letras("Digite la fecha de vinculacion del tecnico: "))
        self.set_nivel (Fun.control_numeros("Evalue su nivel de desempeño laboral de 1 a 5: "))
        self.set_salario(Fun.control_numeros("Digite el salario basico mensual recibido: ")) 


    def informacion_Imprimir_Datos(self):

        print("---------DATOS INGRESADOS------------\n"
        "ID personal: {0}\n" 
        "Nombre :  {1}\n" 
        "Apellido : {2}\n" 
        "Fecha de nacimiento: {3}\n"
        "Ciudad de nacimiento : {4}\n"
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
        estados = ["En DG1", "En DG2", "En DG3", "En DG4"]
        emi= randint(0,len(estados) -1)
        print("Aporte DG : {0}".format(estados[emi]))


    def estado2(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de EPS : {0}".format(estados[emi]))


    def estado3(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de PENSION: {0}".format(estados[emi]))


    def estado31(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de ARL: {0}".format(estados[emi]))

    def estado4(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Parafiscal SENA: {0}".format(estados[emi]))

    def estado5(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Valor aporte caja de compensacion : {0}".format(estados[emi]))

    def estado6(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Parafiscal ICBF: {0}".format(estados[emi]))

    def estado7(self):
        estados = ["120mil", "100mil", "150mil", "115mil"]
        emi= randint(0,len(estados) -1)
        print("Auxilio de transporte: {0}".format(estados[emi]))

    def estado8(self):
        estados = ["1.500.000", "2.000.000", "3.000.000", "2.500.000"]
        emi= randint(0,len(estados) -1)
        print("Sueldo Neto devengado: {0}".format(estados[emi]))

    def estado9(self):
        estados = ["1 millon", "2 millones", "3 millones", "4 millones"]
        emi= randint(0,len(estados) -1)
        print("Liquidacion por año de trabajo: {0}".format(estados[emi]))

    def estado10(self):
        estados = ["12 millones", "10 millones", "20 millones", "42 millones"]
        emi= randint(0,len(estados) -1)
        print("Liquidacion tecnico administrativo por todos los años laborados : {0}".format(estados[emi]))


#----------------------PROFESIONAL-------------------------------------

class Profesional (Planta):

    def __init__(self, idPersona = "", nomPersona = "", apePersona = "", fechaNacimiento = "", ciudadNacimiento = "",
    genero = "", estrato = "", dependencia = "", titulo = "", fechaVinculacion ="", nivel="",  salario=""):

        super ().__init__ (idPersona, nomPersona, apePersona, fechaNacimiento, ciudadNacimiento, genero, estrato, dependencia, titulo, fechaVinculacion)

        self.__nivel = nivel 
        self.__salario = salario


    def set_nivel(self, value):
        self.__nivel = value


    def get_nivel(self):
        return self.__nivel


    def set_salario(self, value):
        self.__salario = value


    def get_salario(self):
        return self.__salario

    def leer_datos(self):
        print("___________INGRESO DE DATOS________________")
        self.set_idPersona (Fun.control_numeros_letras("Digite el ID de la persona: "))
        self.set_nomPersona (Fun.control_letras("Digite el nombre: "))
        self.set_apePersona (Fun.control_letras("Digite el apellido: "))
        self.set_fechaNacimiento (Fun.control_numeros_letras("Digite la fecha de nacimiento: "))
        self.set_ciudadNacimiento (Fun.control_letras("Escriba la ciudad de nacimiento: "))
        self.set_genero (Fun.control_letras("Digite el genero de la persona: "))
        self.set_estrato(Fun.control_numeros("Digite el estrato socioeconomico: ")) 
        self.set_dependencia (Fun.control_letras("Digite la dependencia donde labora el profesional: "))
        self.set_titulo (Fun.control_letras("Digite el titulo academico del profesional: "))
        self.set_fechaVinculacion (Fun.control_letras("Digite la fecha de vinculacion del profesional: "))
        self.set_nivel (Fun.control_numeros("Evalue su nivel de desempeño laboral de 1 a 5: "))
        self.set_salario(Fun.control_numeros("Digite el salario basico mensual recibido: ")) 


    def informacion_Imprimir_Datos(self):

        print("---------DATOS INGRESADOS------------\n"
        "ID personal: {0}\n" 
        "Nombre :  {1}\n" 
        "Apellido : {2}\n" 
        "Fecha de nacimiento: {3}\n"
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
        estados = ["En DG1", "En DG2", "En DG3", "En DG4"]
        emi= randint(0,len(estados) -1)
        print("Aporte DG : {0}".format(estados[emi]))


    def estado2(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de EPS : {0}".format(estados[emi]))


    def estado3(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de PENSION: {0}".format(estados[emi]))


    def estado31(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Aporte de ARL: {0}".format(estados[emi]))

    def estado4(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Parafiscal SENA: {0}".format(estados[emi]))

    def estado5(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Valor aporte caja de compensacion : {0}".format(estados[emi]))

    def estado6(self):
        estados = ["150mil", "200mil", "300mil", "50mil"]
        emi= randint(0,len(estados) -1)
        print("Parafiscal ICBF: {0}".format(estados[emi]))

    def estado7(self):
        estados = ["120mil", "100mil", "150mil", "115mil"]
        emi= randint(0,len(estados) -1)
        print("Auxilio de transporte: {0}".format(estados[emi]))

    def estado8(self):
        estados = ["1.500.000", "2.000.000", "3.000.000", "2.500.000"]
        emi= randint(0,len(estados) -1)
        print("Sueldo Neto devengado: {0}".format(estados[emi]))

    def estado9(self):
        estados = ["1 millon", "2 millones", "3 millones", "4 millones"]
        emi= randint(0,len(estados) -1)
        print("Liquidacion por año de trabajo: {0}".format(estados[emi]))

    def estado10(self):
        estados = ["12 millones", "10 millones", "20 millones", "42 millones"]
        emi= randint(0,len(estados) -1)
        print("Liquidacion tecnico administrativo por todos los años laborados : {0}".format(estados[emi]))  


#----------------------FIN ARBOL ------------------------------------- 


#***************************************#
# CENTRO DE BIOTECNOLOGIA AGROPECUARIA  #
# NOMBRE EMILIANO PERILLA AGUILAR       #
# VERSION : 4.0                         #
# Fecha: 09/06/2024                     #
#***************************************#

#Este programa se encuentra diseñado par demostrar la funcionalidad que resulta 
# del correcto manejo del POP, mediante super clases, subclases y clases logramos
# crear y modificar los atributos y metodos de un objeto. Super clase producto, 



from modules import clases  # Importo modulo clases donde esta la informacion principal del programa 
from random import randint # Importo randint para sacar valore aleatorios en algunos estados 
from modules import functions as Fun # Importo funciones donde se encuentran funciones de control de entrada 
# from colorama import Fore,Back # Importo colorama para color fondo y fuente
# print(Fore.BLACK + Back.BLUE)# Defino colores fondo y fuente 

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
    completo = clases.TiempoCompleto ("", "", "", "", "", "", 0, "", "", "", 0, 0, 0) # Defino 

    completo.leer_datos()       # Esta funcion de 

    completo.informacion_Imprimir_Datos() # Esta funcion 

    completo.estado1() # Esta funcion me imprime 

    completo.estado2() # Esta funcion me imprime

    completo.estado3() # Esta funcion me imprime

    completo.estado31() # Esta funcion me imprime

    completo.estado4() # Esta funcion me imprime

    completo.estado5() # Esta funcion me imprime

    completo.estado6() # Esta funcion me imprime

    completo.estado7() # Esta funcion me imprime

    completo.estado8() # Esta funcion me imprime

    completo.estado9() # Esta funcion me imprime


  elif opcion== 2:
    
    ocacional = clases.Ocasionales ("", "", "", "", "", "", 0, "", "", "", "", 0, 0) # Defino

    ocacional.leer_datos()       # Esta funcion de 

    ocacional.informacion_Imprimir_Datos() # Esta funcion 

    ocacional.estado1() # Esta funcion me imprime 

    ocacional.estado2() # Esta funcion me imprime

    ocacional.estado3() # Esta funcion me imprime

    ocacional.estado31() # Esta funcion me imprime

    ocacional.estado4() # Esta funcion me imprime

    ocacional.estado5() # Esta funcion me imprime

    ocacional.estado6() # Esta funcion me imprime

    ocacional.estado7() # Esta funcion me imprime

    ocacional.estado8() # Esta funcion me imprime

    ocacional.estado9() # Esta funcion me imprime

  elif opcion== 3:

    catedra = clases.HoraCatedra ("", "", "", "", "", "", 0, "", "", 0, 0, 0, 0) # Defino

    catedra.leer_datos()       # Esta funcion de 

    catedra.informacion_Imprimir_Datos() # Esta funcion 

    catedra.estado1() # Esta funcion me imprime 

    catedra.estado2() # Esta funcion me imprime

    catedra.estado3() # Esta funcion me imprime

    catedra.estado31() # Esta funcion me imprime

    catedra.estado4() # Esta funcion me imprime

    catedra.estado5() # Esta funcion me imprime

    catedra.estado6() # Esta funcion me imprime

    catedra.estado7() # Esta funcion me imprime

    catedra.estado8() # Esta funcion me imprime

    catedra.estado9() # Esta funcion me imprime

    

  elif opcion== 4:

    auxilia = clases.Auxiliar ("", "", "", "", "", "", 0, "", "", "", 0, 0) # Defino

    auxilia.leer_datos()       # Esta funcion de 

    auxilia.informacion_Imprimir_Datos() # Esta funcion 

    auxilia.estado1() # Esta funcion me imprime 

    auxilia.estado2() # Esta funcion me imprime

    auxilia.estado3() # Esta funcion me imprime

    auxilia.estado31() # Esta funcion me imprime

    auxilia.estado4() # Esta funcion me imprime

    auxilia.estado5() # Esta funcion me imprime

    auxilia.estado6() # Esta funcion me imprime

    auxilia.estado7() # Esta funcion me imprime

    auxilia.estado8() # Esta funcion me imprime

    auxilia.estado9() # Esta funcion me imprime

    auxilia.estado10() # Esta funcion me imprime
    
  
  elif opcion== 5:

    tecnic = clases.Tecnico("", "", "", "", "", "", 0, "", "", "", 0, 0) # Defino

    tecnic.leer_datos()       # Esta funcion de 

    tecnic.informacion_Imprimir_Datos() # Esta funcion 

    tecnic.estado1() # Esta funcion me imprime 

    tecnic.estado2() # Esta funcion me imprime

    tecnic.estado3() # Esta funcion me imprime

    tecnic.estado31() # Esta funcion me imprime

    tecnic.estado4() # Esta funcion me imprime

    tecnic.estado5() # Esta funcion me imprime

    tecnic.estado6() # Esta funcion me imprime

    tecnic.estado7() # Esta funcion me imprime

    tecnic.estado8() # Esta funcion me imprime

    tecnic.estado9() # Esta funcion me imprime

    tecnic.estado10() # Esta funcion me imprime


  elif opcion== 6:

    profes = clases.Profesional("", "", "", "", "", "", 0, "", "", "", 0, 0) # Defino

    profes.leer_datos()       # Esta funcion de 

    profes.informacion_Imprimir_Datos() # Esta funcion 

    profes.estado1() # Esta funcion me imprime 

    profes.estado2() # Esta funcion me imprime

    profes.estado3() # Esta funcion me imprime

    profes.estado31() # Esta funcion me imprime

    profes.estado4() # Esta funcion me imprime

    profes.estado5() # Esta funcion me imprime

    profes.estado6() # Esta funcion me imprime

    profes.estado7() # Esta funcion me imprime

    profes.estado8() # Esta funcion me imprime

    profes.estado9() # Esta funcion me imprime

    profes.estado10() # Esta funcion me imprime


  elif opcion== 7:

    prestadorService = clases.OPS("", "", "", "", "", "", 0, "", "", "", 0, 0) # Defino

    prestadorService.leer_datos()       # Esta funcion de 

    prestadorService.informacion_Imprimir_Datos() # Esta funcion 

    prestadorService.estado1() # Esta funcion me imprime 

    prestadorService.estado2() # Esta funcion me imprime

    prestadorService.estado3() # Esta funcion me imprime

    prestadorService.estado31() # Esta funcion me imprime

    prestadorService.estado4() # Esta funcion me imprime

    prestadorService.estado5() # Esta funcion me imprime

    prestadorService.estado6() # Esta funcion me imprime

    prestadorService.estado7() # Esta funcion me imprime

    prestadorService.estado8() # Esta funcion me imprime

    prestadorService.estado9() # Esta funcion me imprime

    prestadorService.estado10() # Esta funcion me imprime

  elif opcion== 0:
    print("Adios") # Al digitar tecla 5 el usuario sale del programa y aparece el letrero ADIOS 
    break          # Declaracion para la finalizacion del bucle while del menu 
  else:
    print("Opcion no valida") # Si se llegase a digitar un numero diferente de 1 a 5 aparece opcion no valida 
