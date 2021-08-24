registered_users = [
    {"username": "suyog", "password": "suyogsuyog"},
    {"username": "ojha", "password": "ojhaojha"}
]


while True:
    choice = int(input("""
                   Enter your choice
                   1. For login
                   2. For Regestation
                   3. Exit
                   """))
    print("------------------------------")

    
    if choice == 1:
        # for login
        username = input("enter your name: ")
        pwd = input("Enter your password: ")
        user = dict(username=username, password=pwd)
        if user in registered_users:
            print("Successfully logged in!!!!")
        else:
            print("sorry!!")

    elif choice == 2:
        username = input("give your name: ")
        pwd = input("give your password: ")
        user = dict(username=username, password=pwd)
        if user in registered_users:
            print("Alredy regrestered")
        else:
            registered_users.append(user)
            print("succssfully regestered")
            print(f"users: {registered_users}")
            
    elif choice == 3:
        break
    
    else:
        print("sorry invalid choice")