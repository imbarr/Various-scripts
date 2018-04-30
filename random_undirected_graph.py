import random
import sys

num = int(sys.argv[1])
percent = int(sys.argv[2])
m = []
for i in range(num):
	m.append([])
	for j in range(i):
		m[i].append(str(int(random.randint(0, 100) <= percent)))

for i in range(num):
	m[i].append(str(0))
	for j in range(i + 1, num):
		m[i].append(m[j][i])


with open("in.txt", "w") as f:
	f.write("\n".join([str(num)] + map(lambda l: " ".join(l), m)))
