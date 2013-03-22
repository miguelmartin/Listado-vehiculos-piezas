# -*- encoding: utf-8 -*-
import psycopg2
import sys
import pprint
from getpass import getpass
contrasenna = getpass("Contrasenna: ")

#Le pedimos al usuario los datos de los vehículos que le interesan
marca = raw_input("Introduce la marca: ")
modelo = raw_input("Introduce el modelo: ")
anno = raw_input("Introduce el año: ")
combustible = raw_input("Introduce el combustible: ")

#realizamos la consulta con los datos pedidos anteriormente

def main():
        conn_string = "host='' dbname='' user='' password='%s'" % contrasenna
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select idvehiculo,nombreversion from vehiculos where upper(nombreversion) like "+"'%"+marca.upper()+"%' and upper(nombreversion) like "+"'%"+modelo.upper()+"%' and añoversion like "+"'%"+anno+"%' and upper(otrocombustible) like "+"'%"+combustible.upper()+"%';")
        records = cursor.fetchall()
        pprint.pprint(records)
if __name__ == "__main__":
        main()
#en el resultado de esta primera parte podremos ver el id del vehiculo del cual queremos un listado de las piezas, pueden ser varios

idvehiculo = raw_input("Introduce el id del vehiculo: ")

def main():
        conn_string = "host='' dbname='' user='' password='%s'" % contrasenna
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select referencia,metadatos,ubicacion from entradastock where refid in (select refid from stockvehiculo where idvehiculo = "+"'"+idvehiculo+"');")
        records = cursor.fetchall()
        pprint.pprint(records)
if __name__ == "__main__":
        main()
