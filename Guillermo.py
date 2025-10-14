from datetime import date
import mysql.connector
from faker import Faker
import random
import pymysql
from conexion import Conexion

fake = Faker('es_CL')



# Conexión a la base de datos
#db = pymysql.connect(
#    host="localhost",
#    user="root",
#    password="",
#    database="bd_uni"
#)

#cursor = db.cursor()


#----------------------------- RUT ALUMNO -----------------------------

class runPersona:
    def __init__(self,numero=None):
        self.numero = numero or random.randint(1_000_000,25_000_000)
        self.dv = self.calcular_dv()
        

    def calcular_dv(self):
        rut_str = str(self.numero)
        suma = 0
        multiplo = 2
        for digito in reversed(rut_str):
            suma += int(digito) * multiplo
            multiplo = 2 if multiplo == 7 else multiplo + 1
        resto = 11 - (suma % 11)
        if resto == 11:
            resto = '0'
        elif resto == 10:
            return 'k'
        else:
            return str(resto)
    def __str__(self):
        return f"{self.Formatear_rut()}"
    def Formatear_rut(self):
        rut_str= f"{self.numero:,}".replace(",",".")
        rut=f"{rut_str}-{self.dv}"
        return rut
    def sin_formato(self):
        
        return f"{self.numero}-{self.dv}"
print("Limpiando tablas relacionadas con Alumno...")
db=Conexion()
db.cursor.execute("DELETE FROM evaluacion")
db.conn.commit()
db.cursor.execute("DELETE FROM curso_alumno")
db.conn.commit()
db.cursor.execute("DELETE FROM curso_tipo_clase")
db.conn.commit()
db.cursor.execute("DELETE FROM alumno")
db.conn.commit()
db.cursor.execute("DELETE FROM tipo_clase")
db.conn.commit()
db.cursor.execute("Alter TABLE evaluacion AUTO_INCREMENT = 1")
db.conn.commit()
db.cursor.execute("Alter TABLE curso_alumno AUTO_INCREMENT = 1")
db.conn.commit()
db.cursor.execute("Alter TABLE curso_tipo_clase AUTO_INCREMENT = 1")
db.conn.commit()
db.cursor.execute("Alter TABLE alumno AUTO_INCREMENT = 1")
db.conn.commit()
db.cursor.execute("Alter TABLE tipo_clase AUTO_INCREMENT = 1")
db.conn.commit()
db.conn.close()


# Generar y agregar 10 alumnos falsos
def Alumnos():
    db=Conexion()
    rutFormateado=fake.rut(max=25000000)  #runPersona()
    estadoInsertado=True
    while estadoInsertado:
        db.cursor.execute("SELECT * FROM alumno WHERE rut =%s",(rutFormateado))
        respuesta=db.cursor.fetchone()
        if(respuesta):
            rutFormateado=fake.rut(min=1000000,max=25000000)#runPersona()
        else:
            estadoInsertado=False
    
    nombre = fake.first_name()
    apellido = fake.last_name()
    correo = fake.email()
    telefono = fake.phone_number()
    # Ajusta los campos según tu tabla , es lo que pondremos en la tabla tienen que tener el mismo nombre 
    db.cursor.execute(
        "INSERT INTO alumno (rut, nombre, apellido, correo,telefono) VALUES (%s, %s, %s, %s,%s)",
        (rutFormateado, nombre, apellido, correo,telefono))
    db.conn.commit()
    db.conn.close()
print("Creando Alumnos...")
for _ in range(10500):
    Alumnos()

#-----------------------------------------------------------------------

# ----------------------------- CURSO ALUMNO -----------------------------

