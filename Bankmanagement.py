import mysql.connector

# -----------------------------
#  CONNECT TO MYSQL DATABASE
# -----------------------------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",        # add your MySQL password
    database="bankdb"   # create DB first with:  CREATE DATABASE bankdb;
)

cursor = mydb.cursor()

# ---------------------------------------
# CREATE TABLE IF NOT EXISTS
# ---------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    acc_no VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50),
    balance DOUBLE
)
""")
mydb.commit()


# ---------------------------------------
def create_account():
    acc_no = input("Enter new account number: ")

    cursor.execute("SELECT * FROM accounts WHERE acc_no = %s", (acc_no,))
    if cursor.fetchone():
        print("⚠️ Account number already exists!\n")
        return

    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))

    cursor.execute("INSERT INTO accounts (acc_no, name, balance) VALUES (%s, %s, %s)",
                   (acc_no, name, balance))
    mydb.commit()

    print("✅ Account created!\n")


# ---------------------------------------
def view_account():
    acc_no = input("Enter account number: ")

    cursor.execute("SELECT name, balance FROM accounts WHERE acc_no = %s", (acc_no,))
    result = cursor.fetchone()

    if result:
        print(f"Name: {result[0]}")
        print(f"Balance: ₹{result[1]}")
    else:
        print("⚠️ Account not found!\n")


# ---------------------------------------
def deposit():
    acc_no = input("Enter account number: ")

    cursor.execute("SELECT balance FROM accounts WHERE acc_no = %s", (acc_no,))
    result = cursor.fetchone()

    if not result:
        print("⚠️ Account not found!\n")
        return

    amount = float(input("Enter amount to deposit: "))
    new_balance = result[0] + amount

    cursor.execute("UPDATE accounts SET balance = %s WHERE acc_no = %s",
                   (new_balance, acc_no))
    mydb.commit()

    print("✅ Deposit successful!\n")


# ---------------------------------------
def withdraw():
    acc_no = input("Enter account number: ")

    cursor.execute("SELECT balance FROM accounts WHERE acc_no = %s", (acc_no,))
    result = cursor.fetchone()

    if not result:
        print("⚠️ Account not found!\n")
        return

    amount = float(input("Enter amount to withdraw: "))
    current_balance = result[0]

    if amount <= current_balance:
        new_balance = current_balance - amount
        cursor.execute("UPDATE accounts SET balance = %s WHERE acc_no = %s",
                       (new_balance, acc_no))
        mydb.commit()
        print("✅ Withdrawal successful!\n")
    else:
        print(f"❌ Withdrawal failed! You only have ₹{current_balance}.\n")


# ---------------------------------------
def menu():
    while True:
        print("\n=== Simple Bank Menu ===")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            view_account()
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice. Try again.")


# Start Program
menu()
