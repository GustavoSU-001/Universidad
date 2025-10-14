import pymysql
import random
from faker import Faker
from Gustavo import Gustavo
import Guillermo
from datetime import date

faker = Faker('es_CL')

# Conexión a la base de datos
db = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_uni',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = db.cursor()

#Limpieza de tabla titulo_profesor
cursor.execute('DELETE FROM profesor_curso')
cursor.execute('ALTER TABLE profesor_curso AUTO_INCREMENT = 1')
db.commit()

#Limpieza de tabla Evaluacion
cursor.execute('DELETE FROM evaluacion')
cursor.execute('ALTER TABLE evaluacion AUTO_INCREMENT = 1')
db.commit()


# Limpieza de tabla Curso Alumno
cursor.execute('DELETE FROM curso_alumno')
cursor.execute('ALTER TABLE curso_alumno AUTO_INCREMENT = 1')
db.commit()

#Limpieza de tabla curso tipo clase
cursor.execute('DELETE FROM curso_tipo_clase')
cursor.execute('ALTER TABLE curso_tipo_clase AUTO_INCREMENT = 1')
db.commit()

#limpieza de tabla curso sala
cursor.execute('DELETE FROM curso_sala')
cursor.execute('ALTER TABLE curso_sala AUTO_INCREMENT = 1')
db.commit()

# Limpieza de tabla curso
cursor.execute('DELETE FROM curso')
cursor.execute('ALTER TABLE curso AUTO_INCREMENT = 1')
db.commit()

# Limpieza de tabla carrera
cursor.execute('DELETE FROM carrera')
cursor.execute('ALTER TABLE carrera AUTO_INCREMENT = 1')
db.commit()

# Lista de carreras 
lista_carreras = [
    # Administración y Servicios
    "Administración de Empresas", "Administración de Empresas Online", "Comercio Exterior",
    "Comercio Exterior Online", "Contabilidad General", "Técnico en Administración Pública",
    "Técnico en Administración Pública Online", "Administración Pública Online", "Contador Público",
    "Ingeniería en Administración de Empresas", "Ingeniería en Administración de Empresas Online",
    "Ingeniería en Comercio Exterior", "Ingeniería en Comercio Exterior Online",
    "Gastronomía", "Administración Gastronómica",
    "Técnico en Enfermería", "Técnico en Farmacia", "Técnico en Odontología",
    "Gestión Turística", "Hotelería y Servicios", "Ingeniería en Gestión Turística",

    # Energía y Sostenibilidad
    "Tecnología en Análisis Químico", "Técnico Agrícola", "Técnico en Medioambiente y Sustentabilidad",
    "Ingeniería Agrícola", "Ingeniería en Medioambiente y Sustentabilidad",
    "Técnico en Construcción", "Técnico en Topografía y Geomática", "Construcción Civil",
    "Ingeniería en Geomensura y Geomática", "Técnico en Climatización y Refrigeración",
    "Técnico en Energías Renovables", "Ingeniería en Climatización y Refrigeración", "Ingeniería en Energía",

    # Mantención y Logística
    "Técnico en Logística", "Ingeniería en Logística", "Mecánica Automotriz en Maquinaria Pesada",
    "Técnico en Mantenimiento Industrial", "Técnico en Mecatrónica", "Técnico en Mecánica y Electromovilidad Automotriz",
    "Ingeniería en Mantenimiento Industrial", "Ingeniería en Maquinaria Pesada y Vehículos Automotrices",
    "Ingeniería en Mecatrónica", "Ingeniería en Mecánica y Electromovilidad Automotriz",
    "Técnico en Mantenimiento de Plantas Mineras", "Técnico en Metalurgia Extractiva", "Técnico en Minería",
    "Técnico en Prevención de Riesgos y Gestión de Emergencias", "Ingeniería en Mantenimiento de Plantas Mineras",
    "Ingeniería en Metalurgia", "Ingeniería en Minas",

    # Tecnología Aplicada
    "Técnico en Automatización y Robótica", "Ingeniería en Automatización y Robótica",
    "Animación Digital y Videojuegos", "Diseño Digital y Web", "Producción de Moda y Tecnología",
    "Diseño Digital Profesional", "Diseño de Moda Profesional", "Electrónica",
    "Técnico en Electricidad Industrial", "Técnico en Telecomunicaciones y Servicios Digitales",
    "Ingeniería Eléctrica", "Ingeniería en Electrónica y Sistemas Inteligentes",
    "Ingeniería en Telecomunicaciones y Servicios Digitales", "Analista Programador",
    "Ingeniería en Ciberseguridad", "Ingeniería en Informática"
]

