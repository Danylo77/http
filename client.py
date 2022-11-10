import requests
import json
import sys

test_data = {
    'test_data_first_name': 'Abc',
    'test_data_second_name': 'Zxc'
}
print(len(sys.argv))
port = sys.argv[0]

r = requests.post('http://127.0.0.1:' + port, data=json.dumps(test_data))

print(r.json())

class Clien:
    def __init__(self, adress):
        self.adress = adress
        self.max_node = None
        self.min_node = None
        self.number_of_tries = 100
        self.current_try_number = 0

    def read(self):
        self.__update_stats()
        return json.loads(requests.get(self.max_node + '/read_message').tex)

    def write(self):
        self.__update_stats()
        requests.post(self.min_node+'/write_message', data=json.dumps(message))

    def check(self):
        pass

    def add_node(self, temp_node):
        pass

    def delete_node(self):
        pass

    def __update_stats(self):
        if self.current_try_number == 0:
            temp = requests.get(self.adress + '/get_stats').text
            stats = json.loads(temp)
            self.max_node = max(stats, key=lambda x: stats[x])
            self.min_node = min(stats, key=lambda x: stats[x])

        self.current_try_number = (self.current_try_number + 1) % self.number_of_tries

