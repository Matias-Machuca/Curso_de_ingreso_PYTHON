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
Al presionar el botón ‘Validar número’, mediante prompt solicitar al usuario
que ingrese un número. Se deberá validar que se encuentre entre 0 y 9 inclusive.
En caso no coincidir con el rango, volverlo a solicitar hasta que la condición
se cumpla
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_numero = customtkinter.CTkButton(master=self, text="Validar numero", command=self.btn_validar_numero_on_click)
        self.btn_validar_numero.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_numero_on_click(self):

        numero = prompt("Ingreso", "Ingrese un numero")
        while numero is None or not numero.isdigit() or (int(numero) < 0 or int(numero) > 9):
            alert("Denegado", "Vuelva a ingresar un numero correcto")
            numero = prompt("Ingreso", "Ingrese un numero valido")
        numero = int(numero)

        alert("Ingreso", "¡Acceso permitido!")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()