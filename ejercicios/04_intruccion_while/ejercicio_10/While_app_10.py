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
        respuesta = True
        acumulador_negativos = 0
        acumulador_positivos = 0
        contador_negativos = 0
        contador_positivos = 0
        contador_ceros = 0
        mensaje = ""

        while respuesta == True:
            numero = prompt("Ingreso", "Ingrese un numero")
            numero = float(numero)
            if numero < 0:
                acumulador_negativos += numero
                acumulador_negativos_txt = str(acumulador_negativos)
                mensaje += "\nLa suma de numeros negativos da: " + acumulador_negativos_txt
                contador_negativos += 1
                contador_negativos_txt = str(contador_negativos)
                mensaje += "\nLa cantidad de numeros negativos es: " + contador_negativos_txt
            elif numero > 0:
                acumulador_positivos += numero
                acumulador_positivos_txt = str(acumulador_positivos)
                mensaje += "\nLa suma de numeros positivos es: " + acumulador_positivos_txt
                contador_positivos += 1
                contador_positivos_txt = str(contador_positivos)
                mensaje += "\nLa cantidad de numeros positivos es: " + contador_positivos_txt
            else:
                contador_ceros += 1
                contador_ceros_txt = str(contador_ceros)
                mensaje += "\nLa cantidad de ceros es de: " + contador_ceros_txt

            respuesta = question("¿Continuar?", "¿Desea ingresar otro numero?")

        diferencia_positivos_negativos = contador_positivos - contador_negativos
        diferencia_positivos_negativos_txt = str(diferencia_positivos_negativos)
        mensaje += "\nLa diferencia entre cantidad de positivos y negativos es: " + diferencia_positivos_negativos_txt

        alert("Resultados", mensaje)

        '''PROBAR SACANDO VARIABLES DE DENTRO DE MENSAJE Y CONCATENAR FUERA DEL BUCLE
        DEJANDO SOLO LOS STRINGS EN CADA MENSAJE'''

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
