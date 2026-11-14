bal = 0

database = {}

def mainpage():
    print("""
        Welcome to S.MFB (Steph's Microfinance Bank)

        If you are a new user
        1. Sign Up

        If you are returning
        2. Log In
    """)

    choice = input("Choice: ")
    if choice == "1":
        signup()
    elif choice == "2":
        login()
    else:
        print("Invalid option")
        mainpage()

def signup():
    print ("Welcome...")
    username = input("Username: ").strip()
    if not username:
        print("Username cannot be empty")
    if username in database:
        print("That username already exists")
        signup()
    else:
        password = input("Enter a password: ").strip()
        email = input("Enter your email: ").strip().lower()
        if "@" not in email:
            print("Invalid email address")
            signup()
        
    # signup()


        user_profile = {
            "username": username,
            "password": password,
            "email": email
        }

        database[username] = user_profile
        # add_database = database.append(user_profile)
        print("Account successfully created!")
        login()

def login():
    print("Welcome back to S.MFB")
    username = input("Username: ").strip()
    if not username:
        print("Username cannot be empty")
    if username in database:
        password = input("Enter your password: ").strip()

        if password == database[username]["password"]:
            print("Login successful!")
            home()
        else:
            print("Incorrect password. Please try again.")
            login()
    else:
        print("Username not found. Kindly signup")
        signup()
        # if password in database:
        #     home()

def home():
    print("""
    Welcome to my bank

    1. Deposit
    2. Withdraw
    3. Check Balance
    4. Back to Mainpage
    #. Exit
    """)

    choice = input("Choice: ")
    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        check_balance()
    elif choice == "4":
        mainpage()
    elif choice == "#":
        print("Goodbye...")
        exit()
    else:
        print("Invalid input")
        home()   

def deposit():
    global bal

    amount = float(input("Amount: "))
    if amount < 1:
        print("Your amount cannot be less than 1")
        home()
        
    bal += amount
    print(f"Your balance is: {bal}")
    home()

def withdraw():
    global bal

    amount = float(input("Amount: "))
    if amount < 1:
        print("Your amount cannot be less than 1")
    elif amount > bal:
        print("Insufficient funds")
    else:
        bal -= amount
        print(f"Your balance is: {bal}")

    home()

def check_balance():
    print("Your new balance is", bal)
    home()


mainpage()