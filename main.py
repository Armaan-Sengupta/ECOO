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
    rules[raw[0]] = raw[1].replace('\n', '')
  k = list(rules.keys())
  for i in range(iterations):
    temp = []
    for letter in axiom:
      if letter in k:
        temp.append(rules[letter])
      else:
        temp.append(letter)
    axiom = ''.join(temp)
  
  print(f"{axiom[0]}{axiom[-1]} {len(axiom)}")
print(f"Time Taken: {time.time() - start}")
f.close()