
#!/usr/bin/python
# -*- encoding: utf-8 -*-
import psycopg2
import sys
import pprint
import cgi
import os.path
#Obtenemos valores

print "Content-Type: text/html"
print ""
valores = cgi.FieldStorage()

modelo = valores["MODELO"].value
combustible =  valores["COMBUSTIBLE"].value
valoroffset =  valores["OFFSET"].value

def main():
        conn_string = "host'' dbname='' user='' password=''"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select distinct(v.idvehiculo),v.nombreversion,v.codigo from vehiculos v,albumvehiculos a,ficheros fi,datosficheros f where v.idvehiculo=a.idvehiculo and fi.id=a.idficherofoto and f.masterid=a.idficherofoto and upper(nombreversion) like "+"'%"+modelo.upper()+"%'and upper(otrocombustible) like "+"'%"+combustible.upper()+"%' LIMIT '10' OFFSET "+"'"+valoroffset+"';")
        resultado = cursor.fetchall()
	print "<ul>"
	for coche in resultado:
		if not os.path.exists("/var/www/img/"+str(coche[0])+".jpg"):
			cursor2 = conn.cursor()
                	cursor2.execute("select f.datos from vehiculos v,albumvehiculos a,ficheros fi,datosficheros f where v.idvehiculo=a.idvehiculo and fi.id=a.idficherofoto and f.masterid=a.idficherofoto and v.idvehiculo="+str(coche[0])+";")
                	mypic2 = cursor2.fetchone()
                	open("/var/www/img/"+str(coche[0])+".jpg", 'wb').write(str(mypic2[0]))
		print "<il><a href='/img/"+str(coche[0])+".jpg'><img src='/img/"+str(coche[0])+".jpg' alt='Smiley face' height='60' width='60'></a><a href='/cgi-bin/agente2.py?idvehiculo="+str(coche[0])+"'>"+(coche[1])+"</a>   "+"ID vehiculo: "+str(coche[2])+"</il></br>"
	print "</ul>"
	nuevovaloroffset = int(valoroffset)+10
	print "<a href='javascript:history.back(1)'>Anterior</a>"
	print "<a href='/cgi-bin/agente4.py?MODELO="+modelo.upper()+"&COMBUSTIBLE="+combustible.upper()+"&OFFSET="+str(nuevovaloroffset)+"'>Siguiente</a>"		
if __name__ == "__main__":
                main()
