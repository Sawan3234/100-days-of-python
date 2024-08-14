import random
import string
def encrypt(message):  
    if(len(message)<=3):
      message=message[::-1]
      return(message)
    else:
     original_message=message
     first_char=original_message[0]
     secret_code=original_message[1:]+first_char
     random_char=''.join(random.choices(string.ascii_letters+string.digits,k=3))
     secret_code=random_char+secret_code
     return(secret_code)
def decryption(code):
    if(len(code)<=3):
        code=code[::-1]
        return code
    else:
        code=code[3:]
        last_letter=code[-1]
        return (last_letter+code[:-1])
        
message=input("enter your message:")
code=encrypt(message)
print(code)
decrypted=decryption(code)
print("the decryption of secret code:",decrypted)

