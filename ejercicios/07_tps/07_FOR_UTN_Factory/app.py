'''
Nombre: Matias
Apellido: Machuca
Div: "I"

UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

        # Variables/contadores/acumuladores/banderas
        contador_postulantes_no_binarios_a = 0
        minimo_edad_jr = None
        acumulador_edades_femeninas = 0
        acumulador_edades_masculinos = 0
        acumuldor_edades_no_binarios = 0
        contador_postulantes_femeninas = 0
        contador_postulantes_masculinos = 0
        contador_postulantes_no_binarios = 0
        contador_postulates_python = 0
        contador_postulantes_js = 0
        contador_postulantes_asp_net = 0
    
        for i in range(0, 10, 1):

            # Validaciones
            nombre = prompt("Nombre", "Ingrese nombre")
            while nombre is None or not nombre.isalpha():
                nombre = prompt("Error", "Ingrese nuevamente su nombre")

            edad = prompt("Edad", "Ingrese edad ")
            while edad is None or not edad.isdigit() or int(edad) < 18:
                edad = prompt("Error", "Ingresar edad correcta")
            edad = int(edad)

            genero = prompt("Genero", " Ingrese genero: F - M - NB")
            while genero != "F" and genero != "M" and genero != "NB":
                genero = prompt("Error", "Ingrese genero: F - M - NB")

            tecnologia = prompt("Tecnologia", " Ingrese tecnologia: PYTHON - JS - ASP.NET")
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("Error", "Ingrese tecnologia: PYTHON - JS - ASP.NET")

            puesto = prompt("Puesto", " Ingrese puesto: Jr - Ssr - Sr")
            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt("Error", "Ingrese puesto: Jr - Ssr - Sr")

            # Punto A
            if genero == "NB":
                if tecnologia == "ASP.NET" or tecnologia == "JS" and puesto == "Ssr":
                    if edad > 24 and edad < 41:
                        contador_postulantes_no_binarios_a += 1

            # Punto B    
            if minimo_edad_jr is None or edad < minimo_edad_jr:
                minimo_edad_jr = edad
                jr_mas_joven = nombre

            # Punto C
            if genero == "F":
                acumulador_edades_femeninas += edad
                contador_postulantes_femeninas += 1
            elif genero == "M":
                acumulador_edades_masculinos += edad
                contador_postulantes_masculinos += 1
            elif genero == "NB":
                acumuldor_edades_no_binarios += edad
                contador_postulantes_no_binarios += 1

            # Punto D
            if tecnologia == "PYTHON":
                contador_postulates_python += 1
            elif tecnologia == "JS":
                contador_postulantes_js += 1
            elif tecnologia == "ASP.NET":
                contador_postulantes_asp_net += 1
            
            if contador_postulates_python > contador_postulantes_js:
                tecnologia_mas_popular = "PYTHON"
            elif contador_postulantes_js > contador_postulantes_asp_net:
                tecnologia_mas_popular = "JS"
            else:
                tecnologia_mas_popular = "ASP.NET"
        
        # Punto C
        if contador_postulantes_femeninas != 0:
            promedio_edad_femenino = acumulador_edades_femeninas / contador_postulantes_femeninas
            print("C - El promedio de edad femenino es: " + str(promedio_edad_femenino))
        else:
            print("C - No hay postulantes femeninas.")
        if contador_postulantes_masculinos != 0:
            promedio_edad_masculino = acumulador_edades_masculinos / contador_postulantes_masculinos
            print("C - El promedio de edad masculino es: " + str(promedio_edad_masculino))
        else:
            print("C - No hay postulantes masculinos.")
        if contador_postulantes_no_binarios != 0:
            promedio_edad_no_binario = acumuldor_edades_no_binarios / contador_postulantes_no_binarios
            print("C - El promedio de edad no binario es: " + str(promedio_edad_no_binario))
        else:
            print("C - No hay postulantes no binarios.")

        # Punto E
        porcentaje_ingresantes_femeninos = (contador_postulantes_femeninas * 100) / 10
        porcentaje_ingresantes_masculinos = (contador_postulantes_masculinos * 100) / 10
        porcentaje_ingresantes_no_binarios = (contador_postulantes_no_binarios * 100) / 10

        print("A - Cantidad de postulantes no binarios, 25 a 40 años, Ssr, ARP.NET o JS : " + str(contador_postulantes_no_binarios_a))

        print("B - La/el Jr mas joven es: " + jr_mas_joven)

        print("D - La tecnologia con mas postulantes es: " + tecnologia_mas_popular)

        print("E - El porcentaje de postulantes femeninos es: " + str(porcentaje_ingresantes_femeninos) + "%")
        print("E - El porcentaje de postulantes masculinos es: " + str(porcentaje_ingresantes_masculinos) + "%")
        print("E - El porcentaje de postulantes no binarios es: " + str(porcentaje_ingresantes_no_binarios) + "%")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
