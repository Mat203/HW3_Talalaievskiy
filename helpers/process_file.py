import json
import os
import re
def process_file(file_path, search_string):
        with open(file_path, 'r') as file:
            text = file.read()
        length_of_text = len(text)
        alphanumeric_count = len(re.findall(r'\w', text))
        occurrences_of_string = text.lower().count(search_string.lower())
        return {
            'length_of_text': length_of_text,
            'alphanumeric_count': alphanumeric_count,
            'occurrences_of_string': occurrences_of_string
        }