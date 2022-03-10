'''
ROBLOX username and password generator
Created by cOpEtriNe
thanks to ayushi7rawat for the original code.
'''

#import the necessary modules!
import random
import string

print('Welcome to the ROBLOX username and password generator! ')
print('Liked this project? support the original Coder here: https://bit.ly/34vVQv0 And my github here: https://bit.ly/3tNllR9')

length = int(input('\nEnter the length of Username (Max 20): '))

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
#string.ascii_letters

#combine the data
all = lower + upper + num

#use random
temp = random.sample(all,length)

#create the password
Username = "".join(temp)

#print the password
print(Username)

print('\nTime to create the password.')

#input the length of password
length = int(input('\nEnter the length of password: '))                      

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#string.ascii_letters

#combine the data
all = lower + upper + num + symbols

#use random 
temp = random.sample(all,length)

#create the password 
password = "".join(temp)

#print the password
print(password)

print('\nAccount Username & Password Generated')
print('Sadly, you have to manually enter this into the ROBLOX account creation page.')
print('If you want to get to the site faster, click here: https://www.roblox.com/   Just make sure you have signed out or use a different browser')

