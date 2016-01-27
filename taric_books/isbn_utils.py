__author__ = 'Geon'
import json


def parse_json_to_model(json_data):
    decoded = json.loads(json_data.text.encode('latin-1', 'replace').decode())
    books = decoded["data"]
    return books