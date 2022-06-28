import menu


class ClientManager:
    def __init__(self):
        self.client_list = []

    def add_client(self, client):
        self.client_list.append(client)
