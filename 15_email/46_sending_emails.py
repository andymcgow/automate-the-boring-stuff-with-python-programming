import smtplib

# Creating a connection object: -
conn = smtplib.SMTP("smtp.gmail.com", 587)

# Starting the connection to the SMTP server
conn.ehlo()

# Starting the TLS encyption: -
# NOTE most modern email servers will require you to start encryption BEFORE logging in.
conn.starttls()

# Logging in: -
# NOTE for Gmail accounts you will now need to create an APP PASSWORD to enable you to log in ! https://myaccount.google.com/apppasswords
# (Logging in to an application like this with your main account password has been prohibited by Google.)
conn.login("your.address@gmail.com", "PASSWORD")

# Sending an email: -
# ("FROM", "TO", "Subject: SUBJECT HERE \n\nMESSAGE HERE")
conn.sendmail("your.address@gmail.com", "recipient.addressw@gmail.com", "Subject: This is the subject \n\nThis is the message.")

# Close connection: -
conn.quit()
