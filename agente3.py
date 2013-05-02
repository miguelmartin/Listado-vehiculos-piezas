#!/usr/bin/python
# -*- encoding: utf-8 -*-

import cgi
import cgitb; cgitb.enable() # Optional; for debugging only
import psycopg2
import sys
import pprint
import cgi
import os.path

print "Content-Type: text/html"
print ""
arguments = cgi.FieldStorage()
for i in arguments.keys():
	refid =  arguments[i].value

#Conexion a la base de datos y consulta
def main():
        conn_string = "host='' dbname='' user='' password=''"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select referencia,estado,ubicacion,precio,metadatos from entradastock where refid="+str(refid)+" ;")
        resultado = cursor.fetchall()
	if not os.path.exists("/var/www/img/"+str(refid)+".jpg"):
		cursor2 = conn.cursor()
        	cursor2.execute("select f.datos from entradastock e inner join albumpiezas a on e.refid=a.refid inner join ficheros fi on fi.id=a.idficherofoto inner join datosficheros f on f.masterid=a.idficherofoto where e.refid="+str(refid)+";")
        	mypic2 = cursor2.fetchone()
		if str(type(mypic2)) == "<type 'NoneType'>":
			url = "<img src='/img/defecto.jpg' alt='Smiley face' height='300' width='300'></img>"
		else:
        		open("/var/www/img/"+str(refid)+".jpg", 'wb').write(str(mypic2[0]))
			url = "<img src='/img/"+str(refid)+".jpg' alt='Smiley face' height='300' width='300'></img>"
	else:
		url = "<img src='/img/"+str(refid)+".jpg' alt='Smiley face' height='300' width='300'></img>"
	print "<ul>"
	print url
        for datopieza in resultado:
                print "<ul>"+str(datopieza[1])+"</ul>"
                print "<ul>"+str(datopieza[0])+"</ul>"
                print "<ul>"+str(datopieza[2])+"</ul>"
                print "<ul>"+str(datopieza[3])+"</ul>"
                print "<ul>"+str(datopieza[4])+"</ul>"
        print "</ul>"
if __name__ == "__main__":
        main()
