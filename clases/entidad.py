""" ANDRES JUAN GUTIERREZ CASTRO
FICHA: 2471718 """

import json

class Entidad:
    #CREAMOS EL CONSTRUCTOS
    def __init__(self):
        #CREAMOS UN ATRIBUTO EL CUAL VA A SER UN DICCIONARIO
        self.diccionario_cliente = {}
    
    #FUNCION PARA DEFINIR LOS 3 CLIENTES
    def definir_clientes(self):
        #DEFINIMOS EL DEPOSITO Y EL RETIRO EN CEROS PARA MANIPULARLOS DEPSUES
        deposito = 0
        retiro = 0

        #COMO SON 3 LOS EMPLEADO PEDIDOS EN EL EJEMPLO CREAMOS UN CICLO FOR QUE SE REPITA 3 VECES
        for i in range(3):
            nombre = input("Escribe el nombre del cliente: ")
            #GUARDAMOS LOS ARGUMENTOS DEL METODO EN EL DICCIONARIO
            self.diccionario_cliente[nombre] = {'deposito': deposito, 'retiro':retiro}
            #GUARDAMOS EL ARCHIVO DE TEXTO
            with open('./static/deposito.txt', 'a') as archivo:
                archivo.write(json.dumps(self.diccionario_cliente))
            
    #AGREGAR DEPOSITO
    def agregar_deposito(self):
        #CREAMOS UN CICLO WHILE PARA AGREGAR DEPOSITOS
        cliente = input('Escribe el nombre del cliente')
        while True:
            #VALIDAMOS QUE EL NOMBRE SEA EL MISMO QUE ESTE EN EL DICCIONARIO
            if cliente in self.diccionario_cliente:
                deposito = 0
                #RECIBIMOS UN INPUT CON LE NUMERO QUE VAMOS A AGREGAR
                cantidad_ingresada = int(input("Escribe la cantida de deposito que vas a agregar: "))

                #INCREMENTAMOS EL VALOR DEL DEPOSITO ANTES DE AGREGARLO
                deposito += cantidad_ingresada

                #MODIFICAMOS DEL VALOR DEL DEPOSTO
                self.diccionario_cliente[cliente]["deposito"] = deposito

                #ESCRIBIMOS LOS DATOS DENTRO DEL ARCHIVO DE TEXTO
                with open('./static/deposito.txt', 'a') as archivo:
                    archivo.write("\n<=====Deposito Agregado=====>\n")
                    archivo.write(json.dumps(self.diccionario_cliente))
                
                #PREGUNTAMOS SI EL USUARIO AGREGARA UN NUEVO DEPOSITO
                print("Deposito agregado")

                pregunta = input("Agregar un nuevo deposito?:")
                if pregunta.upper() == 'SI':
                    print("Espera...")
                else:
                    break

            else:
                print("Haz ingresado un dato no valido")
                break
    
    #FUNNCION PARA RETIRAR
    def retirar_dinero(self):
        cliente = input('Escribe el nombre del cliente')
        #CREAMOS UN CICLO WHILE PARA AGREGAR DEPOSITOS
        while True:
            #VALIDAMOS QUE EL NOMBRE SEA EL MISMO QUE ESTE EN EL DICCIONARIO
            if cliente in self.diccionario_cliente:
                retiro = 0
                #RECIBIMOS UN INPUT CON LE NUMERO QUE VAMOS A AGREGAR
                cantidad_retirada = int(input("Escribe la cantidad de dinero que vas a retirar: "))

                #INCREMENTAMOS EL VALOR DEL DEPOSITO ANTES DE AGREGARLO
                retiro += cantidad_retirada

                #MODIFICAMOS DEL VALOR DEL DEPOSTO
                self.diccionario_cliente[cliente]["deposito"] -= cantidad_retirada
                self.diccionario_cliente[cliente]["retiro"] = retiro

                #ESCRIBIMOS LOS DATOS DENTRO DEL ARCHIVO DE TEXTO
                with open('./static/deposito.txt', 'a') as archivo:
                    archivo.write("\n<=====Deposito Retirado=====>\n")
                    archivo.write(json.dumps(self.diccionario_cliente))
                
                #PREGUNTAMOS SI EL USUARIO AGREGARA UN NUEVO DEPOSITO
                print("Retiro exitoso")

                pregunta = input("Retirar nuevo deposito?:")
                if pregunta.upper() == 'SI':
                    print("Espera...")
                else:
                    break
            else:
                print("Haz ingresado un dato no valido")
                break
    
    #CREAMOS UNA FUNCION QUE INICE TODAS LAS DEMAS
    def menu_opciones(self):
        #CREAMOS EL CICLO QUE A RECORRER LAS OPCIONES
        while True:
            print("<============================================================>")
            print(
                "Opciones de la Entidad Financiera:\n" +
                "1. Crear clientes\n" +
                "2. Agregar deposito\n" +
                "3. Retirar dinero\n" +
                "4. Salir\n"
            )

            #CREAMOS UNA VARIABLE QUE VA CONTENER LA OPCION DEL USUARIO
            opcion = int(input("Esbribe el numemero de opcion: "))

            #EVALUAMOS LA OPCION ESCOGIGA Y LLAMAMOS LA FUNCION
            if opcion == 1:
                #LLAMADO AL METODO
                self.definir_clientes()
            elif opcion == 2:
                #LLAMADO AL METODO
                self.agregar_deposito()
            elif opcion == 3:
                #LLAMADO AL METODO
                self.retirar_dinero()
            elif opcion == 4:
                print("Haz elegido salir del programa")
                break
            else:
                print("Respuesta no aceptada")
