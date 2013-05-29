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
modelo1 = form.getvalue("modelo")
modelo = modelo1.replace(" ", "%")
valoroffset = "0"

#Conexion a la base de datos y consulta
def main():
        conn_string = "host='' dbname='' user='' password=''"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select refid,(es.refid || ' ' || es.reffab1 || ' ' ||es.reffab2 || ' ' || es.refequiv) as refpieza,(art.descripcion || ' ' || ver.nombrecompleto) AS Nombrepieza from entradastock es ,articulos art,versiones ver,referencias ref where es.referencia = ref.referencia and art.idarticulo = ref.idarticulo and ver.idversion = ref.idversion and (art.descripcion || ' ' || ver.nombrecompleto|| ' ' ||es.refid || ' ' || es.reffab1 || ' ' ||es.reffab2 || ' ' || es.refequiv) like "+"'%"+modelo.upper()+"%' and ( es.ubicacion in ( 'Almacenada' ) or ( (es.ubicacion = 'Montada en vehículo' or es.ubicacion = 'En control de calidad' or es.ubicacion = 'En proceso de desmontaje') and es.estado = 'Material revisado' ) ) order by es.refid desc  LIMIT '10' OFFSET "+"'"+valoroffset+"';")
        resultado = cursor.fetchall()
	nuevovaloroffset = int(valoroffset)+10
	cursor3 = conn.cursor()
	cursor3.execute("select count(*) from entradastock es ,articulos art,versiones ver,referencias ref where es.referencia = ref.referencia and art.idarticulo = ref.idarticulo and ver.idversion = ref.idversion and (art.descripcion || ' ' || ver.nombrecompleto|| ' ' ||es.refid || ' ' || es.reffab1 || ' ' ||es.reffab2 || ' ' || es.refequiv) like "+"'%"+modelo.upper()+"%' and ( es.ubicacion in ( 'Almacenada' ) or ( (es.ubicacion = 'Montada en vehículo' or es.ubicacion = 'En control de calidad' or es.ubicacion = 'En proceso de desmontaje') and es.estado = 'Material revisado' ) );")
	numfilas = cursor3.fetchall()
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
	if resultado == []:
                print "<h3>No hay resultados</h3>"
                print "<h1><a href='javascript:history.back(1)'>Volver a intentar</h1>"
        if numfilas[0][0] > 10:
		print "<h3><p><a class='siguiente' href='/cgi-bin/agente4piezas.py?NOMPIEZA="+modelo1.upper()+"&OFFSET="+str(nuevovaloroffset)+"'>Siguiente >> </a></p></h3>"
	print "<ul>"
	for coche in resultado:
		if not os.path.exists("/var/www/img/"+str(coche[0])+".jpg"):
			cursor2 = conn.cursor()
                	cursor2.execute("select f.datos from entradastock es inner join albumpiezas a on es.refid=a.refid inner join ficheros fi on fi.id=a.idficherofoto inner join datosficheros f on f.masterid=a.idficherofoto where es.refid ="+str(coche[0])+";")
                	mypic2 = cursor2.fetchone()
                	if str(type(mypic2)) == "<type 'NoneType'>":
                        	url = "<img id='vehiculo' src='/img/defecto.jpg' alt='Smiley face' height='100' width='100'></img>"
                	else:
				open("/var/www/img/"+str(coche[0])+".jpg", 'wb').write(str(mypic2[0]))
				url = "<a href='/img/"+str(coche[0])+".jpg'><img id='vehiculo' src='/img/"+str(coche[0])+".jpg' alt='Smiley face' height='100' width='100'></a>"
		else:
			url = "<a href='/img/"+str(coche[0])+".jpg'><img id='vehiculo' src='/img/"+str(coche[0])+".jpg' alt='Smiley face' height='100' width='100'></a>"
		print "<h3><il>"+str(url)+"<a href='/cgi-bin/agente3.py?idvehiculo="+str(coche[0])+"&NOMVERSION="+str(coche[2])+"'>"+(coche[2])+"</a>   "+"ID pieza: "+str(coche[0])[0:-2]+"</il></br></h3>"
	print "</ul>"
	if numfilas[0][0] > 10:
		print "<h3><a class='siguiente' href='/cgi-bin/agente4piezas.py?NOMPIEZA="+modelo1.upper()+"&OFFSET="+str(nuevovaloroffset)+"'>Siguiente >> </a></h3>"	
	print "<div id='footer'>"
        print "©Tododesguace.com 2013"
        print "</div>"
	print "</div>"
        print "</body>"
if __name__ == "__main__":
                main()
