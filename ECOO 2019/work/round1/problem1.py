# Problem 1: SOLVED

f = open('DATA11.txt', 'r')
for i in range(10):
  raw = f.readline().split(" ")
  num_shirts = int(raw[0])
  number_of_events = int(raw[1])
  number_of_days = int(raw[2])
  clean = num_shirts
  dirty = 0
  days = list(map(int, f.readline().split(" ")))
  count_laundry = 0

  for i in range(number_of_days):
    if clean == 0:
      count_laundry += 1
      clean = num_shirts
      
    if (i + 1) in days:
      c = days.count(i+1)
      clean += 1*c
      num_shirts += 1*c
    
    clean -= 1

  print(count_laundry)
f.close()