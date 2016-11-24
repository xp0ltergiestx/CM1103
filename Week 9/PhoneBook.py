#Define the empty class PhoneBookEntry here
class PhoneBookEntry:
	pass

class PhoneBook:
	def __init__(self):
		self.data=dict()	
	
	def addEntry(self,name,number,email):
		self.data[name]=PhoneBookEntry()
		self.data[number]=number
		self.data[email]=email

	def delEntry(self,name):
		#Write code here to delete the appropriate entry from the self.data dictionary
		self.data.pop(name)
	
	def exist(self, name) :
		if name in self.data:
			return True
		else:
			return False	

	def printBook(self):
		for name, number, email in self.data.items():
			print(self.name, self.number, self.email)

myPhoneBook=PhoneBook()
myPhoneBook.addEntry("Stuart Allen","02920222222","S.M.Allen@cs.cf.ac.uk")
myPhoneBook.addEntry("Tom Beach","02920111111","T.H.Beach@cs.cf.ac.uk")
myPhoneBook.exist("Stuart Allen")
myPhoneBook.exist("Tom")
myPhoneBook.printBook()