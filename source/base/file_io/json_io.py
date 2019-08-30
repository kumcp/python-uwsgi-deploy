import json


def read_data_json(json_file):
    try:
        with open(json_file, 'r', encoding="utf-8") as f:
            data = json.load(f)
    except IOError as identifier:
        raise identifier
    return data
