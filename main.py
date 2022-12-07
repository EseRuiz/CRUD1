#programa de comunicacion sql3 lite con python, generando la #creacion en la base de datos principal, modificacion, #eliminacion y actualizacion en menu desplegable.
import sqlite3
from tabulate import tabulate

x = 0

db = sqlite3.connect("baseprueba.db")
cursor = db.cursor()

liscrud = [["#", "Opcion"], ["1", "Mostrar"], ["2", "Insertar"],
           ["3", "Eliminar"], ["4", "Actualizar"], ["5", "Salir"]]


def seleccionar():
  datos = cursor.execute("SELECT * FROM Padre")

  #obtener el primer dato
  print(cursor.fetchone())

  #obtener  todos los registros
  print(datos.fetchall())


def insertar():
  nombre = input("Ingrese nombre: ")
  apellido = input("Ingrese Apellido: ")
  registros = [(nombre, apellido)]
  cursor.executemany("INSERT INTO Padre (nombre,apellido) VALUES (?,?)",
                     registros)
  db.commit()


def eliminar():
  ida = input("Ingrese id a borrar: ")
  cursor.execute("DELETE FROM Padre WHERE {} like '%{}%'".format(
    "idPadre", ida))
  db.commit()


def actualizar():
  id = input("Ingrese id :")
  nombre2 = input("Ingrese nombre: ")
  cursor.execute("UPDATE Padre SET nombre = ? WHERE idPadre=?", (nombre2, id))
  db.commit()


while x < 1:
  print("")
  print(tabulate(liscrud, headers='firstrow'))
  print("")
  opcion = input("Ingrese Opcion : ")
  if opcion == "1":
    seleccionar()
  if opcion == "2":
    insertar()
  if opcion == "3":
    eliminar()
  if opcion == "4":
    actualizar()
  if opcion == "5":
    x = 2
    cursor.close()
