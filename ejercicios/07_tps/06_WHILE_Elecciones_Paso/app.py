import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Machuca
Div: "I"

De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        
        respuesta = True
        maximo_votos = None
        minimo_votos = None
        acumulador_votos = 0
        cantidad_candidatos = 0
        acumulador_edades = 0

        while respuesta:
            nombre = prompt("nombre", "Ingrese nombre")
            while nombre is None or not nombre.isalpha():
                nombre = prompt("nombre", "Ingrese nuevamente su nombre")
            
            edad = prompt("Edad", "Ingrese edad ")
            while edad is None or not edad.isdigit() or int(edad) < 26:
                edad = prompt("Error", "Ingresar edad correcta")
            edad = int(edad)

            cantidad_votos = prompt("Cantidad de votos", "Ingrese la cantidad de votos")
            while cantidad_votos is None or not cantidad_votos.isdigit():
                cantidad_votos = prompt("cantidad_votos", "Ingresar cantidad votos")
            cantidad_votos = int(cantidad_votos)

            if maximo_votos is None or cantidad_votos > maximo_votos:
                maximo_votos = cantidad_votos
                candidato_con_mas_votos = nombre
            if minimo_votos is None or cantidad_votos < minimo_votos:
                minimo_votos = cantidad_votos
                candidato_menos_votos = nombre
                edad_menos_votado = edad

            cantidad_candidatos += 1

            acumulador_edades += edad

            acumulador_votos += cantidad_votos

            respuesta = question("Nuevo ingreso", "¿Desea ingresar otro/a candidato?")


        promedio_edades = acumulador_edades / cantidad_candidatos

        print(candidato_con_mas_votos + " fue el/la mas votado/a")
        print(candidato_menos_votos + " de " + str(edad_menos_votado) + " años fue el/la menos votado/a")
        print("El promedio de edad es: " + str(promedio_edades))
        print("El total de votos es: " + str(acumulador_votos))

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
