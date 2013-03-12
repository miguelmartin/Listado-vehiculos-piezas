# -*- encoding: utf-8 -*-
import psycopg2
import sys
import pprint
def main():
	conn_string = "host='localhost' dbname='prueba' user='postgres' password='usuario'"
 	conn = psycopg2.connect(conn_string)
 	cursor = conn.cursor()
 	cursor.execute("select dni,telefono from clientes;")
 	records = cursor.fetchall()
 	pprint.pprint(records)
if __name__ == "__main__":
	main()
