# This script encodes a series of bytes/characters given

def encode(message):
    encoded_message = ""
    i = 0
    while i <= len(message) - 1:
        count = 1
        ch = message[i]
        j = i
        while j < len(message) - 1:
            if message[j] == message[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        encoded_message = encoded_message + str(count) + ch
        i = j + 1
    return encoded_message


# Provide different values for message and test your program
input_message = str(input("Introduce the message to be encoded as a series of characters (e.g AAABBCC): "))
encoded_message = encode(input_message)
print(encoded_message)
