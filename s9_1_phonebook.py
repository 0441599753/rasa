import sqlite3
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()
dastoor = input("dastoor:")
if dastoor == 'contact jadid':
    nam = input("nam:")
    famili = input("famili:")
    shomare = int(input("shomare:"))
    etelaat = f"insert into phone values('{nam}' ,'{famili}', {shomare})"
    cursor.execute(etelaat)
    conn.commit()
    print("ezafe shod")
elif dastoor == 'contactha':
    open = "select * from  phone"
    cursor.execute(open)
    phones = cursor.fetchall()
    for contacts in phones:
        print(contacts)
    conn.commit()
elif dastoor == 'hazf nam':
    nam2 = input('nam:')
    delete = f"delete from phone where nam = '{nam2}'"
    cursor.execute(delete)
    conn.commit()
elif dastoor == 'joste va joo nam':
    nam3 = input('nam:')
    search = f"select * from phone where nam = '{nam3}'"
    cursor.execute(search)
    p = cursor.fetchall()
    for con in p:
        print(con)
    conn.commit()
elif dastoor == 'joste va joo shomare':
    shomare2 = int(input('shomare:'))
    search = f"select * from phone where shomare = {shomare2}"
    cursor.execute(search)
    p = cursor.fetchall()
    for con in p:
        print(con)
    conn.commit()
elif dastoor == 'hazf shomare':
    shomare3 = input('shomare:')
    delete = f"delete from phone where shomare = {shomare3}"
    cursor.execute(delete)
    conn.commit()
else:
    print("eshtebah")
