#/usr/bin/python3
import re

def two_vowels(text):
    regStr = r"\w*[aeiouауоиэыеёюя]{2}\w*(?=\s+[aeiouауоиэыеёюя]*[b-df-hj-np-tv-zб-дж-зй-нп-тф-ъь]?[aeiouауоиэыеёюя]*[b-df-hj-np-tv-zб-дж-зй-нп-тф-ъь]?[aeiouауоиэыеёюя]*[b-df-hj-np-tv-zб-дж-зй-нп-тф-ъь]?[aeiouауоиэыеёюя]*\s+)"
    print("\n", regStr, "\n")
    reg = re.compile(regStr, re.IGNORECASE)
    return reg.findall(text)

if __name__ == "__main__":
    inp = ""
    print("Input your text to match pattern:")
    while True:
        try:
            line = input()
            inp += line + "\n"
        except EOFError:
            break
    
    i = 0
    for el in two_vowels(inp):
        i += 1
        print(i, el)
