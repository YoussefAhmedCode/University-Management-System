import json
def load_data(filename):
    try:
        with open(filename, 'r') as fh:
            return json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(filename,data):
    with open(filename, 'w') as fh:
        json.dump(data, fh, indent=4)