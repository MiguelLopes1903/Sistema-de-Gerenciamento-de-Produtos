import psycopg2

def get_connection():
    conn = psycopg2.connect(
        dbname ="postgres",
        user= "postgres",
        password = "19032007",
        host = "127.0.0.1",
        port= "5432"
)
    return conn