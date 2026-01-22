import random
import string

def check_chars(x):
    for ch in x :
         if ("A" <= ch <= "Z") or ("a" <= ch <= "z"):
             return True
    return False


def password_generator(output_file):
    min_length = 8
    while True :
        pass_length = int(input(f"how long the password should be? (min {min_length}) "))
        if pass_length >= min_length: break
        user_confirmation = input(f"password is shorter than {min_length}. confirme anyways? (y/n) ").strip().lower()
        if user_confirmation == "y":
            break
        
    count= int(input("how many accounts do you want? "))
    use_symboles = input("do you want to use symboles? (y/n):").strip().lower()

    char_randoms = string.ascii_letters + string.digits 
    if use_symboles == "y":
        char_randoms += string.punctuation
    output_file = "password.txt"

    for j in range (count) :
        while True:
            account= input("which account do u want to assign this password? ")
            if check_chars(account) :
                break
            else:
                print("account name must have at least one lettre . try again")

        password = ""
        for i in range (pass_length):
            password += random.choice(char_randoms)
        print("Generated strong password  ",account,":",password)
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(f"{account} : {password}\n")