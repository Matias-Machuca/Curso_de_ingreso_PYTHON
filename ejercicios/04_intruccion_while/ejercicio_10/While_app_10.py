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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números
que el usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos
Informar los resultados mediante alert()
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        acumulador_negativos = 0
        acumulador_positivos = 0
        contador_negativos = 0
        contador_positivos = 0
        contador_ceros = 0

        numero = prompt("Ingreso", "Ingrese un numero")
        while numero is not None:
            numero = int(numero)
            if numero < 0:
                acumulador_negativos += numero
                contador_negativos += 1
            elif numero > 0:
                acumulador_positivos += numero
                contador_positivos += 1
            else:
                contador_ceros += 1
            if numero is None:
                break    
            numero = prompt("Ingreso", "Ingrese un numero")

        diferencia_positivos_negativos = contador_positivos - contador_negativos

        mensaje = "La suma de numeros negativos es: " + str(acumulador_negativos)
        mensaje += "\nLa suma de numeros positivos es: " + str(acumulador_positivos)
        mensaje += "\nLa cantidad de numeros negativos es: " + str(contador_negativos)
        mensaje += "\nLa cantidad de numeros positivos es: " + str(contador_positivos)
        mensaje += "\nLa cantidad de ceros es : " + str(contador_ceros)
        mensaje += "\nLa diferencia entre cantidad de positivos y negativos es: " + str(diferencia_positivos_negativos)

        alert("Resultados", mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
