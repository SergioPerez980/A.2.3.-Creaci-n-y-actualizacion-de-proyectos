import pymongo

# Conexión a la base de datos
cliente = pymongo.MongoClient("mongodb://localhost:27017/")  # Cambiar la URL de conexión si es necesario
db = cliente["Escuela"]  # Seleccionar la base de datos "Escuela"

# Verificar la conexión
print(db.list_collections())  # Muestra las colecciones existentes en la base de datos

# Crear la colección "Materia" si no existe
if "Materia" not in db.list_collections():
    db.create_collection("Materia")
    print("Colección 'Materia' creada")

# Interacciones con la colección "Materia"
# (Agregar, eliminar, modificar, consultar documentos)

# Ejemplo: Insertar un documento en la colección "Materia"
materia = {
    "nombre": "Matemáticas",
    "descripcion": "Curso de matemáticas básicas",
    "profesor": "Juan Pérez"
}

db.Materia.insert_one(materia)
print("Documento insertado correctamente")


# ... (Agregar más ejemplos de interacciones con la colección)
