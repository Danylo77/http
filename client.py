import requests
import json
import sys
from flask import Flask, render_template

test_data = {
    'test_data_first_name': 'Abc',
    'test_data_second_name': 'Zxc'
}

# port = sys.argv[1]
# print(port)
#
# r = requests.post('http://127.0.0.1:' + port, data=json.dumps(test_data))


class Client:
    app = Flask(name)

    @app.route("/", methods = ["GET"])
    def write_message(self):
        return "<h1>HELLO</h1>"

    def init(self, address: str):
        self.address = address
        self.max_node = None
        self.min_node = None
        self.number_of_tries = 100
        self.current_try_number = 0

    def read(self):
        self.__update_stats_()
        return json.loads(requests.get(self.max_node + '/read_message').text)

    def write(self, message):
        self.__update_stats_()
        requests.post(self.min_node + '/write_message', data=json.dumps(message))

    def check(self):
        pass

    def add_node(self, temp_node):
        pass

    def delete_node(self):
        pass

    def __update_stats_(self):
        if self.current_try_number == 0:
            temp = requests.get(self.address + '/get_stats').text
            stats = json.loads(temp)
            self.max_node = max(stats, key=lambda x: stats[x])
            self.min_node = min(stats, key=lambda x: stats[x])

        self.current_try_number = (self.current_try_number + 1) % self.number_of_tries





client_1 = Client("http://127.0.0.1:8011")


client_1.write(test_data)
print(client_1.read())