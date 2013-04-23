#!/usr/bin/python
# -*- encoding: utf-8 -*-

import cgi
import cgitb; cgitb.enable() # Optional; for debugging only
import psycopg2
import sys
import pprint
import cgi

print "Content-Type: text/html"
print ""
arguments = cgi.FieldStorage()
for i in arguments.keys():
 codvehiculo =  arguments[i].value

#Conexion a la base de datos y consulta
def main():
        conn_string = "host='192.168.1.250' dbname='crvnet5' user='augusto' password='augusto2013'"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select art.descripcion,es.refid from entradastock es inner join referencias ref on es.referencia = ref.referencia inner join articulos art on art.idarticulo = ref.idarticulo inner join versiones ver on ver.idversion = ref.idversion where es.refid in (select refid from stockvehiculo where idvehiculo = "+str(codvehiculo)+") ;")
        resultado = cursor.fetchall()
        print "<img src='/img/"+str(codvehiculo)+".jpg' alt='Smiley face' height='220' width='220'></img>"
        print "<ul>"
        for pieza in resultado:
               print "<a href='/cgi-bin/agente3.py?idvehiculo="+str(pieza[1])+"'><il>"+(pieza[0])+"</il></a><br/>"
        print "</ul>"

if __name__ == "__main__":
        main()

