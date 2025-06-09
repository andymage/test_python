from datetime import *

class Empleado:
    def __init__(self, empleado:str,salario:float, fecha_contrat:str): # Se definen los argumentos para la Clase
        self.empleado = empleado
        self.salario = salario
        self.fecha_contrat = datetime.strptime(fecha_contrat, '%Y-%m-%d').date()
    
    def __str__(self): 
        return f"Datos\nEmpleado: {self.empleado}\nSalario: {self.salario}"
    
    def aniversario(self):
        today = date.today()
        return today.year - self.fecha_contrat.year
    
em1 = Empleado("Ernesto",1300,"2013-12-12")
print(em1)
print(f"Años que el empleado ha trabajado: ",em1.aniversario())