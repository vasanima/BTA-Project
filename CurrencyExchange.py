from FileManager import FileManager
from HistoryMessages import HistoryMessages

class CurrencyExchange:
    def __init__(self, balance = 0):
        self.file_manager = FileManager()

    def write_to_history(self, hist_dict):
        self.file_manager.add_to_json(hist_dict, "hist.json")

    def get_exchange_rates(self):
        # server_link = "<link>"
        # response = requests.get(server_link)
        # return json.loads(response.text)

        # TODO: заглушка, пока нет сервера
        tmp = {
            'USD': 1.15,
            'EUR': 1.0,
            'GBP': 0.88,
            'JPY': 129.5,
            'AUD': 1.62,
            'CAD': 1.48,
            'CHF': 1.08,
        }
        return tmp

    
    def exchange_currency(self, currency_from, currency_to, amount):

        rate = self.get_exchange_rates()

        if currency_from not in rate.keys() or currency_to not in rate.keys():
            print("Currency exchange failed!")
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            return 
        
        try:
            amount = float(amount)
        except Exception as e:
            print("Currency exchange failed!")
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            return

        source_rate = rate[currency_from]
        target_rate = rate[currency_to]
        converted_amount = (amount / source_rate) * target_rate

        history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
        self.write_to_history(history_message)
        return converted_amount