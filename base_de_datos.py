import sqlite3

global conectar,c

conectar =sqlite3.connect("base_principal.db")
c = conectar.cursor()

def crea_tabla():
    c.execute("""
        CREATE TABLE PRODUCTOS(
        "ID" INTERGER(5) PRIMARY KEY,
        "nombre_articulo" VARCHAR(50) NOT NULL UNIQUE,
        "nombre_segundario" VARCHAR(50),
        "PRECIO$" INTEGER(20) NOT NULL
    )""")

def Buscar_por_ID(codigo):
    conectar = sqlite3.connect("base_principal.db")
    c = conectar.cursor()
    c.execute("""
    SELECT * FROM PRODUCTOS WHERE ID=? """,codigo)
    return c.fetchone()

def Buscar_por_nombre(nombre):
    conectar = sqlite3.connect("base_principal.db")
    c = conectar.cursor()
    nombre = nombre.capitalize()
    c.execute("SELECT * FROM PRODUCTOS WHERE nombre_articulo=? ",(nombre,))
    busqueda = c.fetchone()
    if busqueda:
        print("Busqueda por nombre primaria hecha")
        return busqueda
    else:
        c.execute("SELECT * FROM PRODUCTOS WHERE nombre_segundario=? ",(nombre,)) 
        busqueda = c.fetchone()
        if busqueda:
            print("segundario")
            return busqueda   
        else:
            print("no existe el nombre buscado")
            
def eliminar_de_base(codigo):
    conectar = sqlite3.connect("base_principal.db")
    c = conectar.cursor()
    c.execute("DELETE FROM PRODUCTOS WHERE ID=? ",(codigo,))
    conectar.commit()

def update_base(codigo_principal,codigo,name,name2,price):
    conectar = sqlite3.connect("base_principal.db")
    c = conectar.cursor()
    c.execute("UPDATE PRODUCTOS SET nombre_articulo=? WHERE ID=?",(name,codigo_principal))
    c.execute("UPDATE PRODUCTOS SET nombre_segundario=? WHERE ID=?",(name2,codigo_principal))
    c.execute("UPDATE PRODUCTOS SET PRECIO$=? WHERE ID=?",(price,codigo_principal))
    c.execute("UPDATE PRODUCTOS SET ID=? WHERE ID=?",(codigo,codigo_principal))
    conectar.commit()

def actualkizar_base_codigo(codigo,nuevoprecio):
    c.execute("UPDATE PRODUCTOS SET PRECIO$=? WHERE ID=?",(nuevoprecio,codigo))

def actualkizar_base_nombre(codigo,nuevonombre):
    c.execute("UPDATE PRODUCTOS SET nombre_articulo=? WHERE ID=?",(nuevonombre,codigo))

def insertar_producto(codigo,nombreP,nombreS,precio):
    conectar = sqlite3.connect("base_principal.db")
    c = conectar.cursor()
    nombreP = nombreP.capitalize()
    nombreS = nombreS.capitalize()
    print(codigo,nombreP,nombreS,precio)
    c.execute("INSERT INTO PRODUCTOS VALUES (?,?,?,?)",(codigo,nombreP,nombreS,precio))
    conectar.commit()

conectar.commit()
conectar.close()