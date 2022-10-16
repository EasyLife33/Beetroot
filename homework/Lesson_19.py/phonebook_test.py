import pytest
import json
from Lesson_26 import app_run, add_new, delete, update, search_by_first_name

@pytest.fixture
def contacts():
    phonebook = 'contactstest.json'
    data = {'contacts': [{'first name': 'Yura', 'last name': 'Hradiuk',
                         'phone number': '067979797', 'city': 'Lviv'}]} 
    with open(phonebook, 'w') as file:
        json.dump(data, file)
    yield phonebook  
    with open(phonebook, 'w') as file:
        json.dump(data, file)
    
def test_add_new(monkeypatch, contacts):

    def patched_input(prompt=''):
        yield "a"
        yield "Mark"
        yield "Zuckerberg"
        yield "0971234567"
        yield "Chernivtsi"
        yield "e"
    generator = patched_input()
    monkeypatch.setattr('builtins.input', lambda _: next(generator))

    app_run('contacts')


def test_search_by_first_name(monkeypatch):
    def patched_input(prompt=''):
        yield "s"
        yield "oleg"
        yield "e"
    generator = patched_input()
    monkeypatch.setattr('builtins.input', lambda _: next(generator))

    app_run('contacts.json')


# make tests isolated
# make a fixture that creates 'contacts.json' and cleans it after the test
