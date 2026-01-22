from functions import password_generator
from functions import strength_tester


gen_pass = password_generator.password_generator

def view_saved_accounts(output_file):
    try:
        with open(output_file, 'r',encoding="utf-8") as f:
            lines = f.readlines()

    except FileNotFoundError:
            print("no password file found yet.")
            return
    if not lines:
         print("password file empty")
         return
    print("\nsaved accounts and passwords: ")
    for line in lines:
         print(line.strip())
    print()

OUTPUT_FILE="password.txt"
while True:
     print("=====Password Manager=====")
     print("1) generate new passwords ")
     print("2) view saved accounts")
     print("3) check your password strength score")
     print("4) exit")
     choice = input("choose an option : ").strip()
     if choice == "2":
        view_saved_accounts(OUTPUT_FILE)
     elif choice == "4":
        print("goodbye see ya later !")
        break
     elif choice == "1":
         gen_pass(OUTPUT_FILE)
     elif choice == "3":
         strength_tester.check()
     else:
        print("invalid choice . try again ")   