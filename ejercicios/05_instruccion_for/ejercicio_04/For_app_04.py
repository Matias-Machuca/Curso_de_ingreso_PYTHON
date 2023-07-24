import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Machuca
Div: "I"

Al presionar el botón Mostrar pedir valores por prompt hasta que el usuario ingrese el
valor 9 (se deberá utilizar 'BREAK').
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        for _ in iter(int, 1):
            valor = prompt("Ingreso", "Ingrese un valor")
            while valor is None or not valor.isdigit():
                valor = prompt("Error", "Ingrese un valor numerico")
            valor = int(valor)
            if valor == 9:
                break
        alert("alert", "Estoy fuera del bucle")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

'''

        from itertools import count
        for i in count():
        "para hacer un for infinito"

        o

        for _ in iter(int, 1):

        '''