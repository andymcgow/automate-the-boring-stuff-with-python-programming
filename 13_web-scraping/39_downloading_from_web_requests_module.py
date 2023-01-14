import requests

# requests.get() allows your to downlad a file from the internet: -
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

# If you store your requests.get() call inside a variable you can check the status code the server returns when trying to fetch that file: -
res.status_code
# 404 = File not Found
# 200 = Everything OK

# NOTE that the file is not downloaded to your Downloads folder, but a data to this program.

# You can perform operations on the file by as it is stored in a variable, such as: -
print(len(res.text))
print(res.text[334:487])

# The below code will raise an exception if there was an issue with the download: -
# res.raise_for_status()
# bad_res = requests.get("http://automatetheboringstuff.com/abcdef123456")
# bad_res.raise_for_status()

# As well as raising an exception, the above code would crash a program so it doesn't continue.
# If a bad download isn't a dealbreaker for your program you can wrap the raise_for_status() in a try/except statement.

# You can save the downloaded webpage to your computer.
# However, you MUST open the file in write-Binary mode to protect the unicode encoding of even plain text files: -
play_file = open("RomeoAndJuliet.txt", "wb")
for chunk in res.iter_content(100000):
    play_file.write(chunk)
play_file.close()
