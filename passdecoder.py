#password encryption!
import base64

def decrypter(decryptionz):

    stringer = base64.b64decode(decryptionz)

    print(stringer)

encrypted_string = input("Paste your string here... ")

decrypter(encrypted_string)
