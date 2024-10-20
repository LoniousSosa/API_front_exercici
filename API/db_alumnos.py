from API_front_exercici.API.client import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT alumne.Nombre, alumne.Ciclo, alumne.Curso, alumne.Grupo, aula.DescAula " + 
            "FROM alumne INNER JOIN aula ON alumne.idAula = aula.idAula")
        alumnos = cur.fetchall()

    except Exception as e:
        return {"status":-1, "message": f"Error de connexión:{e}"}
    
    finally:
        conn.close()

    return alumnos


def read_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = ("select * from alumne where idAlumne = %s")
        idValue = (id,)
        cur.execute(query,idValue)
        alumno = cur.fetchall()
    
    except Exception as e:
        return {"status":-1, "message": f"Error de connexión:{e}"}
    
    finally:
        conn.close()
    
    return alumno

def create(idAula,nombre,ciclo,grupo,createdAt,updatedAt):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "insert into alumne (idAula,Nombre,Ciclo,Grupo,CreatedAt,UpdatedAt) VALUES (%s,%s,%s,%s,%s,%s);"
        values=(idAula,nombre,ciclo,grupo,createdAt,updatedAt)
        cur.execute(query,values)
    
        conn.commit()
        alumne_id = cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return alumne_id

def update_alumne(idAlumne,nombre,ciclo,curso,grupo):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "update alumne SET Nombre = %s, Ciclo = %s,Curso = %s,Grupo = %s WHERE idAlumne = %s;"
        values=(nombre,ciclo,curso,grupo,idAlumne)
        cur.execute(query,values)
        updated_recs = cur.rowcount
    
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return updated_recs

def delete_alumne(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "DELETE FROM alumne WHERE idAlumne = %s;"
        cur.execute(query,(id,))
        deleted_recs = cur.rowcount
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
        
    return deleted_recs