def Curso_Alumno(id_curso):
    db=Conexion()
    #Obtener todos los ID_Curso válidos   

    db.cursor.execute("SELECT Capacidad_Max, Año FROM curso WHERE ID_Curso=%s", (id_curso))
    #cursos_disponibles = [row[0] for row in cursor.fetchall()]
    datos=db.cursor.fetchall()[0]
    disponibles,año = datos['Capacidad_Max'],datos['Año']
    disponibles_diferencia=disponibles-random.randint(1,int(disponibles/2))

    alumnos = []
    
    while len(alumnos) < disponibles_diferencia:
        # Obtener todos los rut válidos
        db.cursor.execute("SELECT rut FROM alumno ORDER BY RAND() LIMIT 1")
        a=db.cursor.fetchall()[0]["rut"]
        
        if a not in alumnos:
            alumnos.append(a)
        #alumnos_disponibles = [row[0] for row in cursor.fetchall()]
    

    # Insertar 10 relaciones en curso_alumno usando FKs
    for a in alumnos:
        #ID_Curso = random.choice(cursos_disponibles)
        #rut = random.choice(alumnos_disponibles)
        Fecha = fake.date_time_between(start_date='-1y', end_date=año)
        db.cursor.execute(
            "INSERT INTO curso_alumno (ID_Curso, Rut_Alumno, Fecha_agregado) VALUES (%s, %s, %s)",
            (id_curso, a, Fecha)
        )
        db.conn.commit()
        id_curso_alumno=db.cursor.lastrowid
        evaluacion(id_curso_alumno,año)
    db.conn.close()
        
#Curso_Alumno(1)

#-----------------------------------------------------------------------


#----------------------------- EVALUACION -----------------------------

# Obtener todos los ID_Curso válidos
#cursor.execute("SELECT ID_Curso_Alumno FROM Curso_Alumno")
#cursos_disponibles = [row[0] for row in cursor.fetchall()]

def evaluacion(id_curso_alumno,año):
# Insertar 10 relaciones en curso_alumno usando FKs
#for _ in range(10):
    db=Conexion()
    ID_Curso = id_curso_alumno#random.choice(cursos_disponibles)
    for _ in range(4):
        f_i=date(año,1,1)
        f_f=date(año,12,31)
        Fecha=fake.date_time_between(start_date=f_i,end_date=f_f)
        ponderacion=fake.random_number(digits=2)
        puntaje=fake.random_int(min=1,max=70)
        nota=fake.random_int(min=1,max=7)
        Fecha = fake.date_time()
        db.cursor.execute(
            "INSERT INTO evaluacion (ID_Curso_Alumno, Fecha, Ponderacion,Puntaje,Nota) VALUES (%s, %s, %s,%s, %s)",
            (ID_Curso,Fecha, ponderacion,puntaje,nota)
        )
        db.conn.commit()
    db.conn.close()
    
    

#------------------------------ Tipo Clase -----------------------------
def Tipo_Clase():
    db=Conexion()
    Nombre=["Online, Offline","Curso","Seminario","Taller","Proyecto"]

    for nombre in Nombre:
    #nombre=random.choice(Nombre)
        db.cursor.execute(
            "INSERT INTO tipo_clase (Nombre) VALUES (%s)",
            (nombre)
        )
    db.conn.commit()
    db.conn.close()
print("Creando Tipo de Clases...")
Tipo_Clase()

#----------------------------- Curso_TipoClase -----------------------------

#obtener todos los ID_Curso válidos   
#cursor.execute("SELECT ID_Curso FROM curso")
#cursos_disponibles = [row[0] for row in cursor.fetchall()]

def Curso_TipoClase(id_curso):
    #cursor.execute("SELECT ID_Curso FROM curso")
    #cursos_disponibles = [row[0] for row in cursor.fetchall()]
    # #obtener todos los tipo clase válidos
    db=Conexion()
    db.cursor.execute("SELECT ID_Tipo_Clase FROM tipo_clase")
    tipos_disponibles = [row["ID_Tipo_Clase"] for row in db.cursor.fetchall()]

    # #insertar 10 relaciones en tipo_clase
    #for _ in range(10):
    ID_Curso = id_curso#random.choice(cursos_disponibles)
    Tipo_clase = random.choice(tipos_disponibles)
    Horas = fake.random_int(min=1,max=3)
    db.cursor.execute(
        "INSERT INTO curso_tipo_clase(ID_Tipo_Clase,ID_Curso,Horas) VALUES (%s, %s,%s)",
        (Tipo_clase,ID_Curso,Horas)
    )
    db.conn.commit()