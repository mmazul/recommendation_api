import psycopg2

engine = psycopg2.connect(
    database="postgres",
    user="",
    password="",
    host="",
    port='5432'
)

cursor = engine.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS TABLA(ID int primary key);""")
