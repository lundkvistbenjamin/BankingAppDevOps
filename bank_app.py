import json
import sys

class BankApp:
    def __init__(self, db_filename='db.json'):
        self.users = self.load_users(db_filename)
        self.current_user = None

    def load_users(self, filename):
        """Load user data from a JSON file."""
        with open(filename, 'r') as file:
            return json.load(file)

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
