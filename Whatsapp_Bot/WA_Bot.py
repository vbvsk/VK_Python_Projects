import pywhatkit
from datetime import datetime
now = datetime.now()
chour = now.strftime("%H")
mobile = input("enter mobile number: ")
message = input("enter message u want to send")
hour = int(input("enter hour"))
minute = int(input("enter min"))
pywhatkit.sendwhatmsg(mobile,message,hour,minute)
