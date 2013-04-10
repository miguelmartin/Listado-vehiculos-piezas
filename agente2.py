#!/usr/bin/python
# -*- encoding: utf-8 -*-
import psycopg2
import sys
import pprint
import cgi

#Obtenemos valores

print "Content-Type: text/html\n"
form = cgi.FieldStorage()
idvehiculo = form.getvalue("idvehiculo")

#Conexion a la base de datos y consulta
def main():
        conn_string = "host='' dbname='' user='' password=''"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select art.descripcion,es.refid from entradastock es inner join referencias ref on es.referencia = ref.referencia inner join $
        records = cursor.fetchall()
        pprint.pprint(records)
if __name__ == "__main__":
        main()

