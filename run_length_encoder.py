# This script encodes a series of bytes/characters using the Run-Length algorithm -- Albert Gubau -- NIA: 229416

def encode(input_msg):

    encoded_msg = ""  # Initialize an empty encoded message

    i = 0
    while i <= len(input_msg) - 1:
        count = 1
        ch = input_msg[i]    # Get the actual character
        j = i

        while j < len(input_msg) - 1:
            if input_msg[j] == input_msg[j + 1]:   # Count the number of character repetitions
                count += 1
                j += 1
            else:
                break

        encoded_msg += str(count) + ch  # Fill the encoded message with the character and the number of appearances
        i = j + 1

    return encoded_msg


# Test of the program
input_message = str(input("Introduce the message to be encoded as a series of characters (e.g: AAABBCC): "))
encoded_message = encode(input_message)
print("The Run-Length encoded message looks like this: ", encoded_message)
