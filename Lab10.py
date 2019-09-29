# Tyler Stamp
# Lab 10
# 12/02/18

import sqlite3


conn = sqlite3.connect('StudentRecord.db')

'''Creating Student and Grade Table'''
conn.execute('''CREATE TABLE Student
    (studentID int,
    name varchar(255),
    address varchar(255),
    status varchar(255)
    )''')
conn.execute('''CREATE TABLE Grade
    (studentID int,
     name varchar(255),
     GPA float,
     major varchar(255)
    )''')

conn.close()
'''Selecting names and addresses of all freshmen'''
cursor = conn.execute('''SELECT studentID, name, address, status from STUDENT''')
for row in cursor:
    if(status == 'Freshman'):
        print("Name =", row[2])
        print("Status =", row[3],"\n")

'''Selecting names and ID of all seniors and juniors'''
cursor = conn.execute('''SELECT studentID, name, address, status from STUDENT''')
for row in cursor:
    if(status == 'Freshman'):
        print("Name =", row[2])
        print("ID =", row[1],"\n")
        
'''Inserting initial values for each table'''
conn.execute('''INSERT INTO Student
    (studentID, name, address, status)\
    VALUES(111111,'John Doe','123 Main St','Freshman')''');
conn.execute('''INSERT INTO Student
    (studentID, name, address, status)\
    VALUES(666666, 'Joseph Public', '666 Hollow Rd', 'Sophomore')''');
conn.execute('''INSERT INTO Student
    (studentID, name, address, status)\
    VALUES(525252, 'Amy Vis', '431 Diamond Rd', 'Senior')''');
conn.execute('''INSERT INTO Student
    (studentID, name, address, status)\
    VALUES(112233, 'Mary Smith', '1 Lake St', 'Freshman')''');
conn.execute('''INSERT INTO Student
    (studentID, name, address, status)\
    VALUES(987654, 'Bart Simpson', 'Fox 5 TV', 'Senior')''');
conn.execute('''INSERT INTO Student
    (studentID, name, address, status)\
    VALUES(023412, 'Homer Simpson', 'Fox 5 TV', 'Senior')''');
conn.execute('''INSERT INTO Student
    (studentID, name, address, status)\
    VALUES(144335, 'Joe Blow', '6 Yard Ct', 'Junior')''');

conn.execute('''INSERT INTO Grade
    (studentID, name, GPA, major)\
    VALUES(111111, 'John Doe', 4.0, 'CS')''');
conn.execute('''INSERT INTO Grade
    (studentID, name, GPA, major)\
    VALUES(666666, 'Joseph Public', 2.3, 'Bio')''');
conn.execute('''INSERT INTO Grade
    (studentID, name, GPA, major)\
    VALUES(134134, 'Kay Reed', 3.8, 'CS')''');
conn.execute('''INSERT INTO Grade
    (studentID, name, GPA, major)\
    VALUES(112233, 'Mary Smith', 3.0, 'Chem')''');
conn.execute('''INSERT INTO Grade
    (studentID, name, GPA, major)\
    VALUES(987654, 'Bart Simpson', 3.7, 'Bio')''');
conn.execute('''INSERT INTO Grade
    (studentID, name, GPA, major)\
    VALUES(144335, 'Joe Blow', 3.09, 'Chem')''');
conn.execute('''INSERT INTO Grade
    (studentID, name, GPA, major)\
    VALUES(525252, 'Amy Vis', 3.5, 'CS')''');

conn.close()

'''Removing Homer Simpson from STUDENT table'''
conn.execute("DELETE from STUDENT where studentID = 023412")
conn.commit()

'''Changing Mary Smith's Address'''
conn.execute("UPDATE STUDENT set address = '100 Lake St' where studentID = 112233")
conn.commit()

'''Deleting Jane Cook'''
conn.execute('''DELETE from STUDENT where name = "Jane Cook"''')
conn.commit()

'''Finding Name and Major of all whose GPA is 3.0 or lower'''
cursor = conn.execute('''SELECT studentID, name, GPA, major from GRADE''')
for row in cursor:
    if(GPA <= 3.0):
        print("Name =", row[2])
        print("Major =", row[4],"\n")

'''Finding the name and address of all CS students'''
cursor = conn.execute('''SELECT studentID, name, address, status from STUDENT''')
for row in cursor:
    if(major == 'CS'):
        print("Name =", row[1])
        print("Address =", row[3])
    
conn.close()


