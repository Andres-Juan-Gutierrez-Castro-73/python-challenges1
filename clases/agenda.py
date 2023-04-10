""" ANDRES JUAN GUTIERREZ CASTRO
FICHA: 2471718 """

import json

#CREAMOS LA CLASE AGENDA
class Agenda:
    #CREACION DEL METODO CONSTRUCTOR
    def __init__(self):
        #CREAMOS UN DICCIONARIO CON LA INFORMACION DE LOS USUARIOS
        self.diccionario_agenda = {}
    
    #FUNCION PARA CREAR UN USUARIO
    def anotar_contacto(self, nombre, telefono, correo):
        #APARTIR DEL NOMBRE VAMOS A GUARDAR LA INFORMACION EN EL DICCIONARIO
        self.diccionario_agenda[nombre] = {'telefono': telefono, 'correo': correo}

        #GUARDAMOS EL ARCHIVO DE TEXTO
        with open('./static/agenda.txt', 'a') as archivo:
            archivo.write(json.dumps(self.diccionario_agenda))
        
        #RETORNAMOS UN MENSAJE POR PANTALLA
        print("¡Nuevo usuario agregado!")
    
    #FUNCION PARA RETORNAR LA LISTA DE LOS QUE ESTAN EN LA AGENDA
    def listado_agenda(self):
        print("Los usuarios que hasta este momento estan en la agenda son:\n")
        #RECORREMOS TODA LA LISTA DE DATOS DEL DICCIONARIO CON UN BUCLE FOR
        for nombre, dato in self.diccionario_agenda.items():
            print(f'{nombre}: numero_telefonico: {dato["telefono"]}, correo_electronico: {dato["correo"]}')
    
    #FUNNCION PARA CONSULTA PERSONA CON EL NOMBRE
    def consultar_persona(self, nombre):
        #CON UN IF CONFIRMAMOS QUE EL ARGUMENTO DEL METODO SEAL EL MISMO QUE UNO DE LOS ELEMENTOS DE LA LISTA
        if nombre in self.diccionario_agenda:
            #GUARDAMOE LE REGISTRO DEL CONTACTO EN UNA VARIABLE
            dato = self.diccionario_agenda[nombre]
            print(f'{nombre}: teléfono: {dato["telefono"]}, mail: {dato["correo"]}')
        else:
            print("Este contacto aun no se ha registrado en la agenda")

    #FUNCION PARA MODIFICAR LA INFORMACION
    def modificar_registro(self, nombre, telefono, correo):
        #EVALUAMOS QUE EL NOMBRE ESTE PRIMERO EN LA AGENDA
        if nombre in self.diccionario_agenda:
            #MODIFICAMOS LOS DATOS QUE HAYAN DENTRO DEL DICCIONARIO
            self.diccionario_agenda[nombre]['telefono'] = telefono
            self.diccionario_agenda[nombre]['correo'] = correo

            #ESCRIBIMOS LOS DATOS DENTRO DEL ARCHIVO DE TEXTO
            with open('./static/agenda.txt', 'w') as archivo:
                archivo.write(json.dumps(self.diccionario_agenda))
            
            #RETORNAMOS UN MENSAJE POR PANTALLA
            print("¡El usuario se ha modificado!")
        else:
            print("No exite un usuario con el nombre que escribirte")
    
    #DEFINIMOS UNA FUNCION QUE TENGA UN MENU DE OPCIONES PARA EJECUTAR LA APLICACION
    def menu_opciones(self):
        #CREMAMOS UN CICLO PARA RECORRER LAS FUNCIONES DEPENDIENDO DE LA RESPUESTA
        while True:
            print("<============================================================>")
            print(
                "Opciones de la Agenda:\n" +
                "1. Escribir un contacto\n" +
                "2. Mostrar la lista de contratos\n" +
                "3. Consultar un contacto\n" +
                "4. Modificar un contacto\n" +
                "5. Salir del programa\n"
            )

            #CREAMOS UNA VARIABLE QUE VA CONTENER LA OPCION DEL USUARIO
            opcion = int(input("Esbribe el numemero de opcion: "))

            #EVALUAMOS LA OPCION ESCOGIGA Y LLAMAMOS LA FUNCION
            if opcion == 1:
                #REBIMOS LOS DATOS
                nombre = input('Ingrese el nombre del contacto: ')
                telefono = input('Ingrese el teléfono del contacto: ')
                correo = input('Ingrese el mail del contacto: ')

                #LOS ENVIAMOS AL METODO
                self.anotar_contacto(nombre, telefono, correo)
            elif opcion == 2:
                #LLAMADO AL METODO
                self.listado_agenda()
            elif opcion == 3:
                #RECIBIMOS EL NOMBRE  A BUSCAR
                nombre = input("Escribe el nombre del contacto de la agenda: ")
                self.consultar_persona(nombre)
            elif opcion == 4:
                #RECIBIMOS LOS DATOS S MODIFICAR CON UN INPUT
                nombre = input('Ingrese el nombre del contacto a modificar: ')
                telefono = input('Ingrese el nuevo teléfono del contacto: ')
                correo = input('Ingrese el nuevo mail del contacto: ')
                self.modificar_registro(nombre, telefono, correo)
            elif opcion == 5:
                print("Elegiste salir de la aplicacion, adios")
                break
            else:
                print("Respuesta no aceptada")

