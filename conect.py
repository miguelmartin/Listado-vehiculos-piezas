#importo la libreria pg para poder utilizar las opciones de python con postgres

import pg

#Realizo la conexión con la base de datos le facilito user, pass y nombre de la base de datos	 

conn = pg.connect(dbname='db_name',user='user_name',passwd='password')

#Aqui realizo la consulta a la base de datos	 
consulta = 'select * from table;'
resultado = conn.query(consulta)
#Cierro la conexión 
conn.close()
#Imprimo el resultado por pantalla	 
print resultado
