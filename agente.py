#!/usr/bin/python
# -*- encoding: utf-8 -*-
import psycopg2
import sys
import pprint
import cgi

#Obtenemos valores

print "Content-Type: text/html\n"
form = cgi.FieldStorage()
marca = form.getvalue("marca")
modelo = form.getvalue("modelo")
combustible = form.getvalue("combustible")
anno = form.getvalue("anno")

#Conexion a la base de datos y consulta
def main():
        conn_string = "host='' dbname='' user='' password=''"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select distinct(v.idvehiculo),v.nombreversion from vehiculos v,albumvehiculos a,ficheros fi,datosficheros f where v.idvehiculo=a.idvehiculo and fi.id=a.idficherofoto and f.masterid=a.idficherofoto and upper(nombreversion) like "+"'%"+marca.upper()+"%' and upper(nombreversion) like "+"'%"+modelo.upper()+"%' and añoversion like "+"'%"+anno+"%' and upper(otrocombustible) like "+"'%"+combustible.upper()+"%';")
        resultado = cursor.fetchall()
	print "<ul>"
	for coche in resultado:
		cursor2 = conn.cursor()
        	cursor2.execute("select f.datos from vehiculos v,albumvehiculos a,ficheros fi,datosficheros f where v.idvehiculo=a.idvehiculo and fi.id=a.idficherofoto and f.masterid=a.idficherofoto and v.idvehiculo="+str(coche[0])+";")
        	mypic2 = cursor2.fetchone()
                open("/var/www/img/"+str(coche[0])+".jpg", 'wb').write(str(mypic2[0]))
		print "<il><img src='/img/"+str(coche[0])+".jpg' alt='Smiley face' height='60' width='60'>"+(coche[1])+"</il></br>"
	print "</ul>"	
if __name__ == "__main__":
                main()
