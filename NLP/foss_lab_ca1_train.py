import sqlite3

conn = sqlite3.connect('train.db')
cursor = conn.cursor()

print ("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS Train_details
         (Train_no INT PRIMARY KEY     NOT NULL,
          Train_name           TEXT    NOT NULL,
          No_of_passengers     INT     NOT NULL)''')

conn.execute('''CREATE TABLE IF NOT EXISTS Ticket
			(Train_no INT  NOT NULL,
			Ticket_amount INT NOT NULL,
			FOREIGN KEY(Train_no) REFERENCES Train_details(Train_no) )''')
print ("Table created successfully")

cursor.execute('''INSERT INTO Train_details(Train_no,Train_name,No_of_passengers) values(101,'Delhiexpress',500)''')
cursor.execute('''INSERT INTO Train_details(Train_no,Train_name,No_of_passengers) values(102,'Mumbaiexpress',800)''')

cursor.execute('''INSERT INTO Ticket(Train_no,Ticket_amount) values(101,500)''')
cursor.execute('''INSERT INTO Ticket(Train_no,Ticket_amount) values(102,600)''')

query = "SELECT Ticket_amount from Ticket"
cursor.execute(query)
conn.commit()
print ("Train details inserted successfully")

conn.close()