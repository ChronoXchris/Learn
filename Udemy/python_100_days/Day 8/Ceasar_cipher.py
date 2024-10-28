alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number\n"))


def ceasar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1

        for letter in original_text:

            if letter not in alphabet_lower:
                output_text += letter
            else:
                shifted_position = alphabet_lower.index(letter) - shift_amount
                shifted_position %= len(alphabet_lower)
                output_text += alphabet_lower[shifted_position]
        print("Here is the {encode_or_decode} result: {output_text}")


ceasar(original_text=text, shift_amount=shift, encode_or_decode=direction)

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number\n"))

    ceasar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Godbye")