from ZimPhoneValidate.validate import is_number_valid


number=str(input("Enter a valid Zim number with country code\n:"))

if is_number_valid(number):
	
	print(f"{number} is a valid phone number")
else:
	print(f"{number} is not a valid phone number")
	
