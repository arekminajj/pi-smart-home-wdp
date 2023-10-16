import json


class status:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            f = open(self.path, "r")
            data = json.load(f)

            return data
        except:
            print(f"ERROR: couldnt load {self.path} file.")

#tempporary fix want 'temp' to be updated from pi.
    def write(self, light_1, temp_set):
        try:
            status = {'light_1': int(light_1), 'temp_set': temp_set, 'temp': 0}
            with open(self.path, 'w') as json_file:
                json.dump(status, json_file)
        except:
            print(f"ERROR: couldnt update {self.path} file")
