def decode_message(message):
    output = ''
    count = 0
    for symbol in message:
        if symbol == '#':
            count += 1
        elif symbol == '@':
            count -= 1
        elif symbol == '*':
            count *= count
        elif symbol == '&':
            output += str(count)
    return output