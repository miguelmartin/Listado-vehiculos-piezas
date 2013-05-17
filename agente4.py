#!/usr/bin/python
# -*- encoding: utf-8 -*-
import psycopg2
import sys
import pprint
import cgi
import os.path
#Obtenemos valores

print "Content-Type: text/html"
print ""
valores = cgi.FieldStorage()

modelo = valores["MODELO"].value
combustible =  valores["COMBUSTIBLE"].value
valoroffset =  valores["OFFSET"].value

def main():
        conn_string = "host='' dbname='' user='' password=''"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select distinct(v.idvehiculo),v.nombreversion,v.codigo from vehiculos v,albumvehiculos a,ficheros fi,datosficheros f where v.idvehiculo=a.idvehiculo and fi.id=a.idficherofoto and f.masterid=a.idficherofoto and upper(nombreversion) like "+"'%"+modelo.upper()+"%'and upper(otrocombustible) like "+"'%"+combustible.upper()+"%' LIMIT '10' OFFSET "+"'"+valoroffset+"';")
        resultado = cursor.fetchall()
	nuevovaloroffset = int(valoroffset)+10
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
	print modelo
	print "<p><a href='/cgi-bin/agente4.py?MODELO="+modelo.upper()+"&COMBUSTIBLE="+combustible.upper()+"&OFFSET="+str(nuevovaloroffset)+"'>Siguiente</a></p>"
        print "<a href='javascript:history.back(1)'>Anterior</a>"
	print "<ul>"	
	for coche in resultado:
		if not os.path.exists("/var/www/img/"+str(coche[0])+".jpg"):
			cursor2 = conn.cursor()
                	cursor2.execute("select f.datos from vehiculos v,albumvehiculos a,ficheros fi,datosficheros f where v.idvehiculo=a.idvehiculo and fi.id=a.idficherofoto and f.masterid=a.idficherofoto and v.idvehiculo="+str(coche[0])+";")
                	mypic2 = cursor2.fetchone()
                	open("/var/www/img/"+str(coche[0])+".jpg", 'wb').write(str(mypic2[0]))
		print "<il><a href='/img/"+str(coche[0])+".jpg'><img id='vehiculo' src='/img/"+str(coche[0])+".jpg' alt='Smiley face' height='60' width='60'></a><a href='/cgi-bin/agente2.py?idvehiculo="+str(coche[0])+"'>"+(coche[1])+"</a>   "+"ID vehiculo: "+str(coche[2])+"</il></br>"
	print "</ul>"
	print "<a href='javascript:history.back(1)'>Anterior</a>"
	print "<a href='/cgi-bin/agente4.py?MODELO="+modelo.upper()+"&COMBUSTIBLE="+combustible.upper()+"&OFFSET="+str(nuevovaloroffset)+"'>Siguiente</a>"
	print "</div>"
	print "</div>"
	print "</body>"
if __name__ == "__main__":
                main()
