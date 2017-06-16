import Ziron

username = ""  # account SID
password = ""  # auth token

# Get the account details
ziron = Ziron.Ziron(username,password)
print ziron.account_retrieve()



