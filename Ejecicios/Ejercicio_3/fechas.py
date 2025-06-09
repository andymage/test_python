from datetime import *

def day_of_week(fecha): # Funcion para obtener el dia de la semana
    day_name = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado","Domingo"]
    day = datetime.strptime(fecha, '%Y-%m-%d').date()
    return day_name[day.isoweekday()-1]



day = day_of_week("2025-06-08")
print(day)