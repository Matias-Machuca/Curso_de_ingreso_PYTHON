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

        numero = prompt("Ingreso", "Ingrese un numero")
        while not numero.isdigit():
            numero = prompt("Error", "Ingresar solo numeros")
        numero = int(numero)

        for numero in range(0, 1, 1):
            if numero % numero == 0 and numero % 1 == 0:
                alert("Primos", "El numero " + str(numero) + " es primo")
            else:
                alert("Primos", "El numero " + str(numero) + " no es primo")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()