# 4-state MDP: S0 -> S1 -> S2 -> S3(terminal)
# Actions: 'stay' or 'move'

states   = [0, 1, 2, 3]
rewards  = {0: -1, 1: -1, 2: -1, 3: 10}  # reward upon entering state
gamma    = 0.9

# transitions[s][a] = (next_state, probability)
transitions = {
    0: {'move': (1, 1.0), 'stay': (0, 1.0)},
    1: {'move': (2, 1.0), 'stay': (1, 1.0)},
    2: {'move': (3, 1.0), 'stay': (2, 1.0)},
    3: {'move': (3, 1.0), 'stay': (3, 1.0)},  # terminal
}

V = {s: 0 for s in states}

for _ in range(100):
    for s in states[:-1]:  # skip terminal
        V[s] = max(
            rewards[ns] + gamma * V[ns]
            for a, (ns, _) in transitions[s].items()
        )

policy = {}
for s in states[:-1]:
    policy[s] = max(transitions[s],
                    key=lambda a: rewards[transitions[s][a][0]]
                                  + gamma * V[transitions[s][a][0]])

print("Values:", V)
print("Policy:", policy)