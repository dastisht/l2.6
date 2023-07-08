import random

def random_queens():
    q = []
    for _ in range(8):
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        q.append((x, y))
    return q

def queens(q):
    for i in range(8):
        for j in range(i + 1, 8):
            if q[i][0] == q[j][0] or q[i][1] == q[j][1]:
            
                return False
            if abs(q[i][0] - q[j][0]) == abs(q[i][1] - q[j][1]):
              
                return False
    return True

s= []
while len(s) < 4:
    q = random_queens()
    if queens(q):
        s.append(q)

for i, q in enumerate(s):
    print(f"Successful arrangement {i+1}:")
    for q in q:
        print(q)
    print()
