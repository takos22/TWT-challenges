def encode(decoded):
    encoded = ""
    i = 0
    while i < len(decoded):
        j = i+1
        while j < len(decoded) and j < i+9 and decoded[j] == decoded[i]:
            j += 1
        encoded += str(j-i) + decoded[i]
        i = j
    return encoded


print(encode("AAABBBCD")) # 3A3B1C1D
print(encode("ABC")) # 1A1B1C
print(encode("AaaaABbCZ")) # 1A3a1A1B1b1C1Z
print(encode("11112222")) # 4142
print(encode("999999999")) # 99
print(encode("gggggggggggggggggggg")) # 9g9g2g
