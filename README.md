===================================================

package name: ZimPhoneValidate
version: 1.0
Developer: Tanaka Chinengundu
Github: https://github.com/taqsblaze
Whatsapp: +263778040497


ZimPhoneValidate is a module for easily validating
Zimbabwean phone numbers within your python software

#How to install

open your terminal in root directory and run the setup.py file
python setup.py install

#How to use

```
from ZimPhoneValidate.validate import isvalid


number=str(input("Enter a valid Zim number with country code\n:"))

if isvalid(number221:
	
	print(f"{number} is a valid phone number")
else:
	print(f"{number} is not a valid phone number")
	
```