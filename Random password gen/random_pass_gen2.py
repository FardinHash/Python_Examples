#import library
import secrets
import string

#define the combinations by calling characters from string
alphabets = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

combination = alphabets + numbers + symbols

#fix the length of password
length = 8

#generating the password
password = ''
for i in range(length):
    password += ''.join(secrets.choice(combination))

#here you the password you got!
print(password)
