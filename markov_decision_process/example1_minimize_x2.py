import random

n_particles, iterations = 10, 50
w, c1, c2 = 0.5, 1.5, 1.5  # inertia, cognitive, social

particles  = [random.uniform(-10, 10) for _ in range(n_particles)]
velocities = [random.uniform(-1, 1)   for _ in range(n_particles)]
pbest      = particles[:]
gbest      = min(pbest, key=lambda x: x**2)

for _ in range(iterations):
    for i in range(n_particles):
        r1, r2 = random.random(), random.random()
        velocities[i] = (w * velocities[i]
                         + c1 * r1 * (pbest[i] - particles[i])
                         + c2 * r2 * (gbest   - particles[i]))
        particles[i] += velocities[i]
        if particles[i]**2 < pbest[i]**2:
            pbest[i] = particles[i]
    gbest = min(pbest, key=lambda x: x**2)

print(f"Best x: {gbest:.4f}, f(x): {gbest**2:.4f}")