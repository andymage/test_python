# Examen de Python

### Instrucciones

- El examen tiene una duración aproximada de **2 horas**.
- Lee las preguntas cuidadosamente y asegúrate de entender lo que se te pide antes de comenzar.
- Resuelve los ejercicios de manera ordenada y comentada, explicando tu razonamiento cuando sea necesario.
- Puedes usar cualquier recurso en línea para resolver el examen, pero no debes copiar código de otras fuentes sin comprensión.
- Al finalizar, genera un Pull Request para revisar tu examen.

### Requisitos

- Tener Python 3.x instalado.
- Familiaridad con el uso de bibliotecas estándar de Python como `datetime`, `os`, `json`, `collections`, etc.

---

## Ejercicios

### Ejercicio 1: Manejo de Archivos

Escribe una función que reciba como parámetro el nombre de un archivo de texto. La función debe leer el archivo, contar cuántas veces aparece una palabra específica y devolver el número de veces que aparece dicha palabra.

**Entrada**:
- El nombre de un archivo de texto (`.txt`).
- Una palabra para buscar dentro del archivo.

**Salida**:
- Un entero que indique el número de veces que la palabra aparece en el archivo.

---

### Ejercicio 2: Programación Orientada a Objetos

Crea una clase llamada `Empleado` que contenga los siguientes atributos:

- `nombre`: el nombre del empleado.
- `salario`: el salario del empleado.
- `fecha_contratacion`: la fecha en que fue contratado el empleado (en formato `YYYY-MM-DD`).

La clase debe tener los siguientes métodos:

- `__str__`: un método que devuelva una representación en cadena de la instancia de `Empleado` (nombre y salario).
- `aniversario`: un método que calcule el número de años que el empleado ha trabajado en la empresa a partir de la fecha de contratación. La fecha de hoy debe ser utilizada para hacer el cálculo.

---

### Ejercicio 3: Manejo de Fechas

Escribe una función que reciba una fecha en formato `YYYY-MM-DD` como cadena y devuelva el día de la semana correspondiente (por ejemplo, "Lunes", "Martes", etc.).

**Entrada**:
- Una cadena que representa una fecha en formato `YYYY-MM-DD`.

**Salida**:
- El nombre del día de la semana correspondiente a la fecha ingresada.

---

### Ejercicio 4: Uso de Estructuras de Datos

Dada una lista de números enteros, escribe una función que devuelva el número que más veces se repite en la lista. Si hay varios números con la misma cantidad de repeticiones, devuelve el más pequeño.

**Entrada**:
- Una lista de números enteros.

**Salida**:
- El número que más veces se repite. Si hay varios, devuelve el más pequeño.

---

### Ejercicio 5: JSON

Escribe una función que reciba un archivo `.json` que contenga una lista de diccionarios. Cada diccionario representa a un estudiante con los siguientes atributos: `nombre`, `edad`, `calificaciones`. La función debe devolver el promedio de las calificaciones de todos los estudiantes.

**Entrada**:
- Un archivo `.json` con la siguiente estructura:
  ```json
  [
    {
      "nombre": "Juan",
      "edad": 20,
      "calificaciones": [90, 80, 70]
    },
    {
      "nombre": "Ana",
      "edad": 22,
      "calificaciones": [85, 90, 95]
    }
  ]
