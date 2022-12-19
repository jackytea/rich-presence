from time import sleep
from sys import exit
from os import getpid, _exit
from logging import basicConfig, info, error, INFO
from pypresence import Presence

def rich_presence(client_id, sleep_delay, config_data):
    try:
        basicConfig(level = INFO)

        RPC = Presence(client_id)
        RPC.connect() 
        RPC.update(**config_data)

        info(f'Successfully connected to Discord application client ID -> {client_id}')

        while True:
            sleep(int(sleep_delay))

    except KeyboardInterrupt:
        try:
            RPC.clear(pid=getpid())
            RPC.close()
            exit(0)
        except SystemExit:
            _exit(0)

    except Exception as e:
        error(f'An error has occurred -> {e}')
