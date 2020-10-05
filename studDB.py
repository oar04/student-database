import sqlite3
def DB_Connect():
    try:
        global conn
        global cur
        conn = sqlite3.connect("studDB.db")
        cur = conn.cursor()
        #cur.execute("drop table if exists Student")
        cur.execute("CREATE TABLE if NOT EXISTS Student \
                (studID INTEGER PRIMARY KEY AUTOINCREMENT,\
                studName VARCHAR (25) NOT NULL,\
                studSurname VARCHAR (25),\
                studMark DECIMAL (7, 2) NOT NULL,\
                studImgLoc VARCHAR (25),\
                studStatus tinyint(1) NOT NULL DEFAULT 1)")
        conn.commit()
        #conn.close()
    except Error as e:
        print(e)


def menu():
    print()
    print()
    print("\t\tStudent Database Operations")
    print()
    print("a. View All Students :")
    print()
    print("b. Add a New Student :")
    print()
    print("c. Update a Student :")
    print()
    print("d. Delete a Student :")
    print()
    print("e. Search for Student :")
    print()
    print("q. quit")
    print()
    choice = input("Enter your choice:")
    return choice[0].lower()

def View():
    #cur.execute('Select * from Student')
    #rows = cur.fetchall()
    #print(rows)

    conn = sqlite3.connect("studDB.db")
    cur=conn.cursor()
    cur.execute("select * from Student")
    rows = cur.fetchall()
    print(rows)
    conn.close()
    return rows


def Add(name, Surname, Mark, imageloc):
    cur.execute("insert into Student values (null,?,?,?,?,?)",\
                (name, Surname, Mark, imageloc, 1))
    conn.commit()

def Update(id, studName, studSurname, studMark, studImgLoc, studStatus):
    cur.execute("update Student set \
    studName=?, studSurname =?, studMark =?, studImgLoc = ?, studStatus =? \
    where studID=?", (studName, studSurname, studMark, studImgLoc, studStatus, id))
    conn.commit()

def Delete(id):
    cur.execute("DELETE FROM Student WHERE studID=?", (id,))
    conn.commit()

def Search(id="", name=""):
    conn = sqlite3.connect("studDB.db")
    cur.connection.cursor()
    cur.execute("SELECT * FROM Student WHERE studID=?", (id,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()
    return rows
    

def main():
    DB_Connect()
    while(True):
        choice = menu()
        if (choice == 'a'):
            print()
            print("View All Selected")
            View()
            print()
        elif(choice == 'b'):
            print("Add a New Student Selected")
            name = input("Enter Student Name")
            Surname = input("Enter Student Surname Title")
            Mark = input("Enter Student Mark")
            imageloc = input("Enter Student Image Location")
            Add(name, Surname, Mark, imageloc)
            print("Record Added")
            Add('Any Body ', 'Admin', 34000, 'img/st1.png')
            print()

        elif(choice == 'c'):
            print("Update a Student Selected")
            studID = input("Enter Student id to be updated: ")
            name = input("Enter Student Name")
            Surname = input("Enter Student Surname Title")
            Mark = input("Enter Student Mark")
            imageloc = input("Enter Student Image Location")
            Update(studID, name , Surname, Mark, imageloc, 1)
            print()

        elif(choice == 'd'):
            print("Delete an Student Selected")
            studID = input("Enter studID for Student to be deleted:")
            Delete(studID)
            print()

        elif(choice == 'e'):
            print("Search for an Student Selected")
            studID = input("Enter studID for Student to be searched:")
            Search(studID)
            print()
        
        elif(choice == 'q'):
            print("You Have Quit The Program")
            print()
            break
        
        else:
            print()
            print("invalid choice - try again")
            print()
           
    conn.close()



main()
