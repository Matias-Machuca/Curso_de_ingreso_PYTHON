import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Machuca
Div: "I"

Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        contador_numeros_divisores = 1
        cantidad_divisores = 0

        numero = prompt("Ingreso", "Ingrese un numero")
        while numero is None or not numero.isdigit():
            numero = prompt("Error", "Ingresar solo numeros")
        numero = int(numero)

        for i in range(1, numero, 1):
            cantidad_divisores += 1
            if numero % cantidad_divisores == 0:
                contador_numeros_divisores += 1
        if contador_numeros_divisores == 2:
            mensaje = "Es primo"
        elif contador_numeros_divisores > 2 or numero == 1:
            mensaje = "No es primo"
        if numero == 0:
            mensaje = "Es un numero aparte"

        alert("¿Primo?", mensaje)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()