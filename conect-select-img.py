#Abrimos conexion con la Base de Datos

import psycopg2
conn_string = "host='localhost' dbname='prueba' user='postgres' password='usuario'"
conn = psycopg2.connect(conn_string)

#Metemos la imagen en la base de datos (datos en binario en la columna de tipo bytea) esta parte no nos interesa pero la necesitamos para probar

mypic=open('/home/usuario/img/imagen.jpg','rb').read()
cursor = conn.cursor()
cursor.execute("INSERT INTO imagenes(idimagen,datos) VALUES (%s,%s);", ('image3.jpg', psycopg2.Binary(mypic)))
conn.commit()

#Leemos la imagen de la base de datos y la escribimos en el fichero copyofimagen.jpg

cursor = conn.cursor()
cursor.execute("SELECT (datos) FROM imagenes WHERE idimagen='image3.jpg';")
mypic2 = cursor.fetchone()
open('/home/usuario/img/copyofimagen.jpg', 'wb').write(str(mypic2[0]))

#Cerramos la conexion con la base de datos

cursor.close()
conn.close()

