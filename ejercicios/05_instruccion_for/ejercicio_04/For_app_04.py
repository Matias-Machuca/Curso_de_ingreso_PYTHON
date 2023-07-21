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

        '''valor = prompt("Valores", "Ingrese un valor")
        while not valor.isdigit():
            valor = prompt("Valores", "Ingrese un valor numerico")
        valor = int(valor)'''

        i = prompt("Valores", "Ingrese un valor")
        i = int(i)
        for i in range(0, 99999, 1):
            if i == 9:
                break
            i = prompt("Valores", "Ingrese un valor valido")
            i = int(i)

        alert("msj", "Fuera del bucle")


        '''

        from itertools import count
        for i in count():
        "para hacer un for infinito"

        '''


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()