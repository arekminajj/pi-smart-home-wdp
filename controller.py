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

    def write(self, light_1, temp_set):
        try:
            status = {'light_1': int(light_1), 'temp_set': temp_set, 'temp': 0}
            with open(self.path, 'w') as json_file:
                json.dump(status, json_file)
        except:
            print(f"ERROR: couldnt update {self.path} file")

    def write_light(self, light1):
        try:
            data = self.read()
            data['light_1'] = int(light1)
            with open(self.path, 'w') as json_file:
                json.dump(data, json_file)
        except:
            print(f"ERROR: couldnt update {self.path} file with lamp data.")

    def write_temp_setting(self, temp_set):
        try:
            data = self.read()
            data['temp_set'] = int(temp_set)
            with open(self.path, 'w') as json_file:
                json.dump(data, json_file)
        except:
            print(f"ERROR: couldnt update {self.path} file with temperature setting data.")

    def write_temp(self, temp):
        try:
            data = self.read()
            data['temp'] = int(temp)
            with open(self.path, 'w') as json_file:
                json.dump(data, json_file)
        except:
            print(f"ERROR: couldnt update {self.path} file with temperature data.")
            