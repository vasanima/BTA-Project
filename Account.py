from FileManager import FileManager
from HistoryMessages import HistoryMessages

class Account:
    def __init__(self, balance = 0):
        self.balance = balance
        self.file_manager = FileManager()
        

    def write_to_history(self, hist_dict):
        self.file_manager.add_to_json(hist_dict, "hist.json")

    def deposit(self, amount):

        try:
            amount = int(amount)
        except ValueError:
            print("Invalid amount for deposit!")
            history_message = HistoryMessages.deposit("failure", amount, self.balance)
            self.write_to_history(history_message)
            return

        if amount > 0:
            self.balance += amount
            history_message = HistoryMessages.deposit("success", amount, self.balance)
            self.write_to_history(history_message)
        else:
            print("Invalid amount for deposit!")
            history_message = HistoryMessages.deposit("failure", amount, self.balance)
            self.write_to_history(history_message)

    def debit(self, amount):

        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount for debit!")
            history_message = HistoryMessages.deposit("failure", amount, self.balance)
            self.write_to_history(history_message)
            return

        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            history_message = HistoryMessages.deposit("success", amount, self.balance)
            self.write_to_history(history_message)
        else:
            history_message = HistoryMessages.deposit("failure", amount, self.balance)
            self.write_to_history(history_message)
            print("Invalid amount for debit!")

    def get_balance(self):
        return self.balance

    def dict_to_string(self, dict):
        if dict["operation_type"] != "exchange":
            return f'type: {dict["operation_type"]} status: {dict["status"]} amount: {dict["amount_of_deposit"]} balance: {dict["total_balance"]}'
        else:
            return f'type: {dict["operation_type"]} status: {dict["status"]} pre exchange amount: {dict["pre_exchange_amount"]} exchange amount: {dict["exchange_amount"]} currency from: {dict["currency_from"]} currency to: {dict["currency_to"]}'
        
    def get_history(self):
        hist_list = self.file_manager.read_json("hist.json")
        return "\n".join([self.dict_to_string(row) for row in hist_list])