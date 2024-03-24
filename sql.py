import sqlite3

##connect to sqlite

connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table, retrieve

cursor = connection.cursor()

## Create Table

table_info = """

Create table Student(Name Varchar(25),class varchar(25),Section Varchar(25),marks INT);

"""

cursor.execute(table_info)

##insert some more records

cursor.execute('''Insert into Student values('Krish','Data Science','A',90)''')
cursor.execute('''Insert into Student values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert into Student values('Darius','Data Science','A',86)''')
cursor.execute('''Insert into Student values('Vikash','Devops','A',50)''')
cursor.execute('''Insert into Student values('Dipesh','Devops','A',35)''')


##Display all the records

print("The inserted records are")

data = cursor.execute('''Select * from Student''')

for row in data:
    print(row)

## Close the connection
    
connection.commit()
connection.close()

