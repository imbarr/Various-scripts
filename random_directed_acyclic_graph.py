import sys
import random

n = int(sys.argv[1])
percent = int(sys.argv[2])

def rand():
    return random.randint(0, 100) <= percent
    
with open("input.txt", "w") as f:
    f.write(sys.argv[1]);
    for i in range(1, n + 1):
        f.write("\n")
        f.write("32767 " * i)
        for j in range(i + 1, n + 1):
            f.write((str(random.randint(0, 1000)) if rand() else "32767") + " ")
    f.write("\n1\n" + sys.argv[1])
               
