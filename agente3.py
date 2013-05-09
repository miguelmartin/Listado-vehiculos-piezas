#!/usr/bin/python
# -*- encoding: utf-8 -*-

import cgi
import cgitb; cgitb.enable() # Optional; for debugging only
import psycopg2
import sys
import pprint
import cgi
import os.path
import subprocess
cont = 0


print "Content-Type: text/html"
print ""
arguments = cgi.FieldStorage()
for i in arguments.keys():
	refid =  arguments[i].value

if not os.path.exists("/var/www/img/"+str(refid)+str(cont+1)+".jpg"):
	def main():
       		conn_string = "host='' dbname='' user='' password=''"
       		conn = psycopg2.connect(conn_string)
		cursor2 = conn.cursor()	
		cursor2.execute("select f.datos from entradastock e inner join albumpiezas a on e.refid=a.refid inner join ficheros fi on fi.id=a.idficherofoto inner join datosficheros f on f.masterid=a.idficherofoto where e.refid="+str(refid)+";")
		fotos = cursor2.fetchall()
		cont2 = 0
		if fotos == []:
			print "<img src='/img/defecto.jpg' alt='Smiley face' height='100' width='100'></img>"
		else:
			for foto in fotos:
				open("/var/www/img/"+str(refid)+""+str(cont2)+".jpg", 'wb').write(str(foto[0]))
				print  "<a href='/img/"+str(refid)+str(cont2)+".jpg'><img src='/img/"+str(refid)+str(cont2)+".jpg' alt='Smiley face' height='100' width='100'></a>"	
				cont2 += 1
	if __name__ == "__main__":
       		main()
else:
	numarchivos = subprocess.check_output("ls -l /var/www/img/"+str(refid)+"[0-9].jpg | wc -l", shell=True)
	for x in xrange(int(numarchivos)):
		print "<a href='/img/"+str(refid)+str(cont)+".jpg'><img src='/img/"+str(refid)+str(cont)+".jpg' alt='Smiley face' height='100' width='100'></a>"
		cont += 1

#Conexion a la base de datos y consulta
def main():
        conn_string = "host='' dbname='' user='' password=''"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select referencia,estado,ubicacion,precio,metadatos from entradastock where refid="+str(refid)+" ;")
        resultado = cursor.fetchall()
	print "<ul>"
        for datopieza in resultado:
                print "<ul>"+str(datopieza[1])+"</ul>"
                print "<ul>"+str(datopieza[0])+"</ul>"
                print "<ul>"+str(datopieza[2])+"</ul>"
                print "<ul>"+str(datopieza[3])+"</ul>"
                print "<ul>"+str(datopieza[4])+"</ul>"
        print "</ul>"
if __name__ == "__main__":
        main()
