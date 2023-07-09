import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math

'''
---
nombre: Matias
apellido: Machuca
div: I
---
Enunciado:

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado perimetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro.
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en es lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts
    (V)Poste Quebracho Fino de 2.2 mts
    (F)Varillas
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)

        self.btn_calcular = customtkinter.CTkButton(
            master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):
        largo_txt = self.txt_largo.get()
        largo_num = float(largo_txt)

        ancho_txt = self.txt_ancho.get()
        ancho_num = float(ancho_txt)

        metros_cuadrados_num = largo_num * ancho_num
        metros_cuadrados_txt = str(metros_cuadrados_num)

        metros_lineales_num = (largo_num * 2) + (ancho_num *2)
        metros_lineales_txt = str(metros_lineales_num)

        #print(metros_lineales_num)

        poste_q_grueso_num = math.floor((metros_lineales_num / 250) + 4)
        poste_q_grueso_txt = str(poste_q_grueso_num)

        #print(poste_q_grueso_num)

        poste_q_fino_num = math.floor(metros_lineales_num / 12)
        poste_q_fino_txt = str(poste_q_fino_num)

        varillas_num = (metros_lineales_num / 2)
        varillas_txt = str(varillas_num)

        cant_alambre_num = math.ceil(metros_lineales_num * 7)
        cant_alambre_txt = str(cant_alambre_num)

        alert("A", "El terreno tiene " + metros_cuadrados_txt + " metros cuadrados y " + metros_lineales_txt + " metros lineales de perimetro.")
        alert("B", "Lleva " + poste_q_grueso_txt + " postes de quebracho grueso de 2.4 mts.")
        alert("C", "Lleva " + poste_q_fino_txt + " postes de quebracho fino de 2.2 mts.")
        alert("D", "Lleva " + varillas_txt + " varillas.")
        alert("E", "Lleva "+ cant_alambre_txt + " metros de alambre de alta resistencia.")


        '''alert("Info", "El terreno tiene " + metros_cuadrados_txt + " metros cuadrados y " + metros_lineales_txt + " metros lineales de perimetro. " +  
        "Lleva " + poste_q_grueso_txt + " postes de quebracho grueso de 2.4 mts. " +
        "Lleva " + poste_q_fino_txt + " postes de quebracho fino de 2.2 mts. " +
        "Lleva " + varillas_txt + " varillas. " +
        "Lleva " + cant_alambre_txt + " metros de alambre de alta resistencia.")'''
        




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
