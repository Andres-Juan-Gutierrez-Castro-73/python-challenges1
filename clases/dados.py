""" ANDRES JUAN GUTIERREZ CASTRO
FICHA: 2471718 """

import random

class JuegoDados:
    #DEFINIMOS LA CLASE CONSTRUCTORA
    def __init__(self):
        #DEFINIMOS LOS ATRIBUTOS QUE VAN A SER USADOS POR LOS METODOS
        self.resultado = []
        self.ganador = False

    #FUNCION PARA TIRAR LOS DADOS
    def jugar(self):
        #CREAMOS UN CICLO QUE SE VA RECORRER 3 VECES (UN LANZAMIENTO POR DADO)
        for i in range(3):
            self.resultado.append(random.randint(1, 6))
        print("Los resultados son:", self.resultado)

        #VALIDAMOS SI LOS DATOS TIENEN EL MISMO RESULTADO
        if self.resultado[0] == self.resultado[1] == self.resultado[2]:
            self.ganador = True

    #FUNCION PARA MOSTRAR EL RESULTADO
    def mostrar_resultado(self):
        if self.ganador:
            print("¡Felicidades, has ganado!")
        else:
            print("Lo siento, has perdido.")

juego = JuegoDados()

