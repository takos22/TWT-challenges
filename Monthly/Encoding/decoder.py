def decode(encoded):
    decoded = ""
    i = 0
    while i < len(encoded):
        decoded += encoded[i+1] * int(encoded[i])
        i += 2
    return decoded


print(decode("3A3B1C1D"))  # AAABBBCD
print(decode("1A1B1C"))  # ABC
print(decode("1A3a1A1B1b1C1Z"))  # AaaaABbCZ
print(decode("4142"))  # 11112222
print(decode("99"))  # 999999999
print(decode("9g9g2g"))  # gggggggggggggggggggg
