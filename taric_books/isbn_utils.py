__author__ = 'Geon'
import json


def get_list_of_books(json_data):
    # decoded = json.loads(json_data.text.encode('latin-1', 'replace').decode())
    decoded = json_data.json()
    books = decoded["data"]
    return books