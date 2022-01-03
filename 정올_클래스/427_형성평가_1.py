class Information:
    name = ""
    number = ""
    address = ""

    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address


name, number, address = input().split()
person = Information(name, number, address)
print("name :", person.name)
print("tel :", person.number)
print("addr :", person.address)
