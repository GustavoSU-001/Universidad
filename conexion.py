import pymysql
def Conexion(self):
    def __init__(self):
        
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='bd_uni',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.db.cursor()
    
    #
    #
    #if tipo in ['delete','select']:
    #    cursor.execute(consulta)
    #else:
    #    cursor.execute(consulta,datos)
    #    
    # 
    #if tipo == 'insert':
    #    db.commit()
    #elif tipo == 'select':
    #    resultado = cursor.fetchall()
    #    cursor.close()
    #    return resultado
    #elif tipo == 'update':
    #    db.commit()
    #elif tipo == 'delete':
    #    db.commit()
    # 
    #cursor.close()
