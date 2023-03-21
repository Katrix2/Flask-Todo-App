import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()

# utwórz tabelę zadan
c.execute('''
    CREATE TABLE zadania
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
     tresc TEXT NOT NULL,
     data_utworzenia DATE NOT NULL);
''')

conn.commit()
conn.close()
