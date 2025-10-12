import faker
from conexion import Conexion

class Gustavo():
    def __init__(self):
        self.faker = faker.Faker('es_CL')
        db = Conexion()
        db.cursor.execute("DELETE FROM titulo_profesor")
        db.conn.commit()
        db.cursor.execute("DELETE FROM profesor_curso")
        db.conn.commit()
        db.cursor.execute("DELETE FROM profesor")
        db.conn.commit()
        db.cursor.execute("DELETE FROM titulo")
        db.conn.commit()
        
        db.cursor.execute("ALTER TABLE titulo_profesor AUTO_INCREMENT = 1")
        db.conn.commit()
        db.cursor.execute("ALTER TABLE profesor_curso AUTO_INCREMENT = 1")
        db.conn.commit()
        db.cursor.execute("ALTER TABLE titulo AUTO_INCREMENT = 1")
        db.conn.commit()
        db.cursor.execute("ALTER TABLE profesor AUTO_INCREMENT = 1")
        db.conn.commit()
        db.conn.close()
        
        
    def Titulo(self):
        titulo = self.faker.job()
        
        while True:
            db=Conexion()
            query = fr"SELECT nombre FROM titulo WHERE nombre='{titulo}'"
            db.cursor.execute(query)
            resultado = db.cursor.fetchall()
            db.conn.close()
            if len(resultado) == 0:
                break
            else:
                titulo = self.faker.job()
                
        
        db=Conexion()
        especialidad = self.faker.job()
        query = fr"INSERT INTO titulo (nombre,especialidad) VALUES ('{titulo}', '{especialidad}')"
        db.cursor.execute(query)
        db.conn.commit()
        db.conn.close()
        
    def Profesor(self):
        
        rut=self.faker.rut(max=25000000)
        
        while True:
            db=Conexion()
            db.cursor.execute("SELECT Rut_Profesor FROM profesor WHERE Rut_Profesor=%s", (rut))
            resultado = db.cursor.fetchall()
            db.conn.close()
            if len(resultado) == 0:
                break
            else:
                rut=self.faker.rut(max=25000000)
            
        nombres=self.faker.first_name()+" "+self.faker.first_name()
        apellido_p=self.faker.last_name()
        apellido_m=self.faker.last_name()
        correo = self.faker.email()
        
        db=Conexion()
        #query = fr"INSERT INTO profesor (rut, nombres, apellido_p, apellido_m, correo) VALUES ({rut}, '{nombres}', '{apellido_p}', '{apellido_m}', '{correo}')"
        db.cursor.execute("INSERT INTO profesor (Rut_Profesor, Nombre, Apellido_Paterno, Apellido_Materno, Correo) VALUES (%s, %s, %s, %s, %s)", (rut, nombres, apellido_p, apellido_m, correo))
        db.conn.commit()
        db.conn.close()
        self.ProfesorTitulo(rut, self.faker.random_int(min=1, max=4))
        
        
    def ProfesorTitulo(self, rut_profesor, cant_titulos):
        print(f"Asignandole Titulo a Profesor: {rut_profesor}")
        titulos=[]
        
        while len(titulos) < cant_titulos:
            db=Conexion()
            query = "SELECT ID_Titulo FROM titulo ORDER BY RAND() LIMIT 1"
            db.cursor.execute(query)
            resultado = db.cursor.fetchall()
            
            id_titulo = resultado[0]['ID_Titulo']
            fecha_obtencion = self.faker.date_between(start_date='-10y', end_date='today')
            if id_titulo not in titulos:
                titulos.append(id_titulo)
                #query = fr"INSERT INTO titulo_profesor (Rut_Profesor, ID_Titulo, Fecha_Agregado) VALUES ({rut_profesor}, {id_titulo}, '{fecha_obtencion}')"
                db.cursor.execute(fr"INSERT INTO titulo_profesor (ID_Titulo, Rut_Profesor, Fecha_Agregado) VALUES (%s, %s, %s)", (id_titulo,rut_profesor,fecha_obtencion))
                db.conn.commit()
                db.conn.close()
                
    def ProfesorCurso(self, id_curso):
        db=Conexion()
        
        
        query = "SELECT Rut_Profesor FROM profesor ORDER BY RAND() LIMIT 1"
        db.cursor.execute(query)
        resultado = db.cursor.fetchall()
        rut_profesor = resultado[0]['Rut_Profesor']
        
        query = fr"Select Año from curso where ID_Curso={id_curso}"
        db.cursor.execute(query)
        resultado = db.cursor.fetchall()
        año_curso = resultado[0]['Año']
        año_rango=self.faker.date_between(start_date="today", end_date='today').year - año_curso
        
        fecha_asignacion = self.faker.date_between(start_date=f'-{año_rango}y', end_date='today')
        db.cursor.execute("INSERT INTO profesor_curso (Rut_Profesor, ID_Curso, Fecha_Agregado) VALUES (%s, %s, %s)", (rut_profesor,id_curso, fecha_asignacion))
        
        db.conn.commit()
        db.conn.close()
        
        
        
                
                
        
        
        



#g=Gustavo()
#print("Creando Titulos...")
#for i in range(50):
#    g.Titulo()
#print("Creando Profesores...")
#for j in range(100):
#    g.Profesor()







