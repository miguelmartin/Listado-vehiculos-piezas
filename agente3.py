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
print "<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'>"
print "<html xmlns='http://www.w3.org/1999/xhtml'>"
print "<head>"
print "<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />"
print "<title>Tododesguace.com</title>"
print "<link rel='stylesheet' type='text/css' href='/css/estilos.css' media='screen' /> "
print "</head>"
print "<body>"
print "<div id='page'>"
print "<div id='cabecera'>"
print "<img id='imagencabecera' src='/img/tododesguacecom.jpg' alt='Tododesguacecom'></img>"
print "<img src='/img/telefono11.jpg' alt='Tododesguacecom'></img>"
print "</div>"
print "<div id='menuh'>" 	
print "<ul id='inicio'>"
print "<li><a href='/index.html'>Inicio</a></li><li><a href='/indexpiezas.html'>Busqueda Por piezas</a></li><li><a href='/indexcoches.html'> Busqueda por vehículos </a></li></ul>"
print "</div>"
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
        print "</ul>"	
	print "</div>"
	print "</body>"
if __name__ == "__main__":
        main()
