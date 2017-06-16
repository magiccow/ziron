import Ziron

username = ""  # account SID
password = ""  # auth token

ziron = Ziron.Ziron(username,password)
params = {"lookup_type":"hlr"}
params["number"] = ""	# Number to lookup

# Get the account details
print ziron.lookup(params)



