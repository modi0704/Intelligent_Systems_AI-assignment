AI Optimization Algorithms Assignment
Descriptions and 2 coded examples each for three classic AI/optimization techniques.

## 1. Genetic Algorithm (GA)

### Description
A **Genetic Algorithm** is a search and optimization technique inspired by the process of **natural selection**. It evolves a population of candidate solutions over multiple generations using three key operations:

| Operation | Description |
|-----------|-------------|
| **Selection** | Favor better-performing individuals to reproduce |
| **Crossover** | Combine two parents to produce offspring |
| **Mutation** | Randomly alter a solution to maintain diversity |

GAs are well-suited for large, complex search spaces where traditional methods struggle.

### Examples
| File | Problem | Technique |
|------|---------|-----------|
| `example1_maximize_x2.py` | Maximize f(x) = x² over integers 0–31 | Binary encoding, single-point crossover, bit-flip mutation |
| `example2_tsp.py` | Find shortest route visiting 5 cities | Permutation encoding, order crossover (OX), swap mutation |

---

##  2. Particle Swarm Optimization (PSO)

### Description
**Particle Swarm Optimization** is a population-based metaheuristic inspired by the **social behavior of birds flocking or fish schooling**. Each particle represents a candidate solution and moves through the search space influenced by:

| Force | Description |
|-------|-------------|
| **Inertia (w)** | Keeps the particle moving in its current direction |
| **Cognitive (c₁)** | Attraction toward the particle's own best position |
| **Social (c₂)** | Attraction toward the swarm's global best position |

PSO is simple to implement and effective for continuous optimization problems.

### Examples
| File | Problem | Technique |
|------|---------|-----------|
| `example1_minimize_x2.py` | Minimize f(x) = x² | 1D PSO with personal & global best tracking |
| `example2_rastrigin.py` | Minimize Rastrigin function (2D) | Multi-dimensional PSO on a complex multi-modal landscape |

---

##  3. Markov Decision Process (MDP)

### Description
A **Markov Decision Process** is a mathematical framework for modeling **sequential decision-making** under uncertainty. It is defined by:

| Component | Symbol | Description |
|-----------|--------|-------------|
| **States** | S | All possible situations the agent can be in |
| **Actions** | A | Choices available to the agent |
| **Transitions** | T(s, a, s') | Probability of moving to state s' after taking action a in state s |
| **Rewards** | R(s) | Feedback signal for being in a state |
| **Discount Factor** | γ | How much future rewards are valued |

MDPs are the backbone of **Reinforcement Learning**.

### Examples
| File | Problem | Technique |
|------|---------|-----------|
| `example1_value_iteration.py` | 4-state linear MDP | Value Iteration to find optimal state values and policy |
| `example2_q_learning.py` | 4×4 FrozenLake-style grid | Q-Learning (model-free RL) to learn navigation policy |

---

##  Requirements

- Python 3.7+
- No external libraries required — all examples use the Python standard library only (`random`, `math`)

---

##  How to Run

```bash
# Clone the repository
git clone https://github.com/<your-username>/ai-assignment.git
cd ai-assignment

# Run any example directly
python genetic_algorithm/example1_maximize_x2.py
python particle_swarm_optimization/example2_rastrigin.py
python markov_decision_process/example2_q_learning.py
```
