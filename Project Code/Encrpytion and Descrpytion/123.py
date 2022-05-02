from cryptography.fernet import Fernet

def password_encrypt(p):
	fernet = Fernet(Fernet.generate_key())
	encMessage = fernet.encrypt(p.encode())
	#print("original string: ",p)
	print("encrypted string: ", encMessage)
	decMessage = fernet.decrypt(encMessage).decode()
	print("decrypted string: ", decMessage)
	return fernet.encrypt(p.encode())
a=input("Enter a name:")
abc=password_encrypt(a)
print(abc)