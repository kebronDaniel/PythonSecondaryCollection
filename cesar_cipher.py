import string

alphabet = list(string.ascii_lowercase)


def take_inputs():
    text = input("Type your message : \n").lower()
    shift = int(input("Type the shift number : \n"))
    return text, shift


def cesar():
    direction = input(
        "Type 'encode' to encrypt and 'decode' to decrypt : \n").lower()

    if direction != 'encode' or direction != 'decode':
        print("Invalid option, use 'encode' or 'decode' ")
    else:
        text, shift = take_inputs()

        if direction == 'encode':
            new_alphabet_list = alphabet[shift:] + alphabet[:shift]
            encrypted_message = ""
            for letter in text:
                if letter in alphabet:
                    encrypted_message += new_alphabet_list[alphabet.index(
                        letter)]
                else:
                    encrypted_message += letter

            print(encrypted_message)

        if direction == 'decode':
            decrypted_message = ""
            for letter in text:
                if letter in alphabet:
                    index = alphabet.index(letter) - shift
                    decrypted_message += alphabet[index]
                else:
                    decrypted_message += letter

            print(decrypted_message)

    go_or_stop = input(
        "Do you want to go again? type' yes' or 'no' \n").lower()
    if go_or_stop == 'yes':
        cesar()


cesar()
