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
        cursor2 = conn.cursor()
        cursor2.execute("select f.datos from vehiculos v,albumvehiculos a,ficheros fi,datosficheros f where v.idvehiculo=a.idvehiculo and fi.id=a.idficherofoto and f.masterid=a.idficherofoto and v.idvehiculo='%s';" %resultado[0][0]) 
        for mypic2 in cursor2.fetchall():
                open("/var/www/img/"+str(resultado[0][0])+".jpg", 'wb').write(str(mypic2[0]))
	        print "<ul>"
	        print "<li><img src='/img/"+str(resultado[0][0])+".jpg' alt='Smiley face' height='60' width='60'>'%s'</li>" %resultado[0][1]
	        print "</ul>"
	        print "<form method='post' action='/cgi-bin/agente2.py'> Ingresa el id: <input name='idvehiculo' type='text' value='idvehiculo' /><input type='submit' value='Consultar' /></form> "
	
        if __name__ == "__main__":
                main()


