#!/usr/bin/python
# -*- encoding: utf-8 -*-
#importamos módulos necesarios
import psycopg2
import sys
import pprint
import cgi
import os.path
#Obtenemos valores del formulario html
valores = cgi.FieldStorage()
modelo = valores["MODELO"].value
valoroffset =  valores["OFFSET"].value
#Nos conectamos a la base de datos y hacemos la consulta con los datos del formulario
def main():
        conn_string = "host='' dbname='' user='' password=''"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select distinct(veh.idvehiculo),veh.nombreversion,veh.codigo from vehiculos veh left join vendido vt on veh.idvehiculo = vt.idvehiculo where vt.idvehiculo is null and upper(nombreversion) like "+"'%"+modelo.upper()+"%' order by veh.codigo desc LIMIT '10' OFFSET "+"'"+valoroffset+"';")
	resultado = cursor.fetchall()
	nuevovaloroffset = int(valoroffset)+10
	cursor3 = conn.cursor()
	cursor3.execute("select count(*) from vehiculos veh left join vendido vt on veh.idvehiculo = vt.idvehiculo where vt.idvehiculo is null and upper(nombreversion) like "+"'%"+modelo.upper()+"%' LIMIT '10' OFFSET '0';")
        resultado2 = cursor3.fetchall()
	numfilas = int(resultado2[0][0]) - int(valoroffset)
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
	print "<h3><< <a class='anterior' href='javascript:history.back(1)'>Anterior</a>"
	if numfilas > 10:
		print "<a class='siguiente' href='/cgi-bin/agente4.py?MODELO="+modelo.upper()+"&OFFSET="+str(nuevovaloroffset)+"'>Siguiente   </a>>></h3>"
	print "<ul>"	
	for coche in resultado:
		if not os.path.exists("/var/www/img/"+str(coche[0])+".jpg"):
			cursor2 = conn.cursor()
                	cursor2.execute("select f.datos from vehiculos v,albumvehiculos a,ficheros fi,datosficheros f where v.idvehiculo=a.idvehiculo and fi.id=a.idficherofoto and f.masterid=a.idficherofoto and v.idvehiculo="+str(coche[0])+";")
                	mypic2 = cursor2.fetchone()
                	if str(type(mypic2)) == "<type 'NoneType'>":
                        	url = "<img id='vehiculo' src='/img/defecto.jpg' alt='Smiley face' height='100' width='100'></img>"
                	else:
				open("/var/www/img/"+str(coche[0])+".jpg", 'wb').write(str(mypic2[0]))
				url = "<a href='/img/"+str(coche[0])+".jpg'><img id='vehiculo' src='/img/"+str(coche[0])+".jpg' alt='Smiley face' height='100' width='100'></a>"
		else:
			url = "<a href='/img/"+str(coche[0])+".jpg'><img id='vehiculo' src='/img/"+str(coche[0])+".jpg' alt='Smiley face' height='100' width='100'></a>"
		print "<h3><il>"+str(url)+"<a href='/cgi-bin/agente2.py?idvehiculo="+str(coche[0])+"&NOMVERSION="+(coche[1])+"'>"+(coche[1])+" </a> "+"ID vehiculo: "+str(coche[2])+"</il></br></h3>"
	print "</ul>"
	print "<h3><< <a class='anterior' href='javascript:history.back(1)'>Anterior </a>"
	if numfilas > 10:
		print "<a class='siguiente' href='/cgi-bin/agente4.py?MODELO="+modelo.upper()+"&OFFSET="+str(nuevovaloroffset)+"'> Siguiente </a>>></h3>"	
	print "<h3></h3>"
	print "<div id='footer'>"
        print "©Tododesguace.com 2013"
        print "</div>"
	print "</div>"
	print "</div>"
	print "</body>"
if __name__ == "__main__":
                main()
