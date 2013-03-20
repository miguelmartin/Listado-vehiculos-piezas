# -*- encoding: utf-8 -*-
import psycopg2
import sys
import pprint
from getpass import getpass
contrasenna = getpass("Contrasenna: ")

marca = raw_input("Introduce la marca: ")
modelo = raw_input("Introduce el modelo: ")
anno = raw_input("Introduce el año: ")
combustible = raw_input("Introduce el combustible: ")

def main():
        conn_string = "host='' dbname='' user='' password='%s'" % contrasenna
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select nombreversion from vehiculos where upper(nombreversion) like "+"'%"+marca+"%' and upper(nombreversion) like "+"'%"+mod$
        records = cursor.fetchall()
        pprint.pprint(records)
if __name__ == "__main__":
        main()

