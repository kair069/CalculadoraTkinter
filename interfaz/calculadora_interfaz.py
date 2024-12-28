import tkinter as tk
from tkinter import messagebox
from servicio.calculadora_servicio import CalculadoraServicio

class CalculadoraInterfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.servicio =CalculadoraServicio()
        self.title("calculadora")
        self.geometry("300x400")

    def realizar_calculo(self):
        try:
            a = float(self.entrada1.get())
            b = float(self.entrada2.get())
            operacion = self.operacion_var.get()
            resultado = self.servicio.calcular(operacion,a,b)
            self.resultado_label.config(text=f"resultado: {resultado}")
        except:
            messagebox.showerror("error","entrada no valida")


    def crear_widget(self):
        self.entrada1 = tk.Entry(self)
        self.entrada1.pack(pady=10)

        self.entrada2 = tk.Entry(self)
        self.entrada2.pack(pady=10)

        self.operacion_var = tk.StringVar(value="suma")

        opciones = ["suma","resta","multiplicacion","division"]
        for op in opciones:
            tk.Radiobutton(self,text=op,variable=self.operacion_var,value=op)
        tk.Button(self,text="Calcular",command=self.realizar_calculo).pack(pady=10)
        self.resultado_label = tk.Label(self,text="resultado")
        self.resultado_label.pack(pady=10)    

        