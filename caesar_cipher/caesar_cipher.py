alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def check_encrypt_index(index):
    new_index = 0

    num_of_alphabet = len(alphabet)
    n = index // num_of_alphabet

    if n == 0:
        new_index = index
    else:
        new_index = index - (num_of_alphabet * n)

    return new_index


def check_decrypt_index(index):
    new_index = 0

    num_of_alphabet = len(alphabet)
    n = abs(index // num_of_alphabet)

    if index >= 0:
        new_index = index
    else:
        new_index = index + (num_of_alphabet * n)

    return new_index


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    for letter in start_text:
        position = alphabet.index(letter)

        if cipher_direction == "encode":
            new_position = check_encrypt_index(position + shift_amount)
        elif cipher_direction == "decode":
            new_position = check_decrypt_index(position - shift_amount)
        else:
            print("Invalid option. Goodbye.")
            exit(0)

        end_text += alphabet[new_position]

    print(f"The {cipher_direction}d text is {end_text}", end="\n\n")


def main():
    is_continue = True

    while is_continue:
        direction = input("\nType 'encode' to encrypt and 'decode' to decrypt: ")
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        result = input("Type 'yes' if you want to go again. Otherwise, type 'no': ")

        if result == "no":
            is_continue = False
            print("Goodbye.")


if __name__ == "__main__":
    main()
