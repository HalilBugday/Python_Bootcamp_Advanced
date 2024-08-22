#usg: halil 1 -> ibmjm
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(orginal_text, shift_amount):
    cipher_text = ""

    for letter in orginal_text:
        shifted_position = alphabet.index(letter) + shift_amount # 3 ->  3 + 4 -> 7
        shifted_position = shifted_position %len(alphabet) # [0-25],  27->2 
        cipher_text = cipher_text + alphabet[shifted_position]
    print(f"Here is the your encoded result: {cipher_text}")


#usg: ibmjm -> halil 1
def decrypt(orginal_text, shift_amount):
    unencrypted_text = ""

    for letter in orginal_text:
        shifted_position = alphabet.index(letter) - shift_amount # 7 -> 7 - 4 -> 3
        shifted_position = shifted_position %len(alphabet) # [0-25], -3->28
        unencrypted_text = unencrypted_text + alphabet[shifted_position]
    print(f"Here is the your decoded result: {unencrypted_text}")