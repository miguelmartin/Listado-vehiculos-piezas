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
        cursor.execute("select v.idvehiculo,v.nombreversion,f.datos from vehiculos v,albumvehiculos a,ficheros fi,datosficheros f where v.idvehiculo=$
        resultado = cursor.fetchall()
        #IMprimir resultados por pantalla.
        print resultado
        #Segundo formulario solicitando el id del vehiculo para mostrar su listado de piezas.
        print "<form method='post' action='/cgi-bin/agente2.py'> Ingresa el id: <input name='idvehiculo' type='text' value='idvehiculo' /><input type$

if __name__ == "__main__":
        main()



