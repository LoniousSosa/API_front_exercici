![image](https://github.com/user-attachments/assets/77ce2b2f-0e2d-4b38-80e7-02fc11e66229)


He logrado esto con esta linea de código: @app.get("/", response_class=HTMLResponse) async def read_index(): return FileResponse("API_front_exercici/front/html/index.html")

En cuanto a la lista de alumnos se muestra así, tanto el script como el css están hardcodeados ya que por link, aunque la ruta este bien o se ponga ruta absoluta no puede acceder a los archivos.

![image](https://github.com/user-attachments/assets/434e49f4-786f-4aca-8b7e-d7a9d206ad3c)


Ahora para las consultas avanzadas, realizaré unas pruebas para ver como funcionan:

skip con limit 1 y skip 0:
![image](https://github.com/user-attachments/assets/2c155f53-e526-432b-ac85-3e7a66986678)

![image](https://github.com/user-attachments/assets/0bf13232-bb21-413a-90d7-a2dd414828f1)

Alumnos por id: 
![image](https://github.com/user-attachments/assets/22cc92bd-af7b-4ad3-a5f6-87a5851afb2a)


skip con limit 1 y skip 0:
![image](https://github.com/user-attachments/assets/a3fa8353-1bf6-47b4-b36a-975e6054e4ee)

![image](https://github.com/user-attachments/assets/814290e7-66a7-4bb6-8758-4132821b22c1)



En la primea imagen se ve como solo se muestra un solo alumno, siendo el de id 1. Sin embargo, en la segunda se puede ver al otro alumno, ya que en la setencia declaramos que
empiece por el segundo registro.


