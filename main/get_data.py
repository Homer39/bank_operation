import json
from datetime import datetime
from class_operations import Operations


def load_data(path='data/operations.json'):
    """
    Открывает файл со списком всех операций
    """
    with open(path, 'r', encoding="utf-8") as f:
        return json.loads(f.read())


def get_last_operations(file_data):
    """
    Создает экземпляры класса из 5 последних операций
    """
    bank_operations = []
    for dict in file_data:
        if dict.get('state') == "EXECUTED":
            bank_operations.append(dict)
    bank_operations = sorted(bank_operations, key=lambda x: datetime.fromisoformat(x['date']))[-5:]
    operation_info = []
    for operation in bank_operations:

        date = operation['date']
        date_object = datetime.fromisoformat(date)
        date_format = date_object.strftime('%d:%m:%Y')

        operation_object = Operations(
            date_format,
            operation.get('description'),
            operation.get('to'),
            operation.get('from'),
            operation.get('operationAmount').get('amount'),
            operation.get('operationAmount').get('currency').get('name'))
        operation_info.append(operation_object)
    return operation_info






