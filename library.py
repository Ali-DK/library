import os
import winsound
 
def login():
    os.system('cls')
    print("--------Welcome to Aarhus library --------")
    cnt = 0
    while True: 
        cnt = cnt + 1
        os.system('color 80')
        password = input("Enter the password: ")
        if password == "data": 
            os.system('cls')            
            print("--------Welcome to Aarhus library --------")
            break
        winsound.Beep(1000, 500)
        print("The password is not correct!")
        if cnt == 3:
            print("Too many wrong attempts! Program terminated!")
            return -1
    return
def help():
    os.system('cls')
    print("________________Help________________")
    print("1. Register: To register a new user you need name and address.\n2. Edit: You can edit a user's name and address\n3. Delete all: You can delete all users\n4. Show all: Show all users\n5. Exit: Exit the program")
    print("____________________________________")
    input("Press enter to return to the main menu...")
    os.system('cls')
    return
def register():
    os.system('cls')
    f = open("library_users.txt", "a")
    print("________User Registration__________")
    name = input("Enter name: ")
    address = input("Enter address: ")
    f.write(name + "," + address + "\n")
    f.close()
    print("The user is successfully registered!")
    print("___________________________________")
    return
def edit():
    f = open("library_users.txt")
    name = input("Enter name of the user to edit: ")
    user_choice = input("What do you want to edit?\n1. name\n2. address\nEnter the number: ")
    if user_choice == "1" :
        new_name = input("Enter new name: ")
    if user_choice == "2":
        new_address = input("Enter new address: ")
    original_text = f.readlines()
    edited_text = []
    for line in original_text:
        parts = line.split(',')
        if parts[0] == name and user_choice == "1":
            line = f"{new_name},{parts[1]}\n"
        if parts[0] == name and user_choice == "2":
            line = f"{parts[0]},{new_address}\n"
        edited_text.append(line)
    print("The user's info is successfully updated!")
    f = open("library_users.txt", "w")
    f.writelines(edited_text)
    f.close()
    return
def delete():
    os.system('cls')
    print("__________Delete all users_________")
    answer = input("Are you sure you want to delete all users? (y/n): ")
    if answer == "y" and os.path.exists("library_users.txt"):
        os.remove("library_users.txt")
        print("All users deleted!")
    else:
        print("The file does not exist.")
    return
def show_all():
    os.system('cls')
    print("__________List of all users_________")
    f = open("library_users.txt")
    print(f.read())
    print("____________________________________")
    return

if login() != -1: 
    f = open("library_users.txt")
    while True:
        os.system('color 07')
        print("______________Main Menu_____________")
        print("0. Help\n1. Register\n2. Edit\n3. Delete all \n4. Show all \n5. Exit")
        print("____________________________________")
        menu_option = input("Please choose a number from the menu: ")
        if menu_option == "0":
            help()
        if menu_option == "1":
            register()
        if menu_option == "2":
            edit()
        if menu_option == "3": 
            delete()
        if menu_option == "4": 
            show_all()
        if menu_option == "5": 
            print("Bye!")
            break