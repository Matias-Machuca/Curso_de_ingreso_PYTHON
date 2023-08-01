import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Matias
apellido: Machuca
div: I
---
Ejercicio: instrucion_if_06
---
Enunciado:
Al presionar el botón 'Calcular', se deberá obtener contenido en la
caja de texto txtEdad, transformarlo en número y calcular si es mayor de edad,
niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años) o
adolescente (edad entre 13 y 17 años) , se deberá informar utilizando
el Dialog alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad_txt = self.txt_edad.get()
        edad_num = int(edad_txt)

        if edad_num > 0 and edad_num < 10:
            alert("Etapa", "Niño/a.")
        elif edad_num > 9 and edad_num < 14:
            alert("Etapa", "Pre-Adolescente.")
        elif edad_num > 12 and edad_num < 18:
            alert("Etapa", "Adolescente.")
        elif edad_num > 17:
            alert("Etapa", "Mayor de Edad.")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()