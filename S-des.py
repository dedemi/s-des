permutation_8 = [
    6, 3, 7, 4, 8, 6, 10, 9
]

permutation_10 = [
    3, 5, 2, 7, 4, 10, 1, 9, 8, 6
]

permutation_ip = [
    2, 6, 3, 1, 4, 8, 5, 7
]

expansion = [
    4, 1, 2, 3, 2, 3, 4, 1
]

permutation_s0 = [
    ['01', '00', '11', '10'], ['11', '10', '01', '00'], ['00', '10', '01', '11'], ['11', '01', '11', '10']
]

permutation_s1 = [
    ['00', '01', '10', '11'], ['10', '00', '01', '11'], ['11', '00', '01', '00'], ['10', '01', '00', '11']
]

permutation_4 = [
    2, 4, 3, 1
]

permutation_ip_rev = [
    4, 1, 3, 5, 7, 2, 8, 6
]


def permutation(text, permutation):
    new_text = ''
    for i in range(len(permutation)):
        new_text += text[permutation[i] - 1]
    return new_text


def shift(key, bit):
    new_key = ''
    for i in range(len(key)):
        new_key += key[(i + bit) % len(key)]
    return new_key


def xor(digit1, digit2):
    new_digit = ''
    for i in range(len(digit1)):
        new_digit += str((int(digit1[i]) + int(digit2[i])) % 2)
    return new_digit


def bin_to_dec(digit):
    new_digit = 0
    for i in range(len(digit)):
        new_digit += int(digit[i]) * (2 ** (len(digit) - i - 1))
    return new_digit


def s0(text):
    x = bin_to_dec(text[0] + text[3])
    y = bin_to_dec(text[1] + text[2])
    return permutation_s0[x][y]


def s1(text):
    x = bin_to_dec(text[0] + text[3])
    y = bin_to_dec(text[1] + text[2])
    return permutation_s1[x][y]


def functionf(text, key):
    text = permutation(text, expansion)
    text = xor(text, key)
    text = s0(text[:4]) + s1(text[4:])
    text = permutation(text, permutation_4)
    return text


# key generation
key_in = input('10 bit key: ')
key_in = permutation(key_in, permutation_10)
key_out_1 = permutation(shift(key_in[:5], 1) + shift(key_in[5:], 1), permutation_8)
key_out_2 = permutation(shift(key_in[:5], 3) + shift(key_in[5:], 3), permutation_8)

# encrypt
text = input('8 bit text: ')
text_in = permutation(text, permutation_ip)
sub_text_l, sub_text_r = text_in[:4], text_in[4:]
temp = functionf(sub_text_r, key_out_1)
sub_text_l = xor(sub_text_l, temp)
temp = functionf(sub_text_l, key_out_2)
sub_text_r = xor(sub_text_r, temp)
text_out = permutation(sub_text_r + sub_text_l, permutation_ip_rev)
print('encryption result: ', text_out)

#decrypt
text_in = permutation(text, permutation_ip)
sub_text_l, sub_text_r = text_in[:4], text_in[4:]
temp = functionf(sub_text_r, key_out_2)
sub_text_l = xor(sub_text_l, temp)
temp = functionf(sub_text_l, key_out_1)
sub_text_r = xor(sub_text_r, temp)
text_out = permutation(sub_text_r + sub_text_l, permutation_ip_rev)
print('decryption result', text_out)