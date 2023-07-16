from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other):
        return self.value == other.value 
        

class Name(Field):
    ...
    

class Phone(Field):
    ...


class Record:
    def __init__(self, name: Name, phone: Phone = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
    
    def add_phone(self, phone: Phone):
        if phone in self.phones:
            return f"Phone {phone} alredy exists at contact {self.name}"
        else:
            self.phones.append(phone)
            return f"Phone {phone} added to contact {self.name}"    


    def change_phone(self, old_phone:Phone, new_phone:Phone):
        if old_phone in self.phones:
            self.phones[self.phones.index(old_phone)] = new_phone
            return f"{self.name}: phone {old_phone} change to {new_phone}"
        return f"Phone {old_phone} does not exist at contact {self.name}"

    
    def __str__(self) -> str:
        return f"{self.name}: {', '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        return f"Contact {record} added success"

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())