import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit must be greater than zero."
        self.balance += amount
        return True, f"Deposited ₹{amount}. New balance: ₹{self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal must be greater than zero."
        if amount > self.balance:
            return False, "Insufficient funds."
        self.balance -= amount
        return True, f"Withdrew ₹{amount}. New balance: ₹{self.balance}"

    def get_balance(self):
        return self.balance


class BankApp:
    def __init__(self, root):
        self.account = None
        self.root = root
        self.root.title("Bank Account Simulator")
        self.root.geometry("400x350")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Bank Account Simulator", font=("Helvetica", 16)).pack(pady=10)

        # Name input
        tk.Label(self.root, text="Enter your name:").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.start_btn = tk.Button(self.root, text="Create Account", command=self.create_account)
        self.start_btn.pack(pady=5)

        # Frame for actions (hidden until account is created)
        self.action_frame = tk.Frame(self.root)
        self.action_frame.pack(pady=10)

        self.amount_entry = tk.Entry(self.action_frame)
        self.amount_entry.pack()

        tk.Button(self.action_frame, text="Deposit", command=self.deposit).pack(pady=2)
        tk.Button(self.action_frame, text="Withdraw", command=self.withdraw).pack(pady=2)
        tk.Button(self.action_frame, text="Check Balance", command=self.check_balance).pack(pady=2)

        self.message_label = tk.Label(self.root, text="", fg="blue")
        self.message_label.pack()

    def create_account(self):
        name = self.name_entry.get()
        if name.strip() == "":
            messagebox.showwarning("Input Error", "Name cannot be empty.")
            return
        self.account = BankAccount(name)
        self.message_label.config(text=f"Account created for {name}")
        self.action_frame.pack()  # Show action buttons

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            success, msg = self.account.deposit(amount)
            self.message_label.config(text=msg, fg="green" if success else "red")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            success, msg = self.account.withdraw(amount)
            self.message_label.config(text=msg, fg="green" if success else "red")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

    def check_balance(self):
        balance = self.account.get_balance()
        self.message_label.config(text=f"Current Balance: ₹{balance}", fg="blue")


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
