def queens(q):
    for i in range(8):
        for j in range(i + 1, 8):
            if q[i][0] == q[j][0] or q[i][1] == q[j][1]:
                return False
            if abs(q[i][0] - q[j][0]) == abs(q[i][1] - q[j][1]):
                return False
    return True

q = []
for _ in range(8):
    x, y = map(int, input().split())
    q.append((x, y))
result = queens(q)

print(result)
