import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if not Path(database).exists():
            with open(database, 'w') as fs:
                fs.write('[]')
        with open(database, 'r') as fs:
            data = json.load(fs)
    except Exception as err:
        print(f"An exception occurred: {err}")
        data = []

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        while True:
            alpha = random.choices(string.ascii_uppercase, k=3)
            num = random.choices(string.digits, k=3)
            spchar = random.choices("@#$%", k=1)
            account = alpha + num + spchar
            random.shuffle(account)
            account = "".join(account)
            if not any(i['Account No.'] == account for i in cls.data):
                return account

    @classmethod
    def __find_account(cls, acnumber, pin):
        """Safely look up an account; returns the record or None."""
        try:
            pin_int = int(pin)
        except ValueError:
            return None
        matches = [
            i for i in cls.data
            if i['Account No.'] == acnumber and i['Pin'] == pin_int
        ]
        return matches[0] if matches else None

    def createaccount(self):
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("Invalid age.")
            return

        if age < 18:
            print("Sorry, you must be at least 18 years old.")
            return

        email = input("Enter your email: ").strip()
        pin = input("Enter your PIN (4 or 6 digits): ").strip()

        if len(pin) not in [4, 6] or not pin.isdigit():
            print("Invalid PIN. Must be 4 or 6 digits.")
            return

        info = {
            "Name": name,
            "Age": age,
            "Email": email,
            "Pin": int(pin),
            "Account No.": Bank.__accountgenerate(),
            "Balance": 0
        }

        Bank.data.append(info)
        Bank.__update()

        print("\nAccount created successfully!\n")
        for key, value in info.items():
            print(f"{key}: {value}")
        print("\nPlease save your account number.")

    def depositemoney(self):
        acnumber = input("Enter account number: ").strip()
        pin = input("Enter PIN: ").strip()

        account = Bank.__find_account(acnumber, pin)
        if not account:
            print("No account found.")
            return

        try:
            amount = int(input("Enter amount to deposit: "))
        except ValueError:
            print("Invalid amount.")
            return

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > 10000:
            print("You can deposit a maximum of 10,000 at once.")
            return

        account["Balance"] += amount
        Bank.__update()

        print("Amount deposited successfully.")
        print("Current Balance:", account["Balance"])

    def withdrawmoney(self):
        acnumber = input("Enter account number: ").strip()
        pin = input("Enter PIN: ").strip()

        account = Bank.__find_account(acnumber, pin)
        if not account:
            print("No account found.")
            return

        try:
            amount = int(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid amount.")
            return

        if amount <= 0:
            print("Invalid amount.")
            return

        if account['Balance'] < amount:
            print("Insufficient balance.")
            return

        account["Balance"] -= amount
        Bank.__update()

        print("Amount withdrawn successfully.")
        print("Current Balance:", account["Balance"])

    def transfermoney(self):
        acnumber = input("Enter your account number: ").strip()
        pin = input("Enter your PIN: ").strip()

        sender = Bank.__find_account(acnumber, pin)
        if not sender:
            print("No account found.")
            return

        target_ac = input("Enter recipient's account number: ").strip()
        recipient = next(
            (i for i in Bank.data if i['Account No.'] == target_ac), None
        )
        if not recipient:
            print("Recipient account not found.")
            return

        if sender['Account No.'] == recipient['Account No.']:
            print("Cannot transfer to the same account.")
            return

        try:
            amount = int(input("Enter amount to transfer: "))
        except ValueError:
            print("Invalid amount.")
            return

        if amount <= 0:
            print("Invalid amount.")
            return

        if sender['Balance'] < amount:
            print("Insufficient balance.")
            return

        sender["Balance"] -= amount
        recipient["Balance"] += amount
        Bank.__update()

        print(f"Transferred {amount} to {recipient['Name']} successfully.")
        print("Your current balance:", sender["Balance"])

    def showdetails(self):
        acnumber = input("Enter account number: ").strip()
        pin = input("Enter PIN: ").strip()

        account = Bank.__find_account(acnumber, pin)
        if not account:
            print("No account found.")
            return

        print("\nAccount Details\n")
        for key, value in account.items():
            if key != 'Pin':
                print(f"{key}: {value}")

    def updatedetails(self):
        acnumber = input("Enter account number: ").strip()
        pin = input("Enter PIN: ").strip()

        account = Bank.__find_account(acnumber, pin)
        if not account:
            print("No account found.")
            return

        print("\nYou can update Name, Email, and PIN.\n")

        name = input("Enter new name (press Enter to skip): ").strip()
        email = input("Enter new email (press Enter to skip): ").strip()
        newpin = input("Enter new PIN (press Enter to skip): ").strip()

        if name:
            account['Name'] = name
        if email:
            account['Email'] = email
        if newpin:
            if len(newpin) not in [4, 6] or not newpin.isdigit():
                print("Invalid PIN. Must be 4 or 6 digits.")
                return
            account['Pin'] = int(newpin)

        Bank.__update()
        print("Details updated successfully.")

    def deleteaccount(self):
        acnumber = input("Enter account number: ").strip()
        pin = input("Enter PIN: ").strip()

        account = Bank.__find_account(acnumber, pin)
        if not account:
            print("No account found.")
            return

        check = input("Are you sure? Press Y to delete: ").strip()

        if check.lower() == 'y':
            Bank.data.remove(account)
            Bank.__update()
            print("Account deleted successfully.")
        else:
            print("Deletion cancelled.")


user = Bank()

while True:
    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Show Details")
    print("6. Update Details")
    print("7. Delete Account")
    print("8. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        user.createaccount()
    elif choice == 2:
        user.depositemoney()
    elif choice == 3:
        user.withdrawmoney()
    elif choice == 4:
        user.transfermoney()
    elif choice == 5:
        user.showdetails()
    elif choice == 6:
        user.updatedetails()
    elif choice == 7:
        user.deleteaccount()
    elif choice == 8:
        print("Thank you for using our bank.")
        break
    else:
        print("Invalid choice.")