import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+94765457285")

print("\nPHONE NUMBERS LOCATOR\n")

if(geocoder.description_for_number(phone_number1,"en")!= ""):
    print(geocoder.description_for_number(phone_number1,"en"))
else:
    print("Unavailable Phone Number")
    
