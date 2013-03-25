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
        conn_string = "host='192.168.1.250' dbname='crvnet5' user='augusto' password='%s'" % contrasenna
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select idvehiculo,nombreversion from vehiculos where upper(nombreversion) like "+"'%"+marca.upper()+"%' and upper(nombreversion) like "+"'%"+modelo.upper()+"%' and añoversion like "+"'%"+anno+"%' and upper(otrocombustible) like "+"'%"+combustible.upper()+"%';")
        records = cursor.fetchall()
        pprint.pprint(records)
if __name__ == "__main__":
        main()

idvehiculo = raw_input("Introduce el id del vehiculo: ")

def main():
        conn_string = "host='192.168.1.250' dbname='crvnet5' user='augusto' password='%s'" % contrasenna
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select art.descripcion,es.refid,es.referencia,es.ubicacion,es.estado,es.nota,ver.nombrecompleto from entradastock es inner join referencias ref on es.referencia = ref.referencia inner join articulos art on art.idarticulo = ref.idarticulo inner join versiones ver on ver.idversion = ref.idversion where refid in (select refid from stockvehiculo where idvehiculo = "+"'"+idvehiculo+"');")
        records = cursor.fetchall()
        pprint.pprint(records)
if __name__ == "__main__":
        main()
