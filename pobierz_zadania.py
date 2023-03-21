import sqlite3

def pobierz_zadania():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    # pobierz listę zadań z bazy danych
    c.execute("SELECT * FROM zadania")
    zadania = c.fetchall()

    conn.close()

    return zadania
