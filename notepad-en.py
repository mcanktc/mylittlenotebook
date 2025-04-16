user_ids= {

}

user_list = [
]


user_notes= {

}

user_log = [

]

def main():
    print("Welcome to the menu. \n 1. Sign Up \n 2. Log In")
    try:
        main_menu = input()
        if int(main_menu) == 1:
            sign_up()
        elif int(main_menu) == 2:
            log_in()
        else:
            print("Please select a valid number from the menu.")
            main()
    except ValueError:
        print("Please enter numbers only.")
        return main()

def sign_up():
    user_name = input("Enter your username: ")
    if user_name in user_list:
        print(f"The username '{user_name}' is already registered in our system.")
        print("Press any key to continue.")
        input()
        main()
    else:
        user_list.append(user_name)
        print(f"Your username has been successfully set as {user_name}.")
    password = input("Please enter your password: ")
    print("Your password has been successfully set.")
    user_id = len(user_name) * 2 + len(password)
    user_ids[user_id] = { "Username" : user_name, "Password" : password, "ID" : user_id }
    print(f"You have successfully signed up. Your membership ID is: {user_id}.")
    print("Press any key to return to the menu.")
    input()
    main()

def log_in():
    user_name = input("Kullanıcı adı:")
    password = input("Şifre:")
    user_id = len(user_name) * 2 + len(password)
    if user_id in user_ids:
            user_log.append(user_id)
            user_page()
    else:
            print("Incorrect username or password.")
            print("Press any key to return to the menu.")
            input()
            main()

def user_page():
    user_id = user_log[-1]
    user_main(user_id)
        
def user_main(user_id):
    print("Welcome to your notes. \n 1. My Profile \n 2. My Notes \n 3. Log Out")
    user_page_menu = input()
    try:
        if int(user_page_menu) == 1:
            user_profile(user_id)
        elif int(user_page_menu) == 2:
            user_note_main(user_id)
        elif int(user_page_menu) == 3:
            main()
        else:
            print("Please select a valid number from the menu.")
            user_page()
    except ValueError:
        return user_page()
    
def user_profile(user_id):
    user_name = user_ids[user_id]["Username"]
    password = user_ids[user_id]["Password"]
    id = user_ids[user_id]["ID"]
    print("Welcome to your profile!")
    print(f"Username: {user_name}")
    print(f"Password: {password}")
    print(f"User ID:: {id}")
    print("Press any key to return to the user menu.")
    input()
    user_main(user_id)

def user_note_main(user_id):
    if user_id in user_notes:
        print(user_notes[user_id])
        print("1. Edit \n 2. Exit")
        
        try:
            user_note_menu = input()
            if int(user_note_menu) == 1:
                user_text = input("Please enter your new note: ")
                user_notes[user_id] = user_text
                print ("Your note has been successfully updated.")
                print("Press any key to return to your notes.")
                input()
                user_note_main(user_id)
            elif int(user_note_menu) == 2:
                user_main(user_id)
            else:
                print("Please select a valid number from the menu.")
                user_note_main(user_id)
        except ValueError:
            return user_note_main(user_id)
    else:
        print("Your first note page has been created successfully.")
        user_first_text = input("Please enter your first note: ")
        user_notes[user_id] = user_first_text
        print(f"Your note: '{user_first_text}' has been saved.")
        print("Press any key to return to your notes.")
        input()
        user_note_main(user_id)

main()