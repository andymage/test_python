import json

def access_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        for val in data:
            val['promedio'] = sum(val['calificaciones']) / len(val['calificaciones'])
    with open("output.json", "w") as out:
        json.dump(data, out, indent=4)

ruta_archivo_ejemplo = "input.json"
access_json(ruta_archivo_ejemplo)