import sqlite3

def usun_zadanie(id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    # usuń zadanie o podanym ID z bazy danych
    c.execute("DELETE FROM zadania WHERE id=?", (id,))

    conn.commit()
    conn.close()
