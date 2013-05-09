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
nompieza =  valores["NOMPIEZA"].value
refpieza = valores["REFPIEZA"].value
valoroffset =  valores["OFFSET"].value

def main():
        conn_string = "host='' dbname='' user='' password=''"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select refid,(es.refid || ' ' || es.reffab1 || ' ' ||es.reffab2 || ' ' || es.refequiv) as refpieza,(art.descripcion || ' ' || ver.nombrecompleto) AS Nombrepieza from entradastock es ,articulos art,versiones ver,referencias ref where es.referencia = ref.referencia and art.idarticulo = ref.idarticulo and ver.idversion = ref.idversion and (art.descripcion || ' ' || ver.nombrecompleto) like "+"'%"+nompieza.upper()+"%' and (es.refid || ' ' || es.reffab1 || ' ' ||es.reffab2 || ' ' || es.refequiv) like "+"'%"+refpieza.upper()+"%' and ver.nombrecompleto like "+"'%"+modelo.upper()+"%'  LIMIT '10' OFFSET "+"'"+valoroffset+"';")
        resultado = cursor.fetchall()
 nuevovaloroffset = int(valoroffset)+10
	print "<a href='javascript:history.back(1)'>Anterior</a>"
	print "<a href='/cgi-bin/agente4piezas.py?NOMPIEZA="+nompieza.upper()+"&REFPIEZA="+refpieza.upper()+"&MODELO="+modelo.upper()+"&OFFSET="+str(nuevovaloroffset)+"'>Siguiente</a>"
	print "<ul>"
	for coche in resultado:
		if not os.path.exists("/var/www/img/"+str(coche[0])+".jpg"):
			cursor2 = conn.cursor()
                	cursor2.execute("select f.datos from entradastock es inner join albumpiezas a on es.refid=a.refid inner join ficheros fi on fi.id=a.idficherofoto inner join datosficheros f on f.masterid=a.idficherofoto where es.refid ="+str(coche[0])+";")
                	mypic2 = cursor2.fetchone()
                	if str(type(mypic2)) == "<type 'NoneType'>":
                        	url = "<img src='/img/defecto.jpg' alt='Smiley face' height='60' width='60'></img>"
                	else:
				open("/var/www/img/"+str(coche[0])+".jpg", 'wb').write(str(mypic2[0]))
				url = "<a href='/img/"+str(coche[0])+".jpg'><img src='/img/"+str(coche[0])+".jpg' alt='Smiley face' height='60' width='60'></a>"
		else:
			url = "<a href='/img/"+str(coche[0])+".jpg'><img src='/img/"+str(coche[0])+".jpg' alt='Smiley face' height='60' width='60'></a>"
		print "<il>"+str(url)+"<a href='/cgi-bin/agente3.py?idvehiculo="+str(coche[0])+"'>"+(coche[2])+"</a>   "+"ID pieza: "+str(coche[0])+"</il></br>"
	print "</ul>"	
	print "<a href='javascript:history.back(1)'>Anterior</a>"
	print "<a href='/cgi-bin/agente4piezas.py?NOMPIEZA="+nompieza.upper()+"&REFPIEZA="+refpieza.upper()+"&MODELO="+modelo.upper()+"&OFFSET="+str(nuevovaloroffset)+"'>Siguiente</a>"	
if __name__ == "__main__":
                main()
