#!/usr/bin/python3

"""
Script that adds all command-line arguments to a Pyth list.
Uses save_to_json_file and load_from_json_file functions.
"""

import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except (FileNotFoundError, json.JSONDecodeError):
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
