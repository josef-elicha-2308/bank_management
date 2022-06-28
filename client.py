class Client:
    def __init__(self, name, age, id, city, balance):
        self.name = name
        self.age = age
        self.id = id
        self.city = city
        self.balance = balance

    def add_money(self, money_to_add):
        self.balance += money_to_add

    def remove_money(self, money_to_remove):
        self.balance -= money_to_remove

    def display_client(self):
        print('My name is ' + self.name)
        print('Im ' + self.age + ' years old')
        print('My TZ is ' + self.id)
        print('Im from ' + self.city)
        print('My account balance is ' + self.balance)
