f = open('DATA21.txt', 'r')
for i in range(10):
  raw = f.readline().split(" ")
  num_rules = int(raw[0])
  iterations = int(raw[1])
  axiom = str(raw[2]).replace('\n', '')
  rules = []
  for i in range(num_rules):
    raw = f.readline().split(" ")
    rules.append((raw[0], raw[1].replace('\n', '')))

  for i in range(iterations):
    for rule in rules:
      axiom = axiom.replace(rule[0], rule[1])
  
  print(f"{axiom[0]}{axiom[-1]} {len(axiom)}")
f.close()