#!/usr/bin/env python3

from decode_message import decode_message

import requests

DATA_URL = 'https://codember.dev/data/message_02.txt'

if __name__ == '__main__':
    message = requests.get(DATA_URL).text

    print(decode_message(message))