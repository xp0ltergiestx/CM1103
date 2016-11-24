class MyName:
	def printMe(self):
		print("{:s} {:s}".format(self.firstname,self.surname))
	def __repr__(self):
		return '%s %s %s' % (self.firstname, self.middlename, self.surname)
			

me=MyName()
me.firstname="Samuel"
me.middlename="Edward"
me.surname="Wincott"
me.printMe()
print(me)	
