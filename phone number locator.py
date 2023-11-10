import phonenumbers
from phonenumbers import geocoder

print("\nPHONE NUMBERS LOCATOR\n")


while (True):
    #add phone number
    number = str(input("\nEnter Phone Number(eg:+94xxxxxxxxx):- "))
    phone_number1 = phonenumbers.parse(number)
    try:
        print(geocoder.description_for_number(phone_number1,"en"))
    except:
        continue
    # if(geocoder.description_for_number(phone_number1,"en")!= ""):
    #     print(geocoder.description_for_number(phone_number1,"en"))
    # else:
    #     print("Unavailable Phone Number")
    
