import random
import ksa

lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '012345678'
symbols = '!@#$%^&*'

combination = lowers + uppers + numbers + symbols
length = 8
password = ''.join(random.sample(combination, length))

print(password)
