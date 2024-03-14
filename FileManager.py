import json

class FileManager:
    def load_data(self, filename):
        with open(filename, "r") as f:
            return f.read()

    def save_data(self, filename, data):
        with open(filename, "w") as f:
            return f.write(data)

    def read_json(self, json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            return data
        
    def write_json(self, list_of_dicts, json_file_path):
        with open(json_file_path, 'w') as file:
            json.dump(list_of_dicts, file, indent=4)

    def add_to_json(self, data, json_file_path):
        hist = self.read_json(json_file_path)
        hist.append(data)
        self.write_json(hist, json_file_path)
            