# Insertar carreras
for nombre in lista_carreras:
    semestre_total = random.choice([4, 8])
    fecha_impartida = faker.date_time_between(start_date='-5y', end_date='now')
    cursor.execute(
        "INSERT INTO carrera (Nombre, Semestre_Total, Fecha_Impartida) VALUES (%s, %s, %s)",
        (nombre, semestre_total, fecha_impartida)
    )
db.commit()

print("Carreras insertadas correctamente.")

import pymysql
import random
from faker import Faker

faker = Faker('es_CL')

# Conexión a la base de datos
db = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_uni',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = db.cursor()



# Diccionario de especialidades por carrera
especialidades = {
    "Administración y Servicios": [
        "Administración de Empresas", "Administración de Empresas Online", "Comercio Exterior",
        "Comercio Exterior Online", "Contabilidad General", "Técnico en Administración Pública",
        "Técnico en Administración Pública Online", "Administración Pública Online", "Contador Público",
        "Ingeniería en Administración de Empresas", "Ingeniería en Administración de Empresas Online",
        "Ingeniería en Comercio Exterior", "Ingeniería en Comercio Exterior Online",
        "Gastronomía", "Administración Gastronómica",
        "Técnico en Enfermería", "Técnico en Farmacia", "Técnico en Odontología",
        "Gestión Turística", "Hotelería y Servicios", "Ingeniería en Gestión Turística"
    ],
    "Energía y Sostenibilidad": [
        "Tecnología en Análisis Químico", "Técnico Agrícola", "Técnico en Medioambiente y Sustentabilidad",
        "Ingeniería Agrícola", "Ingeniería en Medioambiente y Sustentabilidad",
        "Técnico en Construcción", "Técnico en Topografía y Geomática", "Construcción Civil",
        "Ingeniería en Geomensura y Geomática", "Técnico en Climatización y Refrigeración",
        "Técnico en Energías Renovables", "Ingeniería en Climatización y Refrigeración", "Ingeniería en Energía"
    ],
    "Mantención y Logística": [
        "Técnico en Logística", "Ingeniería en Logística", "Mecánica Automotriz en Maquinaria Pesada",
        "Técnico en Mantenimiento Industrial", "Técnico en Mecatrónica", "Técnico en Mecánica y Electromovilidad Automotriz",
        "Ingeniería en Mantenimiento Industrial", "Ingeniería en Maquinaria Pesada y Vehículos Automotrices",
        "Ingeniería en Mecatrónica", "Ingeniería en Mecánica y Electromovilidad Automotriz",
        "Técnico en Mantenimiento de Plantas Mineras", "Técnico en Metalurgia Extractiva", "Técnico en Minería",
        "Técnico en Prevención de Riesgos y Gestión de Emergencias", "Ingeniería en Mantenimiento de Plantas Mineras",
        "Ingeniería en Metalurgia", "Ingeniería en Minas"
    ],
    "Tecnología Aplicada": [
        "Robótica",
        "Animación Digital y Videojuegos", "Diseño Digital y Web", "Producción de Moda y Tecnología",
        "Diseño Digital Profesional", "Diseño de Moda Profesional", "Electrónica",
        "Técnico en Electricidad Industrial", "Técnico en TelecomuniTécnico en Automatización y Robótica", "Ingeniería en Automatización y Rcaciones y Servicios Digitales",
        "Ingeniería Eléctrica", "Ingeniería en Electrónica y Sistemas Inteligentes",
        "Ingeniería en Telecomunicaciones y Servicios Digitales", "Analista Programador",
        "Ingeniería en Ciberseguridad", "Ingeniería en Informática"
    ]
}

