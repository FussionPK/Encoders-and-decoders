#password encryption!
import base64

def encrypter(password):

    password_bytes = password.encode('utf-8')

    encoded_password = base64.b64encode(password_bytes)

    print(encoded_password)

user_password = input("Enter your password: ")

encrypter(user_password)
