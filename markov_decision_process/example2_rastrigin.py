import random, math

def rastrigin(pos):
    return 10*len(pos) + sum(x**2 - 10*math.cos(2*math.pi*x) for x in pos)

dim, n, iters = 2, 20, 100
w, c1, c2 = 0.4, 1.5, 1.5

particles  = [[random.uniform(-5,5) for _ in range(dim)] for _ in range(n)]
velocities = [[random.uniform(-1,1) for _ in range(dim)] for _ in range(n)]
pbest      = [p[:] for p in particles]
gbest      = min(pbest, key=rastrigin)

for _ in range(iters):
    for i in range(n):
        for d in range(dim):
            r1, r2 = random.random(), random.random()
            velocities[i][d] = (w * velocities[i][d]
                                 + c1*r1*(pbest[i][d] - particles[i][d])
                                 + c2*r2*(gbest[d]    - particles[i][d]))
            particles[i][d] += velocities[i][d]
        if rastrigin(particles[i]) < rastrigin(pbest[i]):
            pbest[i] = particles[i][:]
    gbest = min(pbest, key=rastrigin)

print(f"Best position: {[round(x,4) for x in gbest]}")
print(f"Best fitness:  {rastrigin(gbest):.4f}")