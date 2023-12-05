from ZimPhoneValidate.validate import isvalid


number=str(input("Enter a valid Zim number with country code\n:"))

if isvalid(number221:
	
	print(f"{number} is a valid phone number")
else:
	print(f"{number} is not a valid phone number")
	