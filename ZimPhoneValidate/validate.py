import re


def is_number_valid(number):
		
	'''
	Returns True if number is a valid zim phone number with country code
	 number: 263773738925
	 '''
	if re.search(r'^263(?:\s?)?(\d{3})(?:\s?)?(\d{3})(?:\s?)(\d{3})$', number):
			
		return True
			
	else: 
			
		return False
	
 	
	
class example:

	def show():

		eg='''
		from ZimPhoneValidate.validate import is_number_valid
		
		number = "263778040497"

		if is_number_valid(number):
			print("Number is Valid")
		else:
			print("Not a valid number")

		'''

		print(eg)
