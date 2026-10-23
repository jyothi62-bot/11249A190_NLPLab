def dfa(s):
    if s.startswith('a') and set(s[1:]) <= {'b'}:
        print("Accepted")
    else:
        print("Rejected")

for s in ["a", "ab", "abb", "abbb"]:
    print(s, ":", end=" ")
    dfa(s)