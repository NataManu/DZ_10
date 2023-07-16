from address_class import AddressBook, Name, Phone, Record

address_book = AddressBook()


def input_error(func):
    def wrapper(*args):
        try:
            result = func(*args)
        except KeyError:
            result = "This name does not exist."
        except ValueError:
            result = "ValueError"            
        except IndexError:
            result = "Give me parameters please."
        return result
    return wrapper


@input_error
def add_command(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec: Record = address_book.get(str(name))
    if rec:
        return rec.add_phone(phone)
    rec = Record(name, phone)
    return address_book.add_record(rec)


@input_error
def change_command(*args):
    name = Name(args[0])
    old_phone = Phone(args[1])
    new_phone = Phone(args[2])
    rec: Record = address_book.get(str(name))
    if rec:
        return rec.change_phone(old_phone, new_phone)
    return f"No contact {name} in address book"


@input_error
def phone_command(*args):
    name = Name(args[0])
    rec: Record = address_book.get(str(name))
    if rec:
        return str(rec)
    return f"No contact {name} in address book"
    

def show_all_command(*args):
    return address_book


def exit_command(*args):
    return "Bye"


def unknown_command(*args):
    return "Invalid command"


def hello_command(*args):
    return "How can I help you?>>>"


COMMANDS = {
            add_command: ("add", "+"),
            change_command: ("change", ),
            phone_command: ("phone", ),
            hello_command: ("hello", ),
            show_all_command: ("show all", ),
            exit_command: ("exit", "close", "bye", "good bye", "stop")
            }

def parser(text:str):
    for cmd, kwds in COMMANDS.items():
        for kwd in kwds:
            if text.lower().startswith(kwd):
                data = text[len(kwd):].strip().split()
                return cmd, data 
    return unknown_command, []


def main():
    print("Hello!")
    
    while True:
        
        user_input = input(">>>")
        
        cmd, data = parser(user_input)
        
        result = cmd(*data)
        
        print(result)
        
        if cmd == exit_command:
            break


if __name__ == "__main__":
    main()

    