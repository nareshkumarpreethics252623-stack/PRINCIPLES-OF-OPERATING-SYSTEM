from collections import deque

P = [("P1", 0, 5), ("P2", 1, 3), ("P3", 2, 6)]
Q = 2

print("PROCESS TABLE")
print("Process  Arrival  Burst")
for p in P:
    print(f"{p[0]:<8}{p[1]:<9}{p[2]}")

# Round Robin
q = deque()
rem = [p[2] for p in P]
ct = [0] * 3
start = [-1] * 3
gantt = []
t = i = 0

while i < 3 or q:
    while i < 3 and P[i][1] <= t:
        q.append(i)
        i += 1

    if not q:
        t = P[i][1]
        continue

    x = q.popleft()

    if start[x] == -1:
        start[x] = t

    s = t
    run = min(Q, rem[x])
    t += run
    rem[x] -= run
    gantt.append((P[x][0], s, t))

    while i < 3 and P[i][1] <= t:
        q.append(i)
        i += 1

    if rem[x]:
        q.append(x)
    else:
        ct[x] = t

# Output
print("\nROUND ROBIN (Time Quantum = 2 ms)")
print("\nGantt Chart:")
print(" | ".join(x[0] for x in gantt))
print("0", end="   ")
for x in gantt:
    print(x[2], end="   ")

print("\n\nProcess  CT  TAT  WT")
tat_sum = wt_sum = 0

for i, (n, a, b) in enumerate(P):
    tat = ct[i] - a
    wt = tat - b
    tat_sum += tat
    wt_sum += wt
    print(f"{n:<8}{ct[i]:<4}{tat:<5}{wt}")

print("\nAverage Turnaround Time =", round(tat_sum / 3, 2), "ms")
print("Average Waiting Time    =", round(wt_sum / 3, 2), "ms")
