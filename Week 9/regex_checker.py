import re
# def username_checker(username):
# 	if re.match(r"([Cc][0-9]{7})", username):
# 		print(username + " is a valid username!")
# 	else:
# 		print(username + " is not a valid username.")
# username_checker("Samwincott")
# username_checker("c1673031")
# username_checker("C1673031")

# def old_username_checker(username):
# 	if re.match(r"([s][c][m][0-9][A-za-z]{2,3})", username):
# 		print(username + " is a valid username!")
# 	else:
# 		print(username + " is not a valid username.")	
# old_username_checker("scm7uii")	
# old_username_checker("scm7UiI")
# old_username_checker("samwincott")

# def sort_code_checker(sortcode):
# 	if re.match(r"([0-9]{2}\-[0-9]{2}\-[0-9]{2})", sortcode):
# 		print(sortcode + " is a valid sortcode!")
# 	else:
# 		print(sortcode + " is not a valid sortcode.")	
# sort_code_checker("09-97-68")	
# sort_code_checker("samwincott")
# sort_code_checker("099768")	

def number_plate_checker(numberplate):
	if re.match(r"([A-Z]{2})[0-9]{2}[A-Z]{3}", numberplate):
		print(numberplate + " is a valid UK car registration number!")
	else:
		print(numberplate + " is not a valid UK car registration number!")
number_plate_checker("BD51SMR")
number_plate_checker("samwincott")
number_plate_checker("bd51smr")
number_plate_checker("BD152SMR")

