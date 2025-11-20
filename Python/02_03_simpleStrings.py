message_name = "athemax rayton"
message_break = " "
print(message_name.title())

message_details = "- Note: [variableName].title() is a method (i.e. an action Python can perform on a piece of data)"
print(message_details)
print (message_break)
print(message_name.upper())
print(message_name.lower())
print (message_break)

message_details = "- Note: [variableName].upper() or [variableName].lower() is also a method (i.e. an action Python can perform on a piece of data)"
print(message_details)

message_details = "- Note: Converting to .lower() is useful before converting user.data further"
print(message_details)
print (message_break)

message_fstring_opener = "Let's discuss f-strings & the difference in use:"
print(message_fstring_opener)

firstName = "athemax"
lastName = "rayton"
full_name = f"{firstName} {lastName}!"
full_name_details = "There is an f outside of the string that allows variables to be interposed within the string."

print(full_name)
print (message_break)
print(full_name_details)
print (message_break)

full_name_Message = f"Hello, {full_name.title()}!"
full_name_MessageDetails = "We can even call a method like .title() or .upper or .lower"
print (message_break)
print(full_name_Message)
print (message_break)
print(full_name_MessageDetails)
print(message_break)
print(message_break)
