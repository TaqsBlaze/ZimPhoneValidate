import re


def isvalid(number):
		
	'''
	Returns True if number is a valid zim phone number with country code
	 number: 263773738925
	 '''
	if re.search(r'^263(?:\s?)?(\d{3})(?:\s?)?(\d{3})(?:\s?)(\d{3})$', number):
			
		return True
			
	else: 
			
		return False
	
	
	