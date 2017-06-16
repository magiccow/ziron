# -*- coding: latin-1 -*-
import Ziron

username = ""  # account SID
password = ""  # auth token

ziron = Ziron.Ziron(username,password)

params = {}

# Set mandatory parameters
params["src"] = ""   # message source - E164 format (e.g. +447700900123) or alphanumeric 
params["dst"] = ""   # message destination - E164 format (e.g. +447700900123)
params["data"] = ""  # message body

# Set optional parameters
params["message_type"] = "sms"  # if missing defaults to SMS
params["callback_url"] = ""     # URL to receive message delivery notifications

# Send the message
ziron.message_send(params)




