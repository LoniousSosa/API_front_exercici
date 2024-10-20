![image](https://github.com/user-attachments/assets/77ce2b2f-0e2d-4b38-80e7-02fc11e66229)

He logrado esto con esta linea de código: @app.get("/", response_class=HTMLResponse) async def read_index(): return FileResponse("API_front_exercici/front/html/index.html")

En cuanto a la lista de alumnos se muestra así, tanto el script como el css están hardcodeados ya que por link, aunque la ruta este bien o se ponga ruta absoluta no puede acceder a los archivos.

![image](https://github.com/user-attachments/assets/434e49f4-786f-4aca-8b7e-d7a9d206ad3c)
