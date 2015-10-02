# secret decoder

# save a message to a file

#encrypt the message to a separate file

# option to decrypt a file

def main():
	message  = raw_input("Enter your message: ")
	plain_message = open("plain message.txt", "w")
	plain_message.write(message)
	plain_message.close()
	
	
	
	
main()