from password_generator import password_generator



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
     print("3) exit")
     choice = input("choose an option : ").strip()
     if choice == "2":
        view_saved_accounts(OUTPUT_FILE)
     elif choice == "3":
        print("goodbye see ya later !")
        break
     elif choice == "1":
         password_generator(OUTPUT_FILE)
     else:
        print("invalid choice . try again ")   