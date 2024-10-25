import sys

class BankApp:
    def __init__(self):
        # Hard-coded users with usernames, passwords, account numbers, and balances
        self.users = {
            'user1': {'password': 'pass1', 'account_number': '111111', 'balance': 1000},
            'user2': {'password': 'pass2', 'account_number': '222222', 'balance': 2000},
            'user3': {'password': 'pass3', 'account_number': '333333', 'balance': 3000}
        }
        self.current_user = None

    def login(self, username, password):
        """Login to the account if the credentials match."""
        user = self.users.get(username)
        if user and user['password'] == password:
            self.current_user = username
            return True
        return False

    def get_balance(self):
        """Return the balance of the current logged-in user."""
        if self.current_user:
            return self.users[self.current_user]['balance']
        raise Exception("No user logged in.")

    def get_account_number(self):
        """Return the account number of the current logged-in user."""
        if self.current_user:
            return self.users[self.current_user]['account_number']
        raise Exception("No user logged in.")

    def logout(self):
        """Logs the current user out."""
        self.current_user = None

# Interactive code to test login and access
if __name__ == "__main__":
    app = BankApp()
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if app.login(username, password):
            print("Login successful!")
            while True:
                print("\n1. Account Balance\n2. Account Number\n3. Exit")
                choice = input("Choose an option: ")

                if choice == "1":
                    print("Balance:", app.get_balance())
                elif choice == "2":
                    print("Account Number:", app.get_account_number())
                elif choice == "3":
                    app.logout()
                    print("Logged out. Exiting program.")
                    sys.exit()  # Terminate the program
                else:
                    print("Invalid option, please choose again.")
        else:
            print("Invalid username or password.")
