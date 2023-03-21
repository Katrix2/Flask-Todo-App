import sqlite3
from datetime import datetime

def dodaj_zadanie(tresc):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    # pobierz obecną datę i czas
    teraz = datetime.now()

    # dodaj nowe zadanie do bazy danych
    c.execute("INSERT INTO zadania (tresc, data_utworzenia) VALUES (?, ?)", (tresc, teraz))

    conn.commit()
    conn.close()
