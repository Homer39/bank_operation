class Operations:
    def __init__(self, date_format, description, address, sender, amount, currency):
        self.date_format = date_format
        self.description = description
        self.address = address
        self.sender = sender
        self.amount = amount
        self.currency = currency

    def get_date_and_description(self):
        """Возвращает время и описание операции
        """
        return f'{self.date_format} {self.description}'

    def get_encode_sender(self):
        """Кодирует счет отправителя
        """
        sender = self.sender
        if "Счет" in sender:
            sender = sender.split()
            privat_number = sender[0] + ' **' + sender[-1][-4:]
        else:
            sender = sender.split()
            block = []
            for i in range(0, 16, 4):
                block.append(sender[-1][i:i + 4])
            number = sender[0:-1] + block
            privat_number = ' '.join(number)
            privat_number = privat_number.replace(privat_number[-12:-5], '** ****')
        return f'{privat_number}'

    def get_encode_destination(self):
        """Кодирует счет получателя
        """
        destination = self.address
        destination = destination.split()
        destination = destination[0] + ' **' + destination[-1][-4:]
        return ''.join(destination)

    def get_destination(self):
        """Возвращает счет получателя
        """
        return self.get_encode_destination()

    def get_from_to_info(self):
        """Возвращает данные о движении стредств
        """
        if not self.sender:
            return self.get_encode_destination()
        return f'{self.get_encode_sender()} -> {self.get_encode_destination()}'

    def get_amount(self):
        """Возвращает сумму и валюту"""
        return f'{self.amount} {self.currency}'

    def print_operation(self):
        """Вывожу информацию об операции"""
        return f'''{self.get_date_and_description()}
{self.get_from_to_info()}
{self.get_amount()}\n'''

    def __repr__(self):
        return f'''('Дата операции - {self.date_format}, Операция - {self.description}, Адрес - {self.address},
Отправитель - {self.sender}, Сумма {self.amount}, Валюта {self.currency}')'''
