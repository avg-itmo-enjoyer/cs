#!/usr/bin/python3

def hamming_code(code):
    corrupted_bit = [
        ("no corrupted bits", None),
        ("r3", 3),
        ("r2", 1),
        ("i3", 5),
        ("r1", 0),
        ("i2", 4),
        ("i1", 2),
        ("i4", 6),
    ]
    s = [0, 0, 0]
    for n, bit in enumerate(code):
        if (n + 1) % 2 in [1]:
            s[0] += code[n]
        if (n + 1) % 4 in [2, 3]:
            s[1] += code[n]
        if (n + 1) % 8 in [4, 5, 6, 7]:
            s[2] += code[n]
    
    corrupted_bit_idx = 0
    for i in reversed(range(len(s))):
        s[i] %= 2
        corrupted_bit_idx += s[i] * (2 ** (len(s) - i - 1))

    ans = code.copy()
    if not corrupted_bit[corrupted_bit_idx][1] is None:
        ans[corrupted_bit[corrupted_bit_idx][1]] = (ans[corrupted_bit[corrupted_bit_idx][1]] + 1) % 2
    return (corrupted_bit[corrupted_bit_idx][0], ans)




if __name__ == "__main__":
    usr_inp = [ int(x) for x in input().strip().split()]
    res = hamming_code(usr_inp)
    print(res[0])
    print(res[1][2], res[1][4], res[1][5], res[1][6])
