class Bank_app:
    bal = 0
    
    database = []
    
    def mainpage(self):
        print("""
            Welcome to S.MFB (Steph's Microfinance Bank)
    
            If you are a new user
            1. Sign Up
    
            If you are returning
            2. Log In
        """)
    
        choice = input("Choice: ")
        if choice == "1":
            self.signup()
        elif choice == "2":
            self.login()
        else:
            print("Invalid option")
            self.mainpage()
    
    def signup(self):
        print ("Welcome...")

        username = input("Username: ").strip()
        if not username:
            print("Username cannot be empty")
        if username in self.database:
            print("That username already exists")
            self.signup()
        else:
            password = input("Enter a password: ").strip()
            email = input("Enter your email: ").strip().lower()
            if "@" not in email:
                print("Invalid email address")
                self.signup()
            
        # signup()
    
    
            user_profile = {
                "username": username,
                "password": password,
                "email": email,
                "bal": 0
            }
    
            # self.database[username] = user_profile
            self.database.append(user_profile)
            print("Account successfully created!")
            self.login()
    
    def login(self):
        print("Welcome back to S.MFB")

        username = input("Username: ").strip()
        # password = input("Password: ").strip()

        # for user in self.database:
        #     if user["username"] == username and user["password"] == password:
        #         self.bal = user["bal"]
        #         print(f"Welcome back, {username}.")
        #         self.home()
        # print("Invalid username or password")
        # self.mainpage()
        if not username:
            print("Username cannot be empty")
        if username in self.database:
            password = input("Enter your password: ").strip()
    
            if password == self.database[username]["password"]:
                print("Login successful!")
                self.home()
            else:
                print("Incorrect password. Please try again.")
                self.login()
        else:
            print("Username not found. Kindly signup")
            self.signup()
            # if password in database:
            #     home()
    
    def home(self):
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
            self.deposit()
        elif choice == "2":
            self.withdraw()
        elif choice == "3":
            self.check_balance()
        elif choice == "4":
            self.mainpage()
        elif choice == "#":
            print("Goodbye...")
            exit()
        else:
            print("Invalid input")
            self.home()   
    
    def deposit(self):
        self.bal
    
        amount = float(input("Amount: "))
        if amount < 1:
            print("Your amount cannot be less than 1")
            self.home()
            
        self.bal += amount

        # for user in self.database:
        #     user["bal"] = self.bal
        #     break


        print(f"Your balance is: {self.bal}")
        self.home()
    
    def withdraw(self):
        self.bal
    
        amount = float(input("Amount: "))
        if amount < 1:
            print("Your amount cannot be less than 1")
        elif amount > self.bal:
            print("Insufficient funds")
        else:
            self.bal -= amount

            # for user in self.database:
            #     user["bal"] = self.bal
            #     break

            print(f"Your balance is: {self.bal}")
    
        self.home()
    
    def check_balance(self):
        print("Your new balance is", self.bal)
        self.home()
    
my_bank = Bank_app()
my_bank.mainpage()
    # mainpage()
