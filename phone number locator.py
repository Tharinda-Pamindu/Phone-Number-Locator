import phonenumbers
from phonenumbers import geocoder

#add phone number
phone_number1 = phonenumbers.parse("<ADD PHONE NUMBER HERE>")

print("\nPHONE NUMBERS LOCATOR\n")

if(geocoder.description_for_number(phone_number1,"en")!= ""):
    print(geocoder.description_for_number(phone_number1,"en"))
else:
    print("Unavailable Phone Number")
    
