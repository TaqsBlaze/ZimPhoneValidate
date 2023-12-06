===================================================

package name: ZimPhoneValidate
version: 1.0
Developer: Tanaka Chinengundu
Github: https://github.com/taqsblaze
Whatsapp: +263778040497


ZimPhoneValidate is a module for easily validating
Zimbabwean phone numbers within your python software

##How to install

open your terminal in root directory and run the setup.py file
python setup.py install

##How to use

```
from ZimPhoneValidate.validate import number_is_valid


number=str(input("Enter a valid Zim number with country code\n:"))

if number_is_valid(number):
	
	print(f"{number} is a valid phone number")
else:
	print(f"{number} is not a valid phone number")
	
```

##Supported formats

- 26377804049
- 263 778 040 49
- 263 7780 040 49
- 263 778 04049

```Currently + is not supported``` and your number wont validate
 
