	#Importamos las siguiente librerias que necesitamos
import psycopg2
import sys
import pprint
	#Le facilitamos los datos para la conexión a la base de datos 
def main():
	conn_string = "host='localhost' dbname='dbname' user='postgres' password='password'"

	# Imprimira la cadena con la cual estamos conectandonos a la base de datos

	print "Connecting to database\n	->%s" % (conn_string)
 
	# Obtenemos la conexion a la base de datos, si hay algún problema lo mostrara
	conn = psycopg2.connect(conn_string)
 
	# Cursores con los  que vamos a  ejecutar la  consulta
	cursor = conn.cursor()
 
	# Ejecuta una consulta
	cursor.execute("SELECT * FROM datosficheros")
 
	# Recibe los datos de la consulta a la base de datos
	records = cursor.fetchall()
 
	
	# Imprimer los datos
	pprint.pprint(records)
