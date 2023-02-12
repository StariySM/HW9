import re
import functools

telephone_book = {}


def parser(user_command):
    user_command_list = user_command.lower().split()
    user_command_search_result = re.search('(hello|add|change|phone|show all|good bye|close|exit)', user_command.lower())
    handler_command = None
    contact = None
    tel_number = None
    if user_command_search_result:
        handler_command = user_command_search_result.group()
        if handler_command in ("phone", "add", "change") and len(user_command_list) > 1:
            contact = user_command_list[1]
        if handler_command in ("add", "change") and len(user_command_list) > 2:
            tel_number = user_command_list[2]

    return handler_command, contact, tel_number


def hello(*args):
    print("How can I help you?")


def add(contact, tel_number):
    if contact == None or tel_number == None:
        raise ValueError("Give me name and phone please after command 'add'")
    telephone_book.update({contact: tel_number})


def change(contact, tel_number):
    if contact == None or tel_number == None:
        raise ValueError("Give me name and phone please after command 'change'")
    elif contact not in telephone_book.keys():
        raise KeyError(f"I can't find {contact} in telephone_book")
    else:
        telephone_book.update({contact: tel_number})


def phone(contact):
    if contact == None:
        raise ValueError("Enter user name please after command 'phone'")
    if contact not in telephone_book.keys():
        raise KeyError(f"I can't find {contact} in telephone_book")
    else:
        print(telephone_book[contact])


def show_all(*args):
    print(telephone_book)


def exit(*args):
    print("Good bye!")
    return True


def exeptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)

    return wrapper


OPERATIONS = {"hello": hello, "add": add, "change": change, "phone": phone, "show all": show_all, "exit": exit,
              "good bye": exit, "close": exit}


@exeptions
def handler(handler_command, contact, tel_number):
    if handler_command == None:
        raise KeyError("Enter correct command")  # handler_command = parser(user_command)[0]
    return OPERATIONS[handler_command](contact, tel_number)


def main():
    while True:
        command = input()
        if handler(*parser(command)):
            break


if __name__ == "__main__":
    main()
