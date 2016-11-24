class PhoneBookEntry:
    number = ""
    email = ""

class PhoneBook:
    def __init__(self):
        self.data=dict()    

    def addEntry(self,name,number,email):
        self.data[name]=PhoneBookEntry()
        self.data[name].number=number
        self.data[name].email=email

    def delEntry(self,name):
        self.data[name].pop()

    def exist(self,name):
        if name in self.data:
            return True
        else:
            return False

    def printBook(self):
        print("===========================")
        for item in self.data:
            print(item)
            print(self.data[item].number)
            print(self.data[item].email)
            print("===========================")

myPhoneBook=PhoneBook()
myPhoneBook.addEntry("Stuart Allen","02920222222","S.M.Allen@cs.cf.ac.uk")
myPhoneBook.addEntry("Tom Beach","02920111111","T.H.Beach@cs.cf.ac.uk")
myPhoneBook.exist("Stuart Allen")
myPhoneBook.exist("Tom")
myPhoneBook.printBook()