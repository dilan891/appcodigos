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
    c.execute("SELECT * FROM PRODUCTOS WHERE nombre_articulo=? ",nombre)
    busqueda = c.fetchone()
    if busqueda:
        print("primario")
        return busqueda
    else:
        c.execute("SELECT * FROM PRODUCTOS WHERE nombre_segundario=? ",nombre) 
        busqueda = c.fetchone()
        if busqueda:
            print("segundario")
            return busqueda   
        else:
            print("no existe el nombre buscado")

def eliminar_de_base(codigo):
    c.execute("DELETE FROM PRODUCTOS WHERE ID=? ",codigo)

def actualkizar_base_codigo(codigo,nuevoprecio):
    c.execute("UPDATE PRODUCTOS SET PRECIO$=? WHERE ID=?",(nuevoprecio,codigo))

def actualkizar_base_nombre(codigo,nuevonombre):
    c.execute("UPDATE PRODUCTOS SET nombre_articulo=? WHERE ID=?",(nuevonombre,codigo))

def insertar_producto(codigo,nombreP,nombreS,precio):
    c.execute("INSERT INTO PRODUCTOS VALUES (?,?,?,?)",(codigo,nombreP,nombreS,precio))

conectar.commit()
conectar.close()