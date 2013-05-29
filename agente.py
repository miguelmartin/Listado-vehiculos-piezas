#!/usr/bin/python
# -*- encoding: utf-8 -*-
#Importamos los módulos necesarios
import psycopg2
import sys
import pprint
import cgi
import os.path
#Obtenemos el valor modelo del formulario HTML
print "Content-Type: text/html\n"
form = cgi.FieldStorage()
modelo = form.getvalue("modelo")
#Sustituimos los espacios en blanco por % para utilizar modelo en la consulta
modelo = modelo.replace(" ", "%")
#Asignamos un valor a offset para luego incrementarlo
valoroffset = "0"
#Conexion a la base de datos y consulta segun modelo
def main():
        conn_string = "host='' dbname='' user='augusto' password=''"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select distinct(veh.idvehiculo),veh.nombreversion,veh.codigo from vehiculos veh left join vendido vt on veh.idvehiculo = vt.idvehiculo where vt.idvehiculo is null and upper(nombreversion) like "+"'%"+modelo.upper()+"%' order by veh.codigo desc LIMIT '10' OFFSET "+"'"+valoroffset+"';")
        resultado = cursor.fetchall()
	nuevovaloroffset = int(valoroffset)+10
	cursor3 = conn.cursor()
	cursor3.execute("select count(*) from vehiculos veh left join vendido vt on veh.idvehiculo = vt.idvehiculo where vt.idvehiculo is null and upper(nombreversion) like "+"'%"+modelo.upper()+"%'  LIMIT '10' OFFSET "+"'"+valoroffset+"';")
        numfilas = cursor3.fetchall()
	#Imprimimos el resultado como un html
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
	#Si el número de filas es menor a 10 no saldra el enlace de siguiente
	if numfilas[0][0] > 10:
		print "<h3><a class='siguiente' href='/cgi-bin/agente4.py?MODELO="+modelo.upper()+"&OFFSET="+str(nuevovaloroffset)+"'>Siguiente</a> >></h3>"
	print "<ul>"
	#Si el resultado de la consulta no obtiene datos significa que no hay resultados que mostrar
	if resultado == []: 
		print "<h3>No hay resultados</h3>"
		print "<h3><a href='javascript:history.back(1)'>Volver atrás</h3>"
	#En el caso de haber datos en la consulta para cada uno de ellos los tratamos acontinuación
	for coche in resultado:
		#Si no existe la imagen del coche  nos conectamos e intentamos consultarla
		if not os.path.exists("/var/www/img/"+str(coche[0])+".jpg"):
			cursor2 = conn.cursor()
                	cursor2.execute("select f.datos from vehiculos v,albumvehiculos a,ficheros fi,datosficheros f where v.idvehiculo=a.idvehiculo and fi.id=a.idficherofoto and f.masterid=a.idficherofoto and v.idvehiculo="+str(coche[0])+";")
                	mypic2 = cursor2.fetchone()
			#Si al consultarla no nos devuelve nada la url sera la de la iamgen por defecto
                	if str(type(mypic2)) == "<type 'NoneType'>":
                        	url = "<img id='vehiculo' src='/img/defecto.jpg' alt='Smiley face' height='100' width='100'></img>"
			#Si devuelve entonces la guardamos y la url sera igual a la url de la imagen
                	else:
				open("/var/www/img/"+str(coche[0])+".jpg", 'wb').write(str(mypic2[0]))
				url = "<a href='/img/"+str(coche[0])+".jpg'><img id='vehiculo' src='/img/"+str(coche[0])+".jpg' alt='Smiley face' height='100' width='100'></a>"
		#En el caso de que ya exista la imagen la url sera igua a la url de la imagen ya existente
		else:
			url = "<a href='/img/"+str(coche[0])+".jpg'><img id='vehiculo' src='/img/"+str(coche[0])+".jpg' alt='Smiley face' height='100' width='100'></a>"
		#Imprimimos cada uno de los coche como item de la lista y enlace a agente2 con el nombre de la version y el id del vehiculo
		print "<il><h3>"+str(url)+"<a href='/cgi-bin/agente2.py?idvehiculo="+str(coche[0])+"&NOMVERSION="+(coche[1])+"'>"+(coche[1])+" </a> "+"ID vehiculo: "+str(coche[2])+"</il></h3>"
	print "</ul>"
	#Si el numero de filas es menor de 10 no mostramos el enlace a la siguiente página
	if numfilas[0][0] > 10:
		print "<h3><a class='siguiente' href='/cgi-bin/agente4.py?MODELO="+modelo.upper()+"&OFFSET="+str(nuevovaloroffset)+"'>Siguiente >> </a></h3>"	
	print "<div id='footer'>"
	print "©Tododesguace.com 2013"
	print "</div>"
	print "</div>"
	print "</body>"
if __name__ == "__main__":
                main()
#fin del programa
