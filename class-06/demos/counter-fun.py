from collections import Counter

counter = Counter((3,3,3,3,2,5,5))

i = 0

mcv = counter.most_common()
for i in range(len(mcv)):
  data = mcv[i]
  value = data[0]
  frequency = data[1]
