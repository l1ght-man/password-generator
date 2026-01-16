import random
import string

pass_length = int(input("how long the password should be? "))
count= int(input("how many password do you want? "))
char_randoms = string.ascii_letters + string.digits + string.punctuation

for j in range (count) :
    password = ""
    for i in range (pass_length):
        password += random.choice(char_randoms)
    print("Generated strong password ",j +1 ,":" ,password)