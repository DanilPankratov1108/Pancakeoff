import sqlite3
conn = sqlite3.connect('timetable.db')
c = conn.cursor()

while True:
    c.execute("""CREATE TABLE IF NOT EXISTS timetable (
                id INTEGER PRIMARY KEY,
                name TEXT,
                organizer TEXT,
                date DATE,
                time TIME
                )""")

    print('\nРасписание школьных мероприятий: Номер | Название | Организатор | Дата | Время:')
    print('add - добавить мероприятие')
    print('delete - удалить мероприятие')
    print('show - показать текущее расписание')
    print('date - изменить дату')
    print('time - изменить время начала проведения мероприятия\n')

    z = input()
    if z != 'add' and z != 'delete' and z != 'show' and z != 'date' and z != 'time':
        print('\nТакой функции не существует\n')
    else:
        if z == 'add':
            print('\nВведите название мероприятия:\n')
            n1 = input()
            print(n1)
            print('\nВведите ФИО организатора(Фамилия Имя Отчество):\n')
            def get_fio():
                n2 = input()
                if len(n2.split()) == 3:
                    return n2
                else:
                    print('\nНе тот формат записи\n')
                    get_fio()
            n2 = get_fio()
            print(n2)
            print('\nВведите дату проведения:\n')
            n3 = input()
            print(n3)
            print('\nВведите время начала проведения:\n')
            n4 = input()
            print(n4)
            c.execute('INSERT INTO timetable (name,organizer,date,time) VALUES (?, ?, ?, ?)', (n1, n2, n3, n4))
            conn.commit()
            print('\nИзменения были внесены\n')
        if z == 'delete':
            print('\nВведите номер мероприятия, которое необоходимо убрать:\n')
            r = int(input())
            c.execute('DELETE FROM timetable WHERE id=?', (r,))
            conn.commit()
            print('\nИзменения были внесены\n')
        if z == 'show':
            c.execute("SELECT * FROM timetable")
            print(c.fetchall())
        if z == 'date':
            def check_id1():
                c.execute("SELECT * FROM timetable")
                n = [i[0] for i in c.fetchall()]
                return n
            print('\nВведите номер мероприятия:\n')
            n = int(input())
            if n not in check_id1():
                print('\nТакого номера не существует\n')
            else:
                print('\nВведите новую дату:\n')
                d = input()
                c.execute('''UPDATE timetable 
                                        SET date=?
                                        Where id=?''', (d, n,))
                conn.commit()
                print('\nИзменения были внесены\n')
        if z == 'time':
            def check_id2():
                c.execute("SELECT * FROM timetable")
                r = [i[0] for i in c.fetchall()]
                return r
            print('\nВведите номер мероприятия:\n')
            r = int(input())
            if r not in check_id2():
                print('\nТакого номера не существует\n')
            else:
                print('\nВведите новое время:\n')
                t = input()
                c.execute('''UPDATE timetable 
                                    SET time=?
                                    Where id=?''', (t, r, ))
            conn.commit()
            print('\nИзменения были внесены\n')
