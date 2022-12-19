from os import getenv
from dotenv import load_dotenv
from utils.json_parser import json_parser
from utils.rich_presence import rich_presence

load_dotenv()

CLIENT_ID = getenv('CLIENT_ID')
JSON_FILE_PATH = getenv('JSON_FILE_PATH')
SLEEP_DELAY_MS = getenv('SLEEP_DELAY_MS')

if __name__ == "__main__":
    config_data = json_parser(JSON_FILE_PATH)
    
    if config_data:
        rich_presence(CLIENT_ID, SLEEP_DELAY_MS, config_data)
