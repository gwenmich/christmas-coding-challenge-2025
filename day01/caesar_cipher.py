import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for char in original_text:
        if char not in alphabet:
            output_text += char
        else:
            current_index = alphabet.index(char)
            new_index = (current_index + shift_amount) % 26
            output_text += alphabet[new_index]

    print(f"{encode_or_decode.capitalize()}d text: {"".join(output_text)}")


continue_cipher = True
print(logo.logo)

while continue_cipher:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if restart == "no":
        continue_cipher = False
        print("Goodbye")