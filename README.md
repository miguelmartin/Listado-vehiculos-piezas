Listado-vehiculos-piezas
========================

Conectar a Web API y generar un listado en HTML.

Este es un commit de prueba desde Debian


El proyecto va a consistir en la creación de una aplicación, através de una API privada,  a la cual nos ofrecen conectarnos, para sacar un listado con sus correspondientes imágenes de los vehículos almacenados en mi base de datos. Es decir tengo una base de datos dónde almaceno los vehículos y piezas, las mismas personas que generaron la base de datos, nos ofrecen una API privada, a la que conectarnos, para poder extraer información de los vehículos almacenados, información como el nombre, color, numero de puertas, imágenes etc.., y a partir de está información generar un HTML con un listado de los vehículos y los datos deseados.


De está manera utilizaremos, APIS, en este caso privada, Bases de datos, en este caso utilizaremos la base de datos que tenemos dónde están almacenados los vehículos y archivos, como por ejemplo las imágenes.


Conectar a base de datos postgres desde linux para comprobar que tenemos conexión:

La W es para forzar a que nos pida la contraseña:

psql -h nombre_o_ip_servidor -d nombre_bd -U usuario -W

Todo esto después de comprobar en el servidor de postgres, que en el fichero pg_hba.conf hemos puesto que acepte las conexiones desde la ip 

o rango de IP`s que eligamos:

