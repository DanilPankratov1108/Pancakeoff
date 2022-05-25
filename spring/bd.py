import sqlite3
import os

def central():
    Names = []
    for i in os.listdir():
        if i[-3:] == ".db":
            Names.append(i)
    s = "Выберите вариант : + : создать новую  .db, - : удалить дб  "
    for i, j in enumerate(Names):
        s += f"\n{i + 1}) {j}"
    print(s)
    s = input("Выберите действие :")

    try:
        s = int(s)
        get_tables(Names[s - 1])
    except:
        if s == "+":
            name = input("Введите имя ")
            w = open(name + ".db", "w+")
            w.close()
        elif s == "-":
            name = int(input("Выберите какую хотите удалить "))
            os.remove(Names[name - 1])
        # central()


def get_tables(S):
    con = sqlite3.connect(S)
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    Names = cursor.fetchall()
    Names = [i[0] for i in Names]
    s = "Выберите вариант : + : создать новую  таблицу , - : удалить сущетсвующую  "
    for i, j in enumerate(Names):
        s += f"\n{i + 1}) {j}"
    print(s)
    s = input("Выберите действие :")
    if s == "+":
        st = input("Введите имя ")
        com = f"""CREATE TABLE {st} ( id INTEGER PRIMARY KEY AUTOINCREMENT,
"""
        mass = ["text ", "INTEGER"]
        while (st != "0"):
            st = input("хотите добавить столбик : 1 da 0 -net")
            if st == "1":
                x = input("choose name ")
                com += x
                com += " "
                y = [print(i + 1, j) for i, j in enumerate(mass)]
                x = int(input(f"choose type {y}"))

                com += str(mass[x - 1])
                com += ","
        com = com[:-1]
        com += ")"

        cursor.execute(com)
        con.commit()
        get_tables(S)
    elif s == "-":
        n = int(input("выберите из списка "))
        print(Names[n - 1])
        cursor.execute(f"DROP TABLE {Names[n - 1]} ")
        con.commit()
        get_tables(S)
    elif type(int(s)) == int:
        table(Names[i - 1], con, cursor)


def table(S, con, cursor):
    cursor.execute(f"select * From {S}")
    x = cursor.fetchall()
    for i, o in enumerate(x):
        print(i + 1, end=" )")
        for j, k in enumerate(o):
            print(k, end=", ")
        print("")

    s = input("Выберите действие : + добавить, - удалить,~ - edit , 0 закончить")
    if s == "-":

        s = f"DELETE FROM {S} WHERE id={x[int(input('выберите из списка')) - 1][0]}"
        cursor.execute(s)
        con.commit()
        table(S, con, cursor)
    elif s == "+":
        cursor.execute(f"PRAGMA table_info({S})")
        s = cursor.fetchall()
        st = f"insert into {S}("
        for i in s:
            st += i[1]
            st += ","
        st = st[0:-1]
        st += ") Values("
        for i in range(len(s)):
            st += input(f"{s[i][1]} ({s[i][2]}) : ")
            st += ","
        st = st[0:-1]
        st += ")"
        cursor.execute(st)
        if con.commit():
            print("succses")
        table(S, con, cursor)
    elif s == "~":
        cursor.execute(f"PRAGMA table_info({S})")
        s = cursor.fetchall()
        n = x[int(input('выберите из списка')) - 1][0]
        for i, o in enumerate(s):
            print(f"{i + 1} ) {o[1]}")
        m = int(input("что изменить :")) - 1
        l = input(f'{s[m][1]} :')
        # Update SqliteDb_developers set salary = 10000 where id = 4
        st = f"Update {S} set {s[m][i]} = '{l}' where id = {n}"
        print(st)
        cursor.execute(st)
        con.commit()
        if con.commit():
            print("succses")
        table(S, con, cursor)
    else:
        exit()


central()