# Asignaturas por especialidad
asignaturas_por_especialidad = {
    "Administración y Servicios": [
        "Introducción a la Administración", "Fundamentos de Economía", "Contabilidad General", "Matemáticas Financieras",
        "Estadística Aplicada", "Derecho Empresarial", "Fundamentos de Marketing", "Ética Profesional y Responsabilidad Social",
        "Administración Financiera", "Microeconomía", "Macroeconomía", "Comportamiento Organizacional",
        "Administración de Recursos Humanos", "Planeación Estratégica", "Dirección y Liderazgo", "Gestión de Operaciones",
        "Gestión de Calidad Total", "Administración de la Producción", "Administración de Servicios", "Gestión de Proyectos",
        "Innovación y Gestión del Cambio", "Desarrollo Organizacional", "Contabilidad de Costos", "Finanzas Corporativas",
        "Presupuestos Empresariales", "Evaluación de Proyectos", "Auditoría Administrativa", "Tributación Empresarial",
        "Marketing de Servicios", "Investigación de Mercados", "Gestión de la Experiencia del Cliente (CX)",
        "Comunicación Corporativa", "Atención y Servicio al Cliente", "Técnicas de Ventas y Negociación",
        "Sistemas de Información Gerencial", "Herramientas Digitales para la Gestión", "Comercio Electrónico",
        "Transformación Digital en Servicios", "Análisis de Datos para la Toma de Decisiones", "Entorno Económico Global",
        "Negocios Internacionales", "Administración Intercultural", "Gestión de la Sostenibilidad",
        "Responsabilidad Social Empresarial", "Gestión de Servicios Turísticos", "Gestión de Servicios de Salud",
        "Gestión Hotelera", "Protocolo y Organización de Eventos", "Logística y Cadena de Suministro",
        "Emprendimiento y Creación de Empresas"
    ],
    "Energía y Sostenibilidad": [
        "Fundamentos de Energía", "Física General", "Química General", "Matemáticas Aplicadas a la Ingeniería",
        "Termodinámica", "Mecánica de Fluidos", "Electrotecnia", "Fundamentos de Sustentabilidad",
        "Ciencia de los Materiales", "Estadística y Análisis de Datos", "Energías Renovables",
        "Energía Solar Fotovoltaica", "Energía Solar Térmica", "Energía Eólica", "Energía Hidráulica",
        "Biomasa y Biocombustibles", "Geotermia", "Energía Mareomotriz y Undimotriz", "Energía Nuclear y Seguridad",
        "Sistemas Híbridos de Energía", "Almacenamiento de Energía", "Redes Inteligentes (Smart Grids)",
        "Eficiencia Energética", "Electrificación Rural y Acceso Universal", "Sistemas Fotovoltaicos Aislados y Conectados",
        "Diseño de Sistemas Energéticos", "Energía y Transporte Sostenible", "Automatización y Control de Sistemas Energéticos",
        "Evaluación del Impacto Ambiental", "Gestión Ambiental", "Economía Circular",
        "Cambio Climático y Políticas Ambientales", "Huella de Carbono y Energía", "Restauración de Ecosistemas",
        "Gobernanza y Desarrollo Sostenible", "Economía de la Energía", "Políticas Energéticas y Ambientales",
        "Legislación Energética y Ambiental", "Mercados Energéticos", "Transición Energética Justa",
        "Financiación de Proyectos Energéticos", "Regulación de Servicios Públicos", "Gestión de Proyectos Energéticos",
        "Innovación Tecnológica en Energía", "Modelado y Simulación de Sistemas Energéticos",
        "Emprendimiento en Energía y Sostenibilidad", "Planificación Energética", "Análisis de Ciclo de Vida (ACV)",
        "Educación y Cultura para la Sostenibilidad", "Auditoría Energética"
    ],
    "Mantención y Logística": [
        "Fundamentos de Mantenimiento", "Mantenimiento Preventivo y Correctivo", "Mantenimiento Predictivo",
        "Gestión de Mantenimiento", "Fiabilidad y Disponibilidad de Equipos", "Lubricación y Tribología",
        "Técnicas de Inspección y Diagnóstico", "Planificación y Programación del Mantenimiento",
        "Mantenimiento Mecánico", "Mantenimiento Eléctrico", "Electromecánica", "Neumática e Hidráulica",
        "Automatización Industrial", "Instrumentación y Control de Procesos", "Tecnología de Materiales",
        "Diagnóstico de Fallas", "Gestión de Repuestos y Herramientas",
        "Sistemas de Gestión de Mantenimiento Asistido por Computadora (CMMS)", "Seguridad Industrial en Mantención",
        "Normativas Técnicas y Estándares de Calidad", "Logística de Abastecimiento", "Logística de Distribución",
        "Gestión de la Cadena de Suministro (Supply Chain Management)", "Almacenamiento y Gestión de Inventarios",
        "Transporte y Distribución", "Logística Inversa", "Embalaje y Manejo de Materiales",
        "Infraestructura y Equipamiento Logístico", "Costos Logísticos", "Gestión de Operaciones",
        "Lean Manufacturing", "Mejora Continua (Kaizen)", "Teoría de Restricciones (TOC)",
        "Gestión de Calidad Total (TQM)", "Six Sigma", "Indicadores de Gestión (KPIs)",
        "Logística Internacional y Comercio Exterior", "Planificación de la Demanda",
        "Gestión de Proyectos en Logística y Mantenimiento", "Habilidades Directivas", "Comunicación Efectiva",
        "Liderazgo y Trabajo en Equipo", "Legislación Laboral y Normas de Seguridad",
        "Sistemas ERP (SAP, Oracle, etc.)", "Sustentabilidad en Logística y Mantenimiento", "Ética Profesional",
        "Responsabilidad Social Empresarial", "Innovación y Tecnología Aplicada", "Emprendimiento Técnico"
    ],
    "Tecnología Aplicada": [
        "Fundamentos de Programación", "Programación Orientada a Objetos", "Estructura de Datos y Algoritmos",
        "Desarrollo Web (Frontend y Backend)", "Bases de Datos", "Programación en Python", "Programación en C/C++",
        "Desarrollo de Aplicaciones Móviles", "Desarrollo de Software Embebido", "Seguridad Informática y Ciberseguridad",
        "Fundamentos de Robótica", "Robótica Industrial", "Robótica Móvil y Autónoma",
        "Programación de Robots (ROS, Arduino, etc.)", "Sensores y Actuadores", "Controladores Lógicos Programables (PLC)",
        "Visión Artificial", "Drones y Vehículos Autónomos", "Mecatrónica", "Diseño e Impresión 3D",
        "Electrónica Analógica", "Electrónica Digital", "Microcontroladores y Microprocesadores",
        "Circuitos Electrónicos", "Diseño de PCBs", "Internet de las Cosas (IoT)", "Instrumentación Electrónica",
        "Energía y Electrónica de Potencia", "Sistemas Embebidos", "Automatización Domótica",
        "Fundamentos de Telecomunicaciones", "Redes de Datos", "Protocolos de Comunicación",
        "Comunicaciones Inalámbricas", "5G y Redes de Nueva Generación", "Redes Ópticas y Fibra",
        "Comunicación Satelital", "Sistemas de Transmisión Digital", "Antenas y Propagación",
        "Ciberseguridad en Redes", "Fundamentos de Inteligencia Artificial", "Machine Learning", "Deep Learning",
        "Visión por Computadora", "Big Data y Analítica Avanzada", "Procesamiento de Lenguaje Natural (NLP)",
        "Ética e IA Responsable", "Sistemas Expertos", "Arquitecturas de Computación Distribuida (Cloud, Edge, etc.)",
        "Computación Cuántica (Introductoria)"
    ]
}

