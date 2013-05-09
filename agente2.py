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
 codvehiculo =  arguments[i].value

#Conexion a la base de datos y consulta
if not os.path.exists("/var/www/img/"+str(codvehiculo)+str(cont+1)+".jpg"):
	def main():
       		conn_string = "host='' dbname='' user='' password=''"
       		conn = psycopg2.connect(conn_string)
		cursor2 = conn.cursor()	
		cursor2.execute("select f.datos from vehiculos v,albumvehiculos a,ficheros fi,datosficheros f where v.idvehiculo=a.idvehiculo and fi.id=a.idficherofoto and f.masterid=a.idficherofoto and v.idvehiculo="+str(codvehiculo)+";")
		fotos = cursor2.fetchall()
		if fotos == []:
                        print "<img src='/img/defecto.jpg' alt='Smiley face' height='100' width='100'></img>"
                else:
			cont2 = 0
			for foto in fotos:
				open("/var/www/img/"+str(codvehiculo)+""+str(cont2)+".jpg", 'wb').write(str(foto[0]))
				print  "<a href='/img/"+str(codvehiculo)+str(cont2)+".jpg'><img src='/img/"+str(codvehiculo)+str(cont2)+".jpg' alt='Smiley face' height='60' width='60'></a>"	
				cont2 += 1
	if __name__ == "__main__":
       		main()
else:
	numarchivos = subprocess.check_output("ls -l /var/www/img/"+str(codvehiculo)+"[0-9].jpg | wc -l", shell=True)
	for x in xrange(int(numarchivos)):
		print "<a href='/img/"+str(codvehiculo)+str(cont)+".jpg'><img src='/img/"+str(codvehiculo)+str(cont)+".jpg' alt='Smiley face' height='60' width='60'></a>"
		cont += 1

def main():
	conn_string = "host='' dbname='' user='' password=''"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select art.descripcion,es.refid from entradastock es inner join referencias ref on es.referencia = ref.referencia inner join articulos art on art.idarticulo = ref.idarticulo inner join versiones ver on ver.idversion = ref.idversion where es.refid in (select refid from stockvehiculo where idvehiculo = "+str(codvehiculo)+") ;")
        resultado = cursor.fetchall()
        print "<ul>"
        for pieza in resultado:
               print "<a href='/cgi-bin/agente3.py?idvehiculo="+str(pieza[1])+"'><il>"+(pieza[0])+"</il></a><br/>"
        print "</ul>"

if __name__ == "__main__":
        main()
