import mysql.connector

# ---------------------------------
# CONNECTING TO MYSQL DATABASE
# ---------------------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",      # add your MySQL password
    database="bankdb"
)

cursor = db.cursor()

# ---------------------------------
# LOGIN FUNCTION
# ---------------------------------
def login():
    print("=== LOGIN ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",
                   (username, password))
    if cursor.fetchone():
        print("Login Successful!\n")
        return True
    else:
        print("Login Failed! Wrong username or password.\n")
        return False

# ---------------------------------
# CREATE TABLE IF NOT EXISTS
# ---------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    acc_no VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50),
    balance DOUBLE
)
""")

# ---------------------------------
def create_account():
    acc_no = input("Enter new account number: ")

    cursor.execute("SELECT * FROM accounts WHERE acc_no=%s", (acc_no,))
    if cursor.fetchone():
        print("Account already exists!")
        return

    name = input("Enter name: ")
    balance = float(input("Enter starting balance: "))

    cursor.execute("INSERT INTO accounts VALUES (%s, %s, %s)", (acc_no, name, balance))
    db.commit()
    print("Account Created!")

# ---------------------------------
def view_account():
    acc_no = input("Enter account number: ")

    cursor.execute("SELECT * FROM accounts WHERE acc_no=%s", (acc_no,))
    data = cursor.fetchone()

    if data:
        print("Name:", data[1])
        print("Balance:", data[2])
    else:
        print("Account not found!")

# ---------------------------------
def deposit():
    acc_no = input("Enter account number: ")

    cursor.execute("SELECT balance FROM accounts WHERE acc_no=%s", (acc_no,))
    data = cursor.fetchone()

    if not data:
        print("Account not found!")
        return

    amount = float(input("Enter amount to deposit: "))
    new_balance = data[0] + amount

    cursor.execute("UPDATE accounts SET balance=%s WHERE acc_no=%s",
                   (new_balance, acc_no))
    db.commit()
    print("Deposit Successful!")

# ---------------------------------
def withdraw():
    acc_no = input("Enter account number: ")

    cursor.execute("SELECT balance FROM accounts WHERE acc_no=%s", (acc_no,))
    data = cursor.fetchone()

    if not data:
        print("Account not found!")
        return

    amount = float(input("Enter amount to withdraw: "))

    if amount > data[0]:
        print("Not enough balance!")
        return

    new_balance = data[0] - amount
    cursor.execute("UPDATE accounts SET balance=%s WHERE acc_no=%s",
                   (new_balance, acc_no))
    db.commit()
    print("Withdrawal Successful!")

# ---------------------------------
def menu():
    while True:
        print("\n1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            view_account()
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            print("Thanks! Goodbye.")
            break
        else:
            print("Invalid choice!")

# ---------------------------------
# PROGRAM STARTS HERE
# ---------------------------------
if login():     # Login must be correct
    menu()      # Then open bank menu
