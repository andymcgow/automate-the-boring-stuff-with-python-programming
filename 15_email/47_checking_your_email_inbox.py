import imapclient
import pyzmail

# Creating a connection object: -
conn = imapclient.IMAPCLient("imap.gmail.com", ssl=True)

# Logging in: -
conn.login("email@gmail.com", "PASSWORD")

# Display a list of the folders in the account: -
conn.list(folders())

# Selecting a folder (normally INBOX), making sure to access as READ ONLY: -
conn.select_folder("INBOX", readonly=True)

# Performing a search: -
# (Returns a list of UIDs of the emails that fit the search criteria)
UIDs = conn.search(["SINCE 20-Aug-2015"])
UIDs = conn.search(["ON 24-Aug-2015"])

# Fetching a specfic email from that list: -
raw_message = conn.fetch([UID], ["BODY[]", "FLAGS"])

# NOTE the raw_message from imapclient will return a string with ALL the message, including all kinds of extra data.
# This is very hard to read so we will pass raw_message over to pyzmail as that can allow us to access the data in a more useful way for programming: -
message = pyzmail.PyzMessage.factory(raw_message[UID][b"BODY[]"])

# We can now perform simple operations on the message, such as: -
message.get_subject()
message.get_addresses("from")
message.get_addresses("to")
message.get_addresses("bcc")

# However to get the actual message body, as emails can be sent as plain text or HTML we need to do some further checking: -
message.text_part # This code will return some data if there is a message. Will return None if there is no message.
message.html_part # This code will return some data if the message is HTML. Will return None if not in HTML.

# If confirmed to be just text, you can use the following code to return a string with the message inside: -
message.text_part.get_payload().decode("UTF-8")

# To DELETE emails you would need to ensure you are not in READ ONLY mode for that folder: -
conn.select_folder("INBOX", readonly=False)
# Then to delete a message(s) you would need to pass on or multiple UIDs, or a variable contianing UIDs (as above) to .delete_messages() : -
conn.delete_messages([UID])

# Close the connection: -
conn.logout()
