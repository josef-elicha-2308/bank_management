import menu
import client_manager
import client

clientmanager = client_manager.ClientManager()

while True:
    menu.print_menu()
    option_chosen = input('Enter your choice: ')
    if option_chosen == '6':
        break

    function_to_call = menu.FUNCTION_MAPPING.get(option_chosen)
    function_to_call(clientmanager)




