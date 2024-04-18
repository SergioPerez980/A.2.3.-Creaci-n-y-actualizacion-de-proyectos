import pymongo

# Connect to MongoDB and create database connection (place this before the function)
cliente = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your connection URI if necessary
db = cliente["Escuela"]

def insertar_documento(db):  # Pass 'db' as an argument
    nombre = input("Ingrese el nombre de la materia: ")
    descripcion = input("Ingrese la descripción de la materia: ")
    profesor = input("Ingrese el nombre del profesor: ")

    # Crear el documento
    materia = {
        "nombre": nombre,
        "descripcion": descripcion,
        "profesor": profesor
    }

    # Insertar el documento en la colección (correct usage of 'db')
    db.Materia.insert_one(materia)
    print("Documento insertado correctamente")

# ... (Rest of your code)

while True:
    opcion = input("¿Desea agregar un nuevo documento? (s/n): ")
    if opcion.lower() == "s":
        insertar_documento(db)  # Pass the 'db' object when calling the function
    else:
        print("Saliendo del programa...")
        break

