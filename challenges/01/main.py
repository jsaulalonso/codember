#!/usr/bin/env python

import requests

DATA_URL = 'https://codember.dev/data/message_01.txt'

message = requests.get(DATA_URL).text

words_list = [x.lower() for x in message.split()]

output = ""

for word in sorted(set(words_list), key=words_list.index):
    output += word
    output += str(words_list.count(word))

print(output)