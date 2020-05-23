def deja_vu(string):
    if len(string) > 26: return "Deja Vu"
    seen = set()
    for l in string:
        if l in seen: return "Deja Vu"
        seen.add(l)
    return "Unique"

print(deja_vu("aaaaaaaghhhhhhhjkll"))
print(deja_vu("aghjkl"))