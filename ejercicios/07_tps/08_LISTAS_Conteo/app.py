import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Machuca
Div: "I"

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los 
números que el usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []


    def btn_comenzar_ingreso_on_click(self):

        self.lista.clear()

        respuesta = True

        while respuesta == True or respuesta == '':
            numero = prompt("Ingreso", "Ingrese un numero")
            while numero is None or numero == '':
                numero = prompt("Ingreso", "Ingresar un numero")
            numero = int(numero)
            self.lista.append(numero)

            respuesta = prompt("Continuar ingreso", "¿Desea ingresar otro numero?")

        #print(self.lista)
        
    def btn_mostrar_estadisticas_on_click(self):

        acumulador_negativos = 0
        acumulador_positivos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        bandera_positivos_negativos = True

        for numero in self.lista:
            if numero > 0:
                acumulador_positivos += numero
                contador_positivos += 1
            elif numero < 0:
                acumulador_negativos += numero
                contador_negativos += 1
            else:
                contador_ceros += 1

            if bandera_positivos_negativos == True:
                maximo_positivo = numero
                minimo_negativos = numero
                bandera_positivos_negativos = False
            else:
                if numero > maximo_positivo:
                    maximo_positivo = numero
                elif numero < minimo_negativos:
                    minimo_negativos = numero

        if contador_negativos > 0:    
            promedio_negativos = acumulador_negativos / contador_negativos
        else:
            promedio_negativos = "No se ingresaron numeros negativos"

        mensaje = "La suma de negativos es: " + str(acumulador_negativos)
        mensaje += "\nLa suma de positivos es: " + str(acumulador_positivos)
        mensaje += "\nLa cantidad de numeros positivos es: " + str(contador_positivos)
        mensaje += "\nLa cantidad de numeros negativos es: " + str(contador_negativos)
        mensaje += "\nLa cantidad de ceros es: " + str(contador_ceros)
        mensaje += "\nEl minimo de los negativos es: " + str(minimo_negativos)
        mensaje += "\nEl maximo de los positivos es: " + str(maximo_positivo)
        mensaje += "\nEl promedio de los negativos es: " + str(promedio_negativos)

        alert("Estadisticas", mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
