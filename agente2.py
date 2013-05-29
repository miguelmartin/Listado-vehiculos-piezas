#!/usr/bin/python
# -*- encoding: utf-8 -*-
#Importamos los módulos necesarios
import cgi
import cgitb; cgitb.enable() # Optional; for debugging only
import psycopg2
import sys
import pprint
import cgi
import os.path
import commands
#Damos un valor a cont que luego utilizaremos más adelante
cont = 0
#Obtenemos los valor desde el la url que a llamado a este programa
valores = cgi.FieldStorage()
nomversion = valores["NOMVERSION"].value
codvehiculo =  valores["idvehiculo"].value
#Imprimimos como un html la página 
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
print "<h2>"+str(nomversion)+"</h2>"
#Si no existe la primera imagen del cohe entonces nos conectamos para consultarlas
if not os.path.exists("/var/www/img/"+str(codvehiculo)+str(cont+1)+".jpg"):
	def main():
       		conn_string = "host='' dbname='' user='' password=''"
       		conn = psycopg2.connect(conn_string)
		cursor2 = conn.cursor()	
		cursor2.execute("select f.datos from vehiculos v,albumvehiculos a,ficheros fi,datosficheros f where v.idvehiculo=a.idvehiculo and fi.id=a.idficherofoto and f.masterid=a.idficherofoto and v.idvehiculo="+str(codvehiculo)+";")
		fotos = cursor2.fetchall()
		#Si no devuelve nada la consulta mostramos la imagen por defecto
		if fotos == []:
                        print "<img  id='imagenarticulo' src='/img/defecto.jpg' alt='Smiley face' height='110' width='110'></img>"
                #En el caso contrario guardamos las iamgenes y imprimimos su url
		else:
			cont2 = 0
			for foto in fotos:
				open("/var/www/img/"+str(codvehiculo)+""+str(cont2)+".jpg", 'wb').write(str(foto[0]))
				print  "<a href='/img/"+str(codvehiculo)+str(cont2)+".jpg'><img  id='imagenarticulo' src='/img/"+str(codvehiculo)+str(cont2)+".jpg' alt='Smiley face' height='110' width='110'></a>"	
				cont2 += 1
	if __name__ == "__main__":
       		main()
	#cerramos la consulta de imágenes
#Si ya existen las imagenes las contamos y las mostramos
else:
	numarchivos = commands.getoutput("ls -l /var/www/img/"+str(codvehiculo)+"[0-9].jpg | wc -l")
	for x in xrange(int(numarchivos)):
		print "<a href='/img/"+str(codvehiculo)+str(cont)+".jpg'><img  id='imagenarticulo' src='/img/"+str(codvehiculo)+str(cont)+".jpg' alt='Smiley face' height='110' width='110'></a>"
		cont += 1
#Ahora consultamos las piezas disponibles para el coche concreto
def main():
	conn_string = "host='' dbname='' user='' password=''"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select art.descripcion,es.refid from entradastock es inner join referencias ref on es.referencia = ref.referencia inner join articulos art on art.idarticulo = ref.idarticulo inner join versiones ver on ver.idversion = ref.idversion where es.refid in (select refid from stockvehiculo where idvehiculo = "+str(codvehiculo)+") order by art.descripcion;")
        resultado = cursor.fetchall()
	print "<p>Piezas en este vehículo:</p>"
        print "<ul>"
        for pieza in resultado:
               print "<p><a href='/cgi-bin/agente3.py?idvehiculo="+str(pieza[1])+"&NOMVERSION="+(pieza[0])+"'><il>"+(pieza[0])+"</il></a></p>"
        print "</ul>"
	print "</ul>"
	print "<div id='footer'>"
        print "©Tododesguace.com 2013"
        print "</div>"	
	print "</div>"
	print "</body>"

if __name__ == "__main__":
        main()
#fin del programa
