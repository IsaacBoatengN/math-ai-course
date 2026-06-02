# Lagrange Multipliers: Constrained Optimization

## Definition

The method of Lagrange multipliers is a powerful technique for finding the local maxima and minima of a function subject to one or more equality constraints. For a function $f(x, y)$ subject to the constraint $g(x, y) = c$, we introduce a new variable $\lambda$ (the Lagrange multiplier) and solve the system:

$$\nabla f(x, y) = \lambda \nabla g(x, y)$$

$$g(x, y) = c$$

This gives us the system of equations:

$$\frac{\partial f}{\partial x} = \lambda \frac{\partial g}{\partial x}$$

$$\frac{\partial f}{\partial y} = \lambda \frac{\partial g}{\partial y}$$

$$g(x, y) = c$$

The solutions $(x, y, \lambda)$ correspond to candidate points where $f$ may have an extremum under the constraint.

## Example

**Problem:** Maximize the area $A = xy$ of a rectangle subject to the perimeter constraint $2x + 2y = 20$ (i.e., $x + y = 10$).

**Step 1:** Set up the Lagrangian function:
$$\mathcal{L}(x, y, \lambda) = xy + \lambda(10 - x - y)$$

**Step 2:** Take partial derivatives and set to zero:
$$\frac{\partial \mathcal{L}}{\partial x} = y - \lambda = 0 \quad \Rightarrow \quad y = \lambda$$
$$\frac{\partial \mathcal{L}}{\partial y} = x - \lambda = 0 \quad \Rightarrow \quad x = \lambda$$
$$\frac{\partial \mathcal{L}}{\partial \lambda} = 10 - x - y = 0$$

**Step 3:** Solve the system:
From $x = \lambda$ and $y = \lambda$, we get $x = y$.
Substitute into $x + y = 10$:
$$x + x = 10 \quad \Rightarrow \quad 2x = 10 \quad \Rightarrow \quad x = 5$$
Thus $y = 5$ and $\lambda = 5$.

**Step 4:** The maximum area is:
$$A = xy = 5 \times 5 = 25 \text{ square units}$$

We can verify this is a maximum by checking that $x = 5, y = 5$ gives a square, which is known to maximize area for a fixed perimeter.

## Why This Matters

Lagrange multipliers are fundamental in economics (utility maximization with budget constraints), physics (minimizing energy with conservation laws), machine learning (SVM optimization with constraints), and engineering (design optimization under resource limits). The method elegantly transforms a constrained problem into an unconstrained one by introducing auxiliary variables, making complex optimization problems tractable.