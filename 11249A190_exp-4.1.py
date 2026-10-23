def dfa(string):
    state = 0
    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = -1
                break
        elif state == 1:
            if ch == 'b':
                state = 2
            else:
                state = -1
                break
        elif state == 2:
            if ch == 'b':
                state = 2
            else:
                state = -1
                break
    if state == 1 or state == 2:
        return "Accepted"
    else:
        return "Rejected"
test_strings = ["a", "ab", "abb", "abbb"]
for s in test_strings:
    print(f"{s} -> {dfa(s)}")