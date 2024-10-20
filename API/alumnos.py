def alumno_schema(alumno) -> dict:
    return {"Nombre": alumno[0],
            "Ciclo": alumno[1],
            "Curso": alumno[2],
            "Grupo": alumno[3],
            "DescAula": alumno[4]
            }

def alumnos_schema(alumnos) -> dict:
    return [alumno_schema(alumno) for alumno in alumnos]