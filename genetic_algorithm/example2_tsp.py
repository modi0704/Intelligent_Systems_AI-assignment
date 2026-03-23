import random, math

cities = [(0,0),(1,3),(4,1),(3,4),(5,2)]

def distance(route):
    return sum(math.dist(cities[route[i]], cities[route[(i+1)%len(route)]])
               for i in range(len(route)))

def crossover(p1, p2):
    start, end = sorted(random.sample(range(len(p1)), 2))
    child = [None]*len(p1)
    child[start:end] = p1[start:end]
    fill = [x for x in p2 if x not in child]
    idx = 0
    for i in range(len(child)):
        if child[i] is None:
            child[i] = fill[idx]; idx += 1
    return child

pop = [random.sample(range(5), 5) for _ in range(10)]

for gen in range(20):
    pop = sorted(pop, key=distance)
    next_gen = pop[:2]
    while len(next_gen) < 10:
        p1, p2 = random.choices(pop[:5], k=2)
        child = crossover(p1, p2)
        if random.random() < 0.2:
            i, j = random.sample(range(5), 2)
            child[i], child[j] = child[j], child[i]
        next_gen.append(child)
    pop = next_gen

print(f"Best route: {pop[0]}, Distance: {distance(pop[0]):.2f}")