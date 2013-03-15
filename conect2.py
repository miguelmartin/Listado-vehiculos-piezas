# -*- encoding: utf-8 -*-
import psycopg2
import sys
import pprint
from getpass import getpass
contrasenna = getpass("Contrasenna: ")
def main():
	conn_string = "host='localhost' dbname='prueba' user='postgres' password='%S'" % contrasenna
 	conn = psycopg2.connect(conn_string)
 	cursor = conn.cursor()
 	cursor.execute("select dni,telefono from clientes;")
 	records = cursor.fetchall()
 	pprint.pprint(records)
if __name__ == "__main__":
	main()
