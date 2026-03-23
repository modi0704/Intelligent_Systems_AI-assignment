import random

# 4x4 grid: 0=safe, 1=hole, 2=goal  (row-major index)
grid = [0,0,0,0,
        0,1,0,1,
        0,0,0,1,
        1,0,0,2]

n_states, n_actions = 16, 4          # up/down/left/right
Q = [[0.0]*n_actions for _ in range(n_states)]
alpha, gamma, epsilon = 0.1, 0.9, 0.2

def step(s, a):
    row, col = divmod(s, 4)
    dr, dc = [(-1,0),(1,0),(0,-1),(0,1)][a]
    nr, nc = max(0,min(3,row+dr)), max(0,min(3,col+dc))
    ns = nr*4 + nc
    if grid[ns] == 1: return ns, -1, True   # hole
    if grid[ns] == 2: return ns, +1, True   # goal
    return ns, 0, False

for episode in range(1000):
    s = 0
    for _ in range(50):
        a = (random.randint(0,3) if random.random() < epsilon
             else Q[s].index(max(Q[s])))
        ns, r, done = step(s, a)
        Q[s][a] += alpha * (r + gamma*max(Q[ns]) - Q[s][a])
        s = ns
        if done: break

policy = ['↑↓←→'[Q[s].index(max(Q[s]))] for s in range(16)]
print("Learned Policy:")
for i in range(0, 16, 4):
    print(policy[i:i+4])
