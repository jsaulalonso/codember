#!/usr/bin/env python

import requests

DATA_URL = 'https://codember.dev/data/message_01.txt'

message = requests.get(DATA_URL).text

words_list = [x.lower() for x in message.split()]

print(''.join([word + str(words_list.count(word)) for word in sorted(set(words_list), key=words_list.index)]))
