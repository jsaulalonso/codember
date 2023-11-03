def decode_message(message):
    words_list = [x.lower() for x in message.split()]
    return ''.join([word + str(words_list.count(word)) for word in sorted(set(words_list), key=words_list.index)])
