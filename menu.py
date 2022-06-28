import client
import client_manager


def print_menu():
    print("------------------WELCOME TO JOSEF'S BANK------------------")
    print('\t 1. New client')
    print('\t 2. View client infos')
    print('\t 3. Edit client infos')
    print('\t 4. Make transaction')
    print('\t 5. Delete client')
    print('\t 6. EXIT')


def new_client(clientmanager):
    client1 = client.Client(name=input("Enter name :"), age=input("Enter age: "), city=input("Enter city:"),
                            id=input("Enter id:"), balance=input("Enter balance"))
    clientmanager.add_client(client1)
    print('Added Client successfully\n\n')


def view_client(clientmanager):
    tz = input('Met la teoudat zehout: ')
    for c in clientmanager.client_list:
        if tz == c.id:
            c.display_client()
            return


def edit_client(clientmanager):
    tz = input('Met la teoudat zehout: ')
    for c in clientmanager.client_list:
        if tz == c.id:
            while True:
                print('\t 1. Change le nom')
                print('\t 2. change lage')
                print('\t 3. change la ville')
                print('\t 4. change le id')
                print('\t 5. change la balance')
                print('\t 6. EXIT')
                choix = input('Choisis ce que tu veu changer : ')
                if choix == "1":
                    c.name = input('Met le nouveau nom: ')
                elif choix == "2":
                    c.age = input('Met le nouvel age: ')
                elif choix == "3":
                    c.city = input('Met la nouvelle ville: ')
                elif choix == "4":
                    c.id = input('Met le noubel id: ')
                elif choix == "5":
                    c.balance = input('Met la nouvelle balance: ')
                elif choix == '6':
                    break
                else:
                    print('Pas compris')


def make_transaction(clientmanager):
    somme = int(input("Met la somme : "))
    destination_id = input('Met la teoudat zehout du gars a qui tu envoyer : ')
    source = input('Met la tz de la source : ')

    for c in clientmanager.client_list:
        if destination_id == c.id:
            c.add_money(somme)

    for c in clientmanager.client_list:
        if source == c.id:
            c.remove_money(somme)


def delete_client(clientmanager):
    tz = input('Met la teoudat zehout: ')
    for c in clientmanager.client_list:
        if tz == c.id:
            clientmanager.client_list.remove(c)


FUNCTION_MAPPING = {
    '1': new_client,
    '2': view_client,
    '3': edit_client,
    '4': make_transaction,
    '5': delete_client
}
