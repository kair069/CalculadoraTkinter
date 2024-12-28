from  logica.calculadora_logica import CalculadoraLogica

class CalculadoraServicio:
    def __init__(self):
        self.logica = CalculadoraLogica()
    
    def calcular(self,operacion,a,b):
        if operacion == 'suma':
            return self.logica.suma(a,b)    
        
        



