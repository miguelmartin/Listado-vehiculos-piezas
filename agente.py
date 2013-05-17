#!/usr/bin/python
# -*- encoding: utf-8 -*-
import psycopg2
import sys
import pprint
import cgi
import os.path
#Obtenemos valores

print "Content-Type: text/html\n"
form = cgi.FieldStorage()
modelo = form.getvalue("modelo")
combustible = form.getvalue("combustible")
valoroffset = "0"

#Conexion a la base de datos y consulta
def main():
        conn_string = "host='server' dbname='bbdd' user='usuario' password='pass'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select distinct(veh.idvehiculo),veh.nombreversion,veh.codigo from vehiculos veh left join vendido vt on veh.idvehiculo = vt.idvehiculo  where upper(nombreversion) like "+"'%"+modelo.upper()+"%' and upper(otrocombustible) like "+"'%"+combustible.upper()+"%' LIMIT '10' OFFSET "+"'"+valoroffset+"';")
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
	print "<div id='cabecera'>"
	print "<img src='/img/tododesguacecom.jpg' alt='Tododesguacecom'></img>"
	print "</div>"
	print "<div id='menuh'>" 
	print "<ul id='inicio'>"
	print "<li><a href='/index.html'>" "Inicio " "</a></li>"  "<li><a href='/indexpiezas.html'>" "Busqueda Por piezas " "</a></li>" "<li><a href='/indexcoches.html'>" "Busqueda por vehículos " "</a></li>" "</ul>"
	print "</div>"
	print "<div id='contenedor4'>"
	print "<p><a href='/cgi-bin/agente4.py?MODELO="+modelo.upper()+"&COMBUSTIBLE="+combustible.upper()+"&OFFSET="+str(nuevovaloroffset)+"'>Siguiente</a></p>"
	print "<div id='contenido'>"
	print "<ul>"
	for coche in resultado:
		if not os.path.exists("/var/www/img/"+str(coche[0])+".jpg"):
			cursor2 = conn.cursor()
                	cursor2.execute("select f.datos from vehiculos v,albumvehiculos a,ficheros fi,datosficheros f where v.idvehiculo=a.idvehiculo and fi.id=a.idficherofoto and f.masterid=a.idficherofoto and v.idvehiculo="+str(coche[0])+";")
                	mypic2 = cursor2.fetchone()
                	if str(type(mypic2)) == "<type 'NoneType'>":
                        	url = "<img id='vehiculo' src='/img/defecto.jpg' alt='Smiley face' height='60' width='60'></img>"
                	else:
				open("/var/www/img/"+str(coche[0])+".jpg", 'wb').write(str(mypic2[0]))
				url = "<a href='/img/"+str(coche[0])+".jpg'><img id='vehiculo' src='/img/"+str(coche[0])+".jpg' alt='Smiley face' height='60' width='60'></a>"
		else:
			url = "<a href='/img/"+str(coche[0])+".jpg'><img id='vehiculo' src='/img/"+str(coche[0])+".jpg' alt='Smiley face' height='60' width='60'></a>"
		print "<il>"+str(url)+"<a href='/cgi-bin/agente2.py?idvehiculo="+str(coche[0])+"'>"+(coche[1])+" </a> "+"ID vehiculo: "+str(coche[2])+"</il></br>"
	print "</ul>"
	print "</div>"
	print "<p><a href='/cgi-bin/agente4.py?MODELO="+modelo.upper()+"&COMBUSTIBLE="+combustible.upper()+"&OFFSET="+str(nuevovaloroffset)+"'>Siguiente</a></p>"	
	print "</div>"
	print "</body>"
if __name__ == "__main__":
                main()
