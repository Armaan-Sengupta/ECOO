# Problem 2 (w/ Timer): SOLVED

import time
f = open('DATA21.txt', 'r')
start = time.time()
for i in range(10):
    raw = f.readline().split(" ")
    num_rules = int(raw[0])
    iterations = int(raw[1])
    axiom = str(raw[2]).replace('\n', '')
    rules = {}
    for i in range(num_rules):
        raw = f.readline().split(" ")
        q = raw[1].replace('\n', '')
        rules[raw[0]] = q
    k = list(rules.keys())
    l = len(axiom)
    first = axiom[0]
    last = axiom[-1]

    # Keep Track of First and Last
    for i in range(iterations):
        if first in k:
            first = rules[first][0]
        if last in k:
            last = rules[last][-1]

    # cache Dictionary
    cache = dict(zip([x for x in k], [0]*num_rules))
    # Add up Current Letters
    for letter in axiom:
        if letter in k:
            cache[letter] += 1

    # Loop the Thingy Iterations
    for c in range(iterations):
        temp = dict(zip([x for x in k], [0]*num_rules))
        oui = cache.items()
        for item in oui:
            if item[0] in k:        
                i = item[0]
                l -= item[1]
                l += len(rules[i])*item[1]
                cache[i] = 0
                # Add the letters in
                for letter in rules[i]:
                    temp[letter] += item[1]
        cache = temp

    print(f"{first}{last} {l}")
print(f"Time Taken: {time.time() - start}")
f.close()