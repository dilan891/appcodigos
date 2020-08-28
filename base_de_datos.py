import sqlite3
 

conectar = sqlite3.connect("base_principal")
c = conectar.cursor()

c.execute("""CREATE TABLE PRODUCTOS(
    ID,
    nombre_articulo VARCHAR(50),
    nombre_segundario VARCHAR(50),
    PRECIO$ INTEGER(20)
)""")

conectar.commit()
conectar.close()