# Función para obtener especialidad
def obtener_especialidad(nombre_carrera):
    for especialidad, lista in especialidades.items():
        if nombre_carrera in lista:
            return especialidad
    return "Sin Clasificar"

# Función para generar sección
def generar_seccion(nombre_carrera):
    palabras = nombre_carrera.split()
    letra1 = palabras[0][0] if len(palabras) >= 1 else 'X'
    letra2 = palabras[1][0] if len(palabras) >= 2 else letra1
    letra_random = random.choice(['i', 'x', 'z', 'r', 'm'])
    return f"{letra1}{letra_random}{letra2}-{random.randint(1, 99)}".upper()

# Obtener carreras con semestre_total
cursor.execute("SELECT ID_Carrera, Nombre, Semestre_Total FROM carrera")
carreras = cursor.fetchall()

# Agrupar carreras por especialidad
carreras_por_especialidad = {esp: [] for esp in especialidades}
for carrera in carreras:
    esp = obtener_especialidad(carrera['Nombre'])
    if esp in carreras_por_especialidad:
        carreras_por_especialidad[esp].append(carrera)


# Limpieza de tabla sala
cursor.execute('DELETE FROM sala')
cursor.execute('ALTER TABLE sala AUTO_INCREMENT = 1')
db.commit()

# Configuración
total_salas = 800
tipos = []

# Distribución proporcional
tipos += ["Sala General"] * int(total_salas * 0.4)
tipos += ["Laboratorio de Computación"] * int(total_salas * 0.3)
tipos += ["Sala Especializada"] * (total_salas - len(tipos))  # lo que falte
#Se generaran un 40% de salas generales, 40% de Laboratorios de computacion y lo que falta pues a terreno 


# Insertar salas
for tipo in tipos:
    if tipo == "Sala General":


        #Se meten las salas generales del piso 1 al 3 como en inacap :V
        piso = random.choice([1, 2, 3])


    elif tipo == "Laboratorio de Computación":

        #Todos los laboratorios estan en el piso 0 
        piso = 0
    else:  # Sala Especializada

        #Creo que estas salas estan en cada piso por eso del 0 al 3

        piso = random.choice([0, 1, 2, 3])
    
    
    cursor.execute("INSERT INTO sala (Tipo, Piso) VALUES (%s, %s)", (tipo, piso))
