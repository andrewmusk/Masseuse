import pytz
import datetime
import time
import re
import os
# Download the helper library from https://www.twilio.com/docs/python/install

from twill.commands import *
from twilio.rest import Client

password = os.environ['MASSAGE_LOGIN']

go("https://my.infinitemassage.com/login.php")
fv("1", "email", "amusk@lendingclub.com")
fv("1", "password", password)

submit('0')

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))

today=pst_now.strftime("%m/%d/%y %a")
print(today)
print(today[3])

if today[0] == '0':
	today = today[1:]

if today[2] == '0':
	today = today[0:2] + today[3:]

print(today)

go('https://my.infinitemassage.com/users.php')
booking = follow(today)

account_sid = 'ACd11b200d5d6828371059fa3bb796ae6d'
auth_token = 'b4e8fc875ce5970583f7d9079a6c9296'
client = Client(account_sid, auth_token)


try:
    print find(">Unavailable<")
except Exception as e:
    message = client.messages.create(
                              body='Hello there Andrew!',
                              from_='+17062045589',
                              to='+13109136851'
                          )
try:
    print find(">Available<")
    message = client.messages.create(
                              body='Hello there Andrew!',
                              from_='+17062045589',
                              to='+13109136851')
except Exception as e:
    print("could not find")


