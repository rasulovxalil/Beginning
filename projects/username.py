import json
from random import randint

class System():
    def __init__(self):
        self.condition = True
        self.datas = self.getdatas()

    def run(self):
        self.showmenu()
        choice = self.chooicemenu()
        print(choice)

        if choice == 1:
            self.signin()
        if choice == 2:
            self.register()
        if choice == 3:
            self.forgotpassword()
        if choice == 4:
            self.quit()

    def showmenu(self):
        print(""""
1-Sign in
2-Register
3-Forgot password
4-Quit        
        """)
    def chooicemenu(self):
        while True:
            try:
                 choice = int(input("Enter your choice:"))
                 while choice <1 or choice >4:
                     choice = int(input("Please enter the number between 1-4"))
                 break
            except ValueError:
                print("please enter integer!\n")
        return choice
    def getdatas(self):
        try:
            with open("kullanicilar.json",'r') as file:
                datas = json.load(file)
        except FileNotFoundError:
            with open("kullanicilar.json",'w') as file:
                file.write("{}")
            with open("kullanicilar.json",'r') as file:
                datas = json.load(file)
        return datas


    def signin(self):
        uname = input("Enter your username: ")
        password = input("Enter your password: ")
        condition = self.control(uname,password)
        if condition:
            self.entrancesucccesful()
        else:
            self.unsuccesfulentrance('Wrong informations')
    def register(self):
        uname = input('Enter your username: ')
        while True:
            password = input('Enter your password: ')
            rpassword = input('Enter your password: ')
            if password == rpassword:
                break
            else:
                print("Passwords doesn't match try again:")
        email = input("Enter your E-mail: ")

        condition = self.avaliableregister(uname,email)
        if condition:
            print("This username or E-mail have been registered!")
        else:
            activationcode = self.getactivationcode()
            accondition = self.activationcontrol(activationcode)

            if accondition:
                self.booking(uname,password,email)
            else:
                print("invalid activation")
    def forgotpassword(self):
        mail = input("Enter your E-mail: ")
        if self.availablemail(mail):
            with open("activation.txt","w") as file:
                activation = str(randint(1000,9999))
                file.write(activation)
            actget = input('Enter activation code for changing password: ')
            if actget == activation:
                while True:
                    newpassword = input("Enter your new password: ")
                    newpaswordr = input("Enter your new password again: ")

                    if newpassword == newpaswordr:
                        break
                    else:
                        print("Passwords doesn't match")

            self.datas = self.getdatas()
            for user in self.datas["kullanicilar"]:
                if user["mail"] == mail:
                    user["password"] = str(newpassword)
            with open("kullanicilar.json","w") as file:
                json.dump(self.datas,file)
                print("Password succesfully changed")
        else:
            print("This mail doesn't exist")



    def availablemail(self,mail):
        self.datas = self.getdatas()

        for user in self.datas['kullanicilar']:
            if user['mail'] == mail:
                return True

            return False

    def quit(self):
        self.condition = False
    def control(self,uname,password):
        self.datas = self.getdatas()

        self.datas["kullanicilar"]

        for user in self.datas["kullanicilar"]:
            if user['uname'] == uname and user["password"] == password and user['timeout'] == '0' and user["activation"] == "Y":
                return True

        return False


    def unsuccesfulentrance(self,reason):
        print(reason)
    def entrancesucccesful(self):
        print('Welcome...')
        self.condition = False

    def avaliableregister(self,uanme,mail):
        self.datas = self.getdatas()
        try:
            for user in self.datas["kullanicilar"]:
                if user['uname'] == user  and user["mail"] == mail:
                    return True
        except KeyError:
            return False
        return False

    def getactivationcode(self):
        with open('activation.txt','w') as file:
            activation = str(randint(1000,9999))
            file.write(activation)
        return activation
    def activationcontrol(self,activation):
        getactivationcode = input("Enter your activation code: ")
        if activation == getactivationcode:
            return True
        else:
            return False

    def booking(self,uname,password,mail):
        self.datas = self.getdatas()
        try:
            self.datas["kullanicilar"].append([{"uname" : uname, "password":password,"mail":mail,'activation':"Y","timeout" : "0"}])
        except KeyError:
            self.datas["kullanicilar"] = []
            self.datas["kullanicilar"].append({"uname" : uname, "password":password,"mail":mail,'activation':"Y","timeout" : "0"})


        with open("kullanicilar.json","w") as file:
            json.dump(self.datas,file)
            print("Succesfully Registered!")




system = System()

while system.condition:
    system.run()