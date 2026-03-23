import random

def fitness(x):
    return x ** 2

population = [random.randint(0, 31) for _ in range(6)]

for generation in range(5):
    population = sorted(population, key=fitness, reverse=True)
    next_gen = population[:2]  # Elitism: keep top 2

    while len(next_gen) < 6:
        p1, p2 = random.choices(population[:4], k=2)
        # Crossover (single-point on 5-bit binary)
        point = random.randint(1, 4)
        mask = (1 << point) - 1
        child = (p1 & ~mask) | (p2 & mask)
        # Mutation
        if random.random() < 0.1:
            child ^= (1 << random.randint(0, 4))
        next_gen.append(child & 31)

    population = next_gen
    print(f"Gen {generation+1}: Best = {max(population)}, Fitness = {fitness(max(population))}")