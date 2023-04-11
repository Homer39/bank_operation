from main.class_operations import Operations
import pytest


@pytest.fixture()
def object_operation():
    operation = Operations(**{
        "date_format": "26:08:2019",
        "amount": "31957.58",
        "currency": "руб.",
        "description": "Перевод организации",
        "sender": "Maestro 1596837868705199",
        "address": "Счет 64686473678894779589"
    })
    return operation


def test_date_and_description(object_operation):
    assert object_operation.get_date_and_description() == "26:08:2019 Перевод организации"


def test_get_encode_sender(object_operation):
    assert object_operation.get_encode_sender() == "Maestro 1596 83** **** 5199"


def test_get_encode_destination(object_operation):
    assert object_operation.get_encode_destination() == "Счет **9589"


def test_get_destination(object_operation):
    assert object_operation.get_destination() == "Счет **9589"


def test_from_to_info(object_operation):
    assert object_operation.get_from_to_info() == "Maestro 1596 83** **** 5199 -> Счет **9589"


def test_get_amount(object_operation):
    assert object_operation.get_amount() == "31957.58 руб."
