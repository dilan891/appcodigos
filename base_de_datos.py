import sqlite3
 

conectar = sqlite3.connect("base_principal")
c = conectar.cursor()

conectar.commit()
conectar.close()