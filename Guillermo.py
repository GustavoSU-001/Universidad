import mysql.connector
from faker import Faker
import random
import pymysql


fake = Faker('es_CL')



# Conexión a la base de datos
db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_universidad"
)

cursor = db.cursor()


#----------------------------- RUT ALUMNO -----------------------------

# class runPersona:
#     def __init__(self,numero=None):
#         self.numero = numero or random.randint(1_000_000,25_000_000)
#         self.dv = self.calcular_dv()

#     def calcular_dv(self):
#         rut_str = str(self.numero)
#         suma = 0
#         multiplo = 2
#         for digito in reversed(rut_str):
#             suma += int(digito) * multiplo
#             multiplo = 2 if multiplo == 7 else multiplo + 1
#         resto = 11 - (suma % 11)
#         if resto == 11:
#             resto = '0'
#         elif resto == 10:
#             return 'k'
#         else:
#             return str(resto)
#     def __str__(self):
#         return f"{self.Formatear_rut()}"
#     def Formatear_rut(self):
#         rut_str= f"{self.numero:,}".replace(",",".")
#         return f"{rut_str}-{self.dv}"
#     def sin_formato(self):
#         return f"{self.numero}-{self.dv}"



# # Generar y agregar 10 alumnos falsos
# for _ in range(10):
#     rutFormateado=runPersona()
#     estadoInsertado=True
#     while estadoInsertado:
#         cursor.execute("SELECT * FROM alumno WHERE rut =%s",(rutFormateado))
#         if(cursor.fetchone()):
#             print("Existe Run Persona")
#             rutFormateado=runPersona()
#         else:
#             estadoInsertado=False
#     nombre = fake.first_name()
#     apellido = fake.last_name()
#     correo = fake.email()
#     telefono = fake.phone_number()
#     # Ajusta los campos según tu tabla , es lo que pondremos en la tabla tienen que tener el mismo nombre 
#     cursor.execute(
#         "INSERT INTO alumno (rut, nombre, apellido, correo,telefono) VALUES (%s, %s, %s, %s,%s)",
#         (rutFormateado, nombre, apellido, correo,telefono))
#     db.commit()
# print("Insertados 10 alumnos")

#-----------------------------------------------------------------------

# ----------------------------- CURSO ALUMNO -----------------------------

#Obtener todos los ID_Curso válidos   

# cursor.execute("SELECT ID_Curso FROM curso")
# cursos_disponibles = [row[0] for row in cursor.fetchall()]

# # Obtener todos los rut válidos
# cursor.execute("SELECT rut FROM alumno")
# alumnos_disponibles = [row[0] for row in cursor.fetchall()]

# # Insertar 10 relaciones en curso_alumno usando FKs
# for _ in range(10):
#     ID_Curso = random.choice(cursos_disponibles)
#     rut = random.choice(alumnos_disponibles)
#     Fecha = fake.date_time()
#     cursor.execute(
#         "INSERT INTO curso_alumno (ID_Curso, Rut_Alumno, Fecha_agregado) VALUES (%s, %s, %s)",
#         (ID_Curso, rut, Fecha)
#     )
#     db.commit()

# print("Insertadas 10 relaciones en curso_alumno")

#-----------------------------------------------------------------------


#----------------------------- EVALUACION -----------------------------

# Obtener todos los ID_Curso válidos
# cursor.execute("SELECT ID_Curso_Alumno FROM Curso_Alumno")
# cursos_disponibles = [row[0] for row in cursor.fetchall()]


# # Insertar 10 relaciones en curso_alumno usando FKs
# for _ in range(10):
#     ID_Curso = random.choice(cursos_disponibles)
#     Fecha=fake.date_time()
#     ponderacion=fake.random_number(digits=2)
#     puntaje=fake.random_int(min=1,max=70)
#     nota=fake.random_int(min=1,max=7)
#     Fecha = fake.date_time()
#     cursor.execute(
#         "INSERT INTO evaluacion (ID_Curso_Alumno, Fecha, Ponderacion,Puntaje,Nota) VALUES (%s, %s, %s,%s, %s)",
#         (ID_Curso,Fecha, ponderacion,puntaje,nota)
#     )
#     db.commit()
# print("Insertadas 10 relaciones en evaluacion")

#------------------------------ Tipo Clase -----------------------------

# Nombre=["Online, Offline","Curso","Seminario","Taller","Proyecto"]

# for _in in range(10):
#     nombre=random.choice(Nombre)
#     cursor.execute(
#         "INSERT INTO tipo_clase (Nombre) VALUES (%s)",
#         (nombre)
#     )
#     db.commit()

# print("Insertadas 10 relaciones en tipo_clase")


#----------------------------- Curso_TipoClase -----------------------------

#obtener todos los ID_Curso válidos   
# cursor.execute("SELECT ID_Curso FROM curso")
# cursos_disponibles = [row[0] for row in cursor.fetchall()]

# #obtener todos los tipo clase válidos
# cursor.execute("SELECT ID_Tipo_Clase FROM tipo_clase")
# tipos_disponibles = [row[0] for row in cursor.fetchall()]

# #insertar 10 relaciones en tipo_clase
# for _ in range(10):
#     ID_Curso = random.choice(cursos_disponibles)
#     Tipo_clase = random.choice(tipos_disponibles)
#     Horas = fake.random_int(min=1,max=3)
#     cursor.execute(
#         "INSERT INTO curso_tipo_clase(ID_Tipo_Clase,ID_Curso,Horas) VALUES (%s, %s,%s)",
#         (Tipo_clase,ID_Curso,Horas)
#     )
#     db.commit()
# print("Insertadas 10 relaciones en curso_tipo_clase")