import tkinter as tk
from tkinter import messagebox
from servicio.calculadora_servicio import CalculadoraServicio

class CalculadoraInterfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.servicio =CalculadoraServicio()
        self.title("calculadora")
        self.geometry("300x400")
        