db.commit()
print("Salas generadas con distribución proporcional y lógica de piso.")

import pymysql
import random

# Conexión a la base de datos
db = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_uni',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = db.cursor()

# Limpieza de tabla sala
#cursor.execute('DELETE FROM sala')
#cursor.execute('ALTER TABLE sala AUTO_INCREMENT = 1')
#db.commit()

# Configuración
#total_salas = 800
#tipos = []

# Distribución proporcional
#tipos += ["Sala General"] * int(total_salas * 0.4)
#tipos += ["Laboratorio de Computación"] * int(total_salas * 0.3)
#tipos += ["Sala Especializada"] * (total_salas - len(tipos))  # lo que falte
#Se generaran un 40% de salas generales, 40% de Laboratorios de computacion y lo que falta pues a terreno 


# Insertar salas
#for tipo in tipos:
#    if tipo == "Sala General":


        #Se meten las salas generales del piso 1 al 3 como en inacap :V
        #piso = random.choice([1, 2, 3])


   # elif tipo == "Laboratorio de Computación":

        #Todos los laboratorios estan en el piso 0 
    #    piso = 0
    #else:  # Sala Especializada

        #Creo que estas salas estan en cada piso por eso del 0 al 3

    #    piso = random.choice([0, 1, 2, 3])
    
    
    #cursor.execute("INSERT INTO sala (Tipo, Piso) VALUES (%s, %s)", (tipo, piso))
#db.commit()

#print("Salas generadas con distribución proporcional y lógica de piso.")
        
def Curso_Sala(id_curso,año):
# Obtener todos los cursos y salas
#cursor.execute("SELECT ID_Curso FROM curso")
#cursos = cursor.fetchall()

    cursor.execute("SELECT Codigo_Sala FROM sala ORDER BY RAND() LIMIT 1")
    datos=cursor.fetchall()[0]["Codigo_Sala"]
    salas = datos

# Verificación
#if not cursos or not salas:
#    print("No hay cursos o salas disponibles")
#else:
    # Asignar una sala aleatoria a cada curso
    #for curso in cursos:
    #id_curso = curso['ID_Curso']
    #sala = random.choice(salas)['Codigo_Sala']
    fecha = faker.date_time_between(start_date=date(año,1,1), end_date=date(año,4,30))
    
    cursor.execute("""INSERT INTO curso_sala 
        (Codigo_Sala, ID_Curso, Fecha) 
        VALUES (%s, %s, %s)""",
        (salas, id_curso, fecha))
    db.commit()



#La idea es que todos los cursos disponibles se les asignara una sala al azar
#Se tomaran todos los cursos disponibles para asignarles una sala :V

g=Gustavo()
print("Creando Titulos...")
for i in range(10500):
    g.Titulo()
print("Creando Profesores...")
for j in range(10500):
    g.Profesor()

# Insertar 50 cursos por especialidad
for especialidad, carreras_esp in carreras_por_especialidad.items():
    print(f"Insertando cursos para la especialidad: {especialidad}")
    print("Ademas se asignaran profesores y alumnos a los cursos")
    print("Esto puede tardar unos minutos, por favor espere...")
    for _ in range(2500):
        carrera = random.choice(carreras_esp)
        nombre_curso = random.choice(asignaturas_por_especialidad.get(especialidad, ["Curso General"]))
        seccion = generar_seccion(carrera['Nombre'])
        hora_total = faker.time(pattern="%H:%M:%S")
        capacidad_max = random.randint(20, 60)
        año = faker.date_time_between(start_date="-10y",end_date="now").year #random.randint(2020, 2025)
        max_semestre = carrera['Semestre_Total']
        semestre = max_semestre - random.randint(0, max_semestre - 1)
        cursor.execute("""INSERT INTO curso 
            (Nombre, Especialidad, Seccion, Hora_Total, Capacidad_Max, Año, Semestre, ID_Carrera) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (nombre_curso, especialidad, seccion, hora_total, capacidad_max, año, semestre, carrera['ID_Carrera']))
        id_curso = cursor.lastrowid
        db.commit()
        g.ProfesorCurso(id_curso)
        Guillermo.Curso_Alumno(id_curso)
        Guillermo.Curso_TipoClase(id_curso)
        Curso_Sala(id_curso,año)



print("Se han generado 50 cursos")







