# pip install pysqlite3

import sqlite3

banco = sqlite3.connect('./SQLite/meubanco.db')

cursor = banco.cursor()

cursor.execute("create table pessoas (nome text, idade integer, email text)")

cursor.execute("insert into pessoas values ('Maria', 40, 'maria123@gmail.com')")
cursor.execute("insert into pessoas values ('João', 47, 'jaun@gmail.com')")
cursor.execute("insert into pessoas values ('Pedro', 32, 'pedro90@gmail.com')")

banco.commit()

cursor.execute("select * from pessoas")

print(cursor.fetchall())