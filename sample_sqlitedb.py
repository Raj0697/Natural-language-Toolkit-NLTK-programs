import sqlite3

try:
	sqliteconn = sqlite3.connect('example.db')
	print("Opened database successfully")

	cursor = sqliteconn.cursor()

	sqliteconn.execute('''
        CREATE TABLE if not exists student(
        	id      text,
            name    text,
            gender  text,
            course  text,);''')
	print("Table created successfully")

	cursor.execute("INSERT INTO student(id,name,gender,course) VALUES (1, 'raj', 'male', 'mca')")

	query = "SELECT * FROM student"
    cursor.execute(query)
    rows=cursor.fetchall()
    for row in rows:
    	print(row)
    sqliteconn.commit()
    sqliteconn.close()

except sqlite3.Error as e:
    print("Error :",e)