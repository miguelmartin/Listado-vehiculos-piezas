#!/usr/bin/python
# -*- encoding: utf-8 -*-
#IMportamos los módulos necesarios
import cgi
import cgitb; cgitb.enable() # Optional; for debugging only
import psycopg2
import sys
import pprint
import cgi
import os.path
import subprocess
#damos el valor a cont que utilizaremos más adelante
cont = 0
#recibimos los datos del formulario
arguments = cgi.FieldStorage()
valores = cgi.FieldStorage()
nomversion = valores["NOMVERSION"].value
refid =  valores["idvehiculo"].value
#Imprimimos el html
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
#Si la primera imagen de la pieza no existe entonces consultamos a la bas de datos
if not os.path.exists("/var/www/img/"+str(refid)+str(cont+1)+".jpg"):
	def main():
       		conn_string = "host='' dbname='' user='' password=''"
       		conn = psycopg2.connect(conn_string)
		cursor2 = conn.cursor()	
		cursor2.execute("select f.datos from entradastock e inner join albumpiezas a on e.refid=a.refid inner join ficheros fi on fi.id=a.idficherofoto inner join datosficheros f on f.masterid=a.idficherofoto where e.refid="+str(refid)+";")
		fotos = cursor2.fetchall()
		cont2 = 0
		#Si no devuelve nada mostramos la imagen por defecto
		if fotos == []:
			print "<img id='imagenarticulo' src='/img/defecto.jpg' alt='Smiley face' height='130' width='130'></img>"
		#Si devuelve entonces guardamos y mostramos cada una de ellas
		else:
			for foto in fotos:
				open("/var/www/img/"+str(refid)+""+str(cont2)+".jpg", 'wb').write(str(foto[0]))
				print  "<a href='/img/"+str(refid)+str(cont2)+".jpg'><img id='imagenarticulo' src='/img/"+str(refid)+str(cont2)+".jpg' alt='Smiley face' height='130' width='130'></a>"	
				cont2 += 1
	if __name__ == "__main__":
       		main()
	#cerramos la consulta de imágenes
#Si existe la primera imagen las contamos y mostramos todas
else:
	numarchivos = subprocess.check_output("ls -l /var/www/img/"+str(refid)+"[0-9].jpg | wc -l", shell=True)
	for x in xrange(int(numarchivos)):
		print "<a href='/img/"+str(refid)+str(cont)+".jpg'><img id='imagenarticulo' src='/img/"+str(refid)+str(cont)+".jpg' alt='Smiley face' height='130' width='130'></a>"
		cont += 1

#Ahora vamos a consultar algunas propiedades interesante para cada pieza
def main():
        conn_string = "host='' dbname='' user='' password=''"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select referencia,estado,ubicacion,precio,reffab2,reffab1,refequiv,nota from entradastock where refid="+str(refid)+" ;")
        resultado = cursor.fetchall()
	print "<ul id='pieza'>"
        for datopieza in resultado:
		print "<ul>"
                print "<p><il>Estado: "+str(datopieza[1])+"</il></p>"
                print "<p><il>Referencia: "+str(datopieza[0])+"</il></p>"
                print "<p><il>Ubicacion: "+str(datopieza[2])+"</il></p>"
                print "<p><il>Precio: "+str(datopieza[3])[0:-1]+"€" "</il></p>"
		print "<p><il>Referencia 1: "+str(datopieza[4])+"</il></p>"
                print "<p><il>Referencia 2: "+str(datopieza[5])+"</il></p>"
                print "<p><il>Referencia equivalente: "+str(datopieza[6])+"</il></p>"
        	print "<p><il>Nota: "+str(datopieza[7])+"</il></p>"
		print "</ul>"
	print "</ul>"
	print "<div id='footer'>"
        print "©Tododesguace.com 2013"
        print "</div>"	
	print "</div>"
	print "</body>"
if __name__ == "__main__":
        main()
#Fin del programa
