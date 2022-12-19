from json import load
from logging import basicConfig, info, error, INFO

def json_parser(json_file_path):
    try:
        basicConfig(level = INFO)

        with open(json_file_path, 'r') as json_file_contents:
            json_data = load(json_file_contents)

        info(f'Successfully parsed json configuration data from -> {json_file_path}')

        return json_data

    except Exception as e:
        error(f'An error has occurred -> {e}')
