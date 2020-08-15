import sqlite3

def checkSetup():
    conn = sqlite3.connect('library_administration.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='admin'")
    result = cursor.fetchone()
    conn.close()
    if result is None:
        return False
    return True

def setup():
    conn = sqlite3.connect('library_administration.db')
    cursor = conn.cursor()
    create_books_table = """
        CREATE TABLE IF NOT EXISTS horarios (
            "Id" INTEGER PRIMARY KEY,
			"Horario"	TEXT NOT NULL,	
			"Data"  TEXT NOT NULL,
			"Tipo"  TEXT NOT NULL,
			"Cliente" TEXT NOT NULL,
			"Valor" TEXT NOT NULL
        );
    """
    create_students_table = """
        CREATE TABLE IF NOT EXISTS clientes (
            "Id" INT NOT NULL,
			"Nome"	TEXT NOT NULL,
			"Telefone"	INTEGER NOT NULL DEFAULT 'SEM TELEFONE',
			"Instagram"	TEXT NOT NULL DEFAULT 'SEM INSTAGRAM',
			"Idade"	TEXT NOT NULL DEFAULT 'SEM IDADE',
			PRIMARY KEY("Id")
        );
    """
    create_historioco_table = """
        CREATE TABLE IF NOT EXISTS historico (
            "Id"    INTEGER NOT NULL UNIQUE,
			"Horario"	TEXT NOT NULL,	
			"Data"  TEXT NOT NULL,
			"Tipo"  TEXT NOT NULL,
			"Cliente" TEXT NOT NULL,
			"Valor" TEXT NOT NULL,
			PRIMARY KEY("Id","Data")
        );
    """
    cursor.execute(create_books_table)
    cursor.execute(create_students_table)
    cursor.execute(create_historioco_table)
    conn.commit()
    conn.close()
setup()

def getConnection():
    return sqlite3.connect('library_administration.db')
