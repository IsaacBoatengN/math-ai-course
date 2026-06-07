---
title: Randomized Neural Networks for Optimal Stopping
author: Math AI Course
date: 2026-06-06
marp: true
paginate: true
---

# Randomized Neural Networks for Optimal Stopping

- Optimal stopping formulation
- Randomized continuation-value approximation
- American put example, theory, and practical guidance

---

## Optimal Stopping: Formal Setup

- Let $(X_t)_{t=0}^T$ be a reward process on a filtered probability space $(\Omega, \mathcal{F}, \mathbb{P})$
- A stopping time $\tau$ satisfies $\{\tau = t\} \in \mathcal{F}_t$
- Value function:

$$
V(t, x) = \sup_{\tau \ge t} \mathbb{E}[X_{\tau} \mid X_t = x]
$$

- Key point: choose the stopping time that maximizes expected reward given current state

---

## Continuation Value and Stopping Rule

- Continuation value:

$$
C(t, x) = \mathbb{E}[V(t+1, X_{t+1}) \mid X_t = x]
$$

- Dynamic programming representation:

$$
V(t,x) = \max\{ X_t, C(t,x) \}
$$

- Stopping criterion:

$$
\text{stop at } t \iff X_t \ge C(t,x)
$$

- Otherwise continue and re-evaluate at $t+1$

---

## Randomized Neural Network Architecture

- Feature map with fixed random hidden parameters:

$$
\Phi(x) = \sigma(W x + b)
$$

- $W \in \mathbb{R}^{d \times m}$, $b \in \mathbb{R}^d$ are drawn randomly and fixed
- Output model:

$$
C(t,x) \approx \beta \cdot \Phi(x)
$$

- Only output weights $\beta$ are trained via linear regression
- This is a form of Extreme Learning Machine / random feature model

---

## Training Algorithm

- For each exercise date $t$ from $T-1$ down to $0$:
  1. simulate $N$ paths from current state distribution
  2. compute targets $y_i \approx V(t+1, X_{t+1}^i)$ or discounted continuation payoff
  3. compute random features $\Phi(x_i)$ for each training point
  4. solve

$$
\beta_t = \arg\min_{\beta} \sum_{i=1}^N (y_i - \beta \cdot \Phi(x_i))^2 + \lambda \|\beta\|^2
$$

- Stopping rule at runtime:

$$
\text{exercise if } X_t \ge \beta_t \cdot \Phi(x_t)
$$

---

## Training Algorithm and Pseudocode

```python
W = np.random.normal(scale=1.0/state_scale, size=(d, state_dim))
b = np.random.uniform(-1, 1, size=(d,))

def phi(x):
    return np.tanh(W @ x + b)

for t in reversed(range(T)):
    Phi = []
    y = []
    for path in paths:
        x_t = path.state_at(t)
        Phi.append(phi(x_t))
        y.append(estimate_continuation_value(path, t))
    Phi = np.vstack(Phi)
    beta = np.linalg.solve(Phi.T @ Phi + reg * np.eye(d), Phi.T @ y)
    models[t] = beta

# at decision time
action = 'stop' if payoff(x_t) >= models[t] @ phi(x_t) else 'continue'
```

---

## Method Comparison

| Method | Complexity | Memory | Accuracy trade-off |
|:------:|:----------:|:------:|:------------------:|
| Randomized NN | $O(N d)$ | $O(d)$ | fast; may underfit if $d$ too small |
| LSMC | $O(N^3)$ exact, $O(N p^2)$ basis | $O(N p)$ | strong low-dim accuracy |
| Full Deep NN | $O(N p^2)$–$O(N p^3)$ | $O(p^2)$ | flexible but expensive |

- $N$ = sample count, $d$ = random feature size, $p$ = basis / hidden width
- Randomized NN trades hidden-layer training for scalable regression

---

## Convergence and Theoretical Support

- Randomized features have a universal approximation property under mild conditions
- Notable results:
  - Rahimi & Recht (2008): random Fourier features approximate shift-invariant kernels
  - Igelnik & Pao (1995), Lu et al. (2017): random networks approximate continuous functions with high probability
- As $d \to \infty$ and $N \to \infty$:

$$
\sup_x |\beta_d \cdot \Phi_d(x) - C(t,x)| \to 0
$$

- Requires:
  - expressive random feature distribution
  - enough paths covering relevant states
  - proper regularization of $\beta$

---

## Limitations and When to Prefer Full Training

- Curse of dimensionality:
  - high-dimensional state spaces still need many random features and paths
- Bias due to random initialization:
  - a single random draw may miss problem-relevant directions
- Prefer full deep training when:
  - the continuation value has complex learned structure
  - abundant data and compute are available
  - feature engineering is difficult and hidden-layer learning is necessary

---

## Concrete Example: American Put

- Parameters: $S_0=100$, $K=100$, $r=0.05$, $\sigma=0.2$, $T=1$ year
- Discretize with 3 decision dates, 10,000 Monte Carlo paths, 500 random features

| $S_t$ | Payoff | Continuation $C(t,x)$ | Decision |
|:-----:|:------:|:---------------------:|:--------:|
| 80    | 20     | 18.4                  | Stop     |
| 90    | 10     | 10.1                  | Continue |
| 100   | 0      | 5.2                   | Continue |
| 110   | 0      | 2.7                   | Continue |

- Shows how continuation value can exceed exercise payoff for moderate in-the-money states
- Real implementation uses discounted future payoffs and recomputed targets at each $t$

---

## Applications and Recommendations

- Beyond finance:
  - clinical trials: early stopping for efficacy/safety
  - maintenance: decide when to repair or replace assets
  - inventory: stop ordering or adjust replenishment timing

- Practical recommendations:
  - choose Gaussian or uniform features based on state scaling
  - start with 5–10× state dimension for $d$
  - augment state with path summaries for path-dependent problems
  - compare with LSMC and full deep models for robustness
