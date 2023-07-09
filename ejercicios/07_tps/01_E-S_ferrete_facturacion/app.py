import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
---
nombre: Matias
apellido: Machuca
div: I
---
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        precio_1_txt = self.txt_importe_1.get()
        precio_1_num = float(precio_1_txt)

        precio_2_txt = self.txt_importe_2.get()
        precio_2_num = float(precio_2_txt)

        precio_3_txt = self.txt_importe_3.get()
        precio_3_num = float(precio_3_txt)

        suma = precio_1_num + precio_2_num + precio_3_num
        suma_txt = str(suma)

        alert("Suma", "El total es: $" + suma_txt)



    def btn_promedio_on_click(self):
        precio_1_txt = self.txt_importe_1.get()
        precio_1_num = float(precio_1_txt)

        precio_2_txt = self.txt_importe_2.get()
        precio_2_num = float(precio_2_txt)

        precio_3_txt = self.txt_importe_3.get()
        precio_3_num = float(precio_3_txt)

        promedio = (precio_1_num + precio_2_num + precio_3_num) / 3
        promedio_txt = str(promedio)

        alert("Promedio", "El promedio es: $" + promedio_txt)



    def btn_total_iva_on_click(self):
        precio_1_txt = self.txt_importe_1.get()
        precio_1_num = float(precio_1_txt)

        precio_2_txt = self.txt_importe_2.get()
        precio_2_num = float(precio_2_txt)

        precio_3_txt = self.txt_importe_3.get()
        precio_3_num = float(precio_3_txt)

        total_iva = (precio_1_num + precio_2_num + precio_3_num) * 1.21
        total_iva_txt = str(total_iva)

        alert("Total IVA", "El precio final mas IVA es: $" + total_iva_txt)

        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()