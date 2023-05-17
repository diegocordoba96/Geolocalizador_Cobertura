1 - Creamos entorno virtual py -m venv entv
2 - Activamos entorno virtual .\entv\Scripts\activate
3 - Instalamos requerimientos pip install -r requirements.txt
4 - Creamos base de datos en postgres y le instalamos extensión postgis
5 - Em el archivo settings en la linea 139 configuramos la base de datos creada
4 - ejecutamos migraciones .\manage.py migrate 
5 - creamos super usuario para crear poligonos py .\manage.py createsuperuser
6 - ejecutamos proyecto py .\manage.py runserver 
