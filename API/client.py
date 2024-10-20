import mysql.connector

def db_client():

    try:
        dbname = "alumnat"
        user = "root"
        password = "1234"
        host = "localhost"
        port = "3306"
        collation = "utf8mb4_general_ci"
        
        return mysql.connector.connect(
            host = host,
            port = port,
            user = user,
            password = password,
            database = dbname,
            collation = collation
        )
    
    except mysql.connector.Error as e:
        raise Exception(f"Error de connexión: {e}")