import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

phn_number = input("Enter the phone number with country code:")

# parsing string to thr phn number
phn = phonenumbers.parse(phn_number)

tz = timezone.time_zones_for_number(phn)
print("Timezone:", str(tz))

location = geocoder.description_for_number(phn,'en')
print("Location:", str(location))

sp = carrier.name_for_number(phn,'en')
print("Service provider:", str(sp))
