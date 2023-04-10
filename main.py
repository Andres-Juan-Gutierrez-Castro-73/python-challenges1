""" ANDRES JUAN GUTIERREZ CASTRO
FICHA: 2471718 """

#IMPORTAMOS LA CLASE EN LA QUE VA A ESTAR AL LOGICA DEL PROGRAMA
from clases.agenda import Agenda
from clases.entidad import Entidad
from clases.dados import JuegoDados

#INSTANCIAMOS LA CLASE
objeto_agenda = Agenda()
objeto_entidad = Entidad()
objeto_datos = JuegoDados()

print(
    "<======SOLUCION TALLER PYTHON CON CLASES=====>\n" +
    "1. Agenda\n" +
    "2. Entidad Financiera\n" +
    "3. Juego Dados\n"
)

#PREGUNTAMOS CUAL ES EL PROBLEMA SE QUE QUIERE MOSTRAR
numero_problema = int(input("Esbribe el numero del problema que quieres ver: "))

#EJECUTAMOS LA CLASE
if numero_problema == 1:
    objeto_agenda.menu_opciones()
elif numero_problema == 2:
    objeto_entidad.menu_opciones()
elif numero_problema == 3:
    objeto_datos.jugar()
    objeto_datos.mostrar_resultado()
else:
    print("Respuesta no aceptada")