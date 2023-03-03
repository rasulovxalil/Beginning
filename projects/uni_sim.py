import sqlite3

class University:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.status = True

        self.connectdatabase()

    def run(self):
        self.menu()
        self.status = False

        choice = self.choice()

        if choice == 1:
            self.addstudent()
        if choice == 2:
            self.deletestudent()
        if choice == 3:
            self.updatestudent()
        if choice == 4:
            while True:
                try:
                    orderby = int(input("1)all\n2)Faculty\n3)Department\n4)Type\n5)Status\nSelect: "))
                    if orderby < 1 or orderby > 5:
                        continue

                except ValueError:
                    print("Must be integer")
            self.showallstudents(orderby)
        if choice == 5:
            pass

    def menu(self):
        print("***** {} Administration System *****".format(self.name))
        print("\n1) Add Student\n2)Delete Student\n3)Update Student\n4)Show All Students\n5)Exit")

    def choice(self):
        while True:
            try:
                process = int(input("Select: "))
                if process <1 or process>5:
                    print("Operation must be between 1 - 5, please select correct numbers")
                    continue
                break
            except ValueError:
                print("Operation must be integer number.Please write correct type.")
        return process

    def addstudent(self):
        print("*** Student Information ***")
        name = input("Student's name: ").lower().capitalize()
        surname = input("Student's surname: ").lower().capitalize()
        faculty = input("Student's faculty: ").lower().capitalize()
        department = input("Student's department: ").lower().capitalize()
        stid = input("Student's ID: ")

        while True:
            try:
                typ = int(input("Student's education type: "))
                if typ <1 or typ > 2:
                    print("Student's education type must be 1 or 2\n")
                    continue
                break
            except ValueError:
                print("Student's education type must be 1 or 2\n")

        status = "Active"

        self.cursor.execute("INSERT INTO students VALUES('{}','{}','{}','{}','{}',{},'{}')".format(name,surname,faculty,department,stid,typ,status))
        self.connect.commit()
        print("Student name {} {} succesfully added".format(name,surname))



    def deletestudent(self):
        self.cursor.execute("SELECT * FROM students")
        allstudents = self.cursor.fetchall()


        convertalllstring = lambda x: [str(y) for y in x]

        for i,j in enumerate(allstudents,1 ):
            print("{}{}".format(i," ".join(convertalllstring(j))))
        while True:
            try:
                select = int(input("Select the student to be deleted: "))
                break
            except ValueError:
                print("Please write correct type(int)")
        self.cursor.execute("DELETE FROM students WHERE ROWID {}".format(select))
        self.connect.commit()

        print("\nStudent succcesfully deleted")


    def updatestudent(self):
        self.cursor.execute("SELECT * FROM students")
        allstudents = self.cursor.fetchall()

        convertalllstring = lambda x: [str(y) for y in x]

        for i, j in enumerate(allstudents, 1):
            print("{}{}".format(i, " ".join(convertalllstring(j))))
        while True:
            try:
                select = int(input("\nSelect the student to be Updated: "))
                break
            except ValueError:
                print("Please write correct type(int)")
        self.cursor.execute("DELETE FROM students WHERE rowid={}".format(select))
        self.connect.commit()

        print("\nStudent succcesfully deleted")
        while True:
            try:
                updateselect =int(input("1)Name\n2)Surname\n3)Faculty\n4)Department\n5)Student ID\n6)Education Type\n7)Status"))
                if updateselect <1 or updateselect>7:
                    continue
                else:
                    break
            except ValueError:

                print("It must be int")
        operations = ["name","surname","faculty","department","stid","typ","status"]
        if updateselect == 6:
            while True:
                try:
                    newvalue = int(input("Enter the new value: "))
                    if newvalue not in (1,2):
                        continue
                    break
                except ValueError:
                    print("please, it must be integer!\n")

            self.cursor.execute("UPDATE students SET typ={} WHERE rowid={}".format(newvalue,select))
        else:
            newvalue =input("Enter the new value: ")
            self.cursor.execute("UPDATE students SET {}='{}' WHERE rowid={}".format(operations[updateselect-1],newvalue,select))

        self.connect.commit()

        print("Update Succes")
    def showallstudents(self,by):
        if by == 1:
            self.cursor.execute("SELECT * FROM students")
            allstudents = self.cursor.fetchall()

            convertalllstring = lambda x: [str(y) for y in x]

            for i, j in enumerate(allstudents, 1):
                print("{}{}".format(i, " ".join(convertalllstring(j))))

        if by == 2:
            self.cursor.execute("SELECT faculty FROM students")
            faculties = list(enumerate(list(set(self.cursor.fetchall())),1))

            for i,j in faculties:
                print("{}){}".format(i,j[0]))
            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("Must be integer!")
            self.cursor.execute("SELECT * FROM students WHERE faculty='{}'".format((faculties[select-1][1][0])))
            self.cursor.execute("SELECT * FROM students")
            allstudents = self.cursor.fetchall()

            convertalllstring = lambda x: [str(y) for y in x]

            for i, j in enumerate(allstudents, 1):
                print("{}{}".format(i, " ".join(convertalllstring(j))))


        if by == 3:
            self.cursor.execute("SELECT department FROM students")
            departments = list(enumerate(list(set(self.cursor.fetchall())), 1))

            for i, j in departments:
                print("{}){}".format(i, j[0]))
            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("Must be integer!")
            self.cursor.execute("SELECT * FROM students WHERE department='{}'".format((departments[select - 1][1][0])))
            self.cursor.execute("SELECT * FROM students")
            allstudents = self.cursor.fetchall()

            convertalllstring = lambda x: [str(y) for y in x]

            for i, j in enumerate(allstudents, 1):
                print("{}{}".format(i, " ".join(convertalllstring(j))))

        if by == 4:
            self.cursor.execute("SELECT typ FROM students")
            typ = list(enumerate(list(set(self.cursor.fetchall())), 1))

            for i, j in typ:
                print("{}){}".format(i, j[0]))
            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("Must be integer!")
            self.cursor.execute("SELECT * FROM students WHERE typ={}".format((typ[select - 1][1][0])))
            self.cursor.execute("SELECT * FROM students")
            allstudents = self.cursor.fetchall()

            convertalllstring = lambda x: [str(y) for y in x]

            for i, j in enumerate(allstudents, 1):
                print("{}{}".format(i, " ".join(convertalllstring(j))))
        if by == 5:
            self.cursor.execute("SELECT status FROM students")
            status = list(enumerate(list(set(self.cursor.fetchall())), 1))

            for i, j in status:
                print("{}){}".format(i, j[0]))
            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("Must be integer!")
            self.cursor.execute("SELECT * FROM students WHERE status='{}'".format((status[select - 1][1][0])))
            self.cursor.execute("SELECT * FROM students")
            allstudents = self.cursor.fetchall()

            convertalllstring = lambda x: [str(y) for y in x]

            for i, j in enumerate(allstudents, 1):
                print("{}{}".format(i, " ".join(convertalllstring(j))))


    def systemexit(self):
        self.status = False

    def connectdatabase(self):
        self.connect = sqlite3.connect("odtu.db")
        self.cursor = self.connect.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS students(name TEXT,surname TEXT,faculty TEXT,department TEXT,stid TEXT,typ INT, status TEXT)")
        self.connect.commit()




ODTU = University("Orta dogu teknik universitesi","Turkiye")

while ODTU.status:
    ODTU.run()

