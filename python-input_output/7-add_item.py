#!/usr/bin/python3
import sys
import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except (FileNotFoundError, json.JSONDecodeError):
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
