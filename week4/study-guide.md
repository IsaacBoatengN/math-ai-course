# Study Guide: Computational Inverse Problems Governed by PDEs

## 1. Concept Explanation

### 1.1 What is an inverse problem?

An inverse problem asks: given observed data, what are the unknown model parameters or inputs that produced that data?

- In a forward problem, the model parameters and PDE are known, and we compute the state or observables.
- In an inverse problem, the state observations are known, and we infer the model parameters or forcing terms.

Intuition: imagine measuring surface temperature on a metal plate and asking what thermal conductivity inside the plate would explain those measurements. This is a reversal of the usual modeling direction.

Formally, an inverse problem can be stated as:

- data: $d \in \mathcal{Y}$, where $\mathcal{Y}$ is a data space
- parameter: $m \in \mathcal{M}$, where $\mathcal{M}$ is a parameter space
- forward map: $F: \mathcal{M} \to \mathcal{Y}$ such that $F(m)$ is the predicted observation

The inverse problem is: find $m$ such that

$$F(m) \approx d. $$

In PDE-governed inverse problems, the forward map is defined implicitly by a PDE constraint.

### 1.2 PDE-constrained optimization formulation

The standard solution strategy casts the inverse problem as a PDE-constrained optimization problem.

Intuition first:

- We build an objective function measuring misfit between predicted and observed data.
- We impose the PDE as a constraint so the predicted data are physically admissible.
- The unknown parameter appears in the PDE, not directly in the objective.

A generic PDE-constrained formulation is:

$$\begin{aligned}
\min_{m,u} \;& J(u,m) = \frac12\|B u - d\|_{\Gamma^{-1}}^2 + \frac{\alpha}{2} \|R(m)\|_{\mathcal{M}}^2, \\
\text{s.t. } \;& A(m; u) = f,\\
\end{aligned}$$

where:

- $u$ is the PDE state variable (e.g., temperature, potential).
- $m$ is the parameter to infer (e.g., conductivity, source intensity).
- $A(m; u) = f$ represents the governing PDE and boundary conditions.
- $B$ is the observation operator mapping the state to measurement locations.
- $d$ is the observed data.
- $\Gamma$ is the data covariance or weighting operator for errors.
- $R(m)$ is a regularization operator.
- $\alpha > 0$ is the regularization parameter.

The PDE constraint can be enforced strongly by introducing a Lagrangian or weakly via reduced formulations. For the reduced formulation, we eliminate $u$ by writing $u = S(m)$ as the PDE solution operator, giving:

$$\min_m \frac12\|B S(m) - d\|_{\Gamma^{-1}}^2 + \frac{\alpha}{2} \|R(m)\|_{\mathcal{M}}^2. $$

A Lagrange multiplier approach yields the first-order optimality conditions (Karush-Kuhn-Tucker conditions) linking adjoint variables, forward states, and parameter updates.

### 1.3 Deterministic (Tikhonov) vs. Bayesian approaches

#### Intuition

- Deterministic approach: impose regularization and solve a single optimization problem. We recover a best-fit parameter under a penalty that controls instability.
- Bayesian approach: treat the unknown parameter as a random field and compute a posterior distribution, capturing uncertainty from noise, model error, and ill-posedness.

#### Formal comparison

Deterministic Tikhonov formulation:

$$\min_m \frac12 \|B S(m) - d\|_{\Gamma^{-1}}^2 + \frac{\alpha}{2} \|m - m_\text{prior}\|_{\mathcal{C}^{-1}}^2. $$

This is equivalent to a maximum a posteriori (MAP) estimate when the noise is Gaussian with covariance $\Gamma$ and the prior on $m$ is Gaussian with covariance $\mathcal{C}$.

Bayesian formulation:

- Prior: $m \sim \mathcal{N}(m_{\text{prior}}, \mathcal{C})$.
- Likelihood: $d \mid m \sim \mathcal{N}(B S(m), \Gamma)$.

The posterior density is

$$\pi(m\mid d) \propto \exp\left( -\frac12\|B S(m) - d\|_{\Gamma^{-1}}^2 - \frac12\|m - m_{\text{prior}}\|_{\mathcal{C}^{-1}}^2 \right).$$

Important distinctions:

- Deterministic Tikhonov gives one estimate $\hat m$; Bayesian gives a distribution over $m$.
- Bayesian methods quantify uncertainty and can propagate it to predictions; deterministic methods may quantify uncertainty only via asymptotic approximations or Lagrange multiplier sensitivity.
- In nonlinear problems, the posterior may be non-Gaussian, while deterministic Tikhonov still yields a single point estimate.

| Feature | Deterministic (Tikhonov) | Bayesian |
|---------|-------------------------|----------|
| Output | Single point estimate | Posterior distribution |
| Handles uncertainty? | No (needs extra step) | Yes, naturally |
| Computational cost | Low to moderate | High (sampling) |
| Prior information | As regularization | Full probability model |
| Solution method | Optimization | Sampling or optimization (MAP) |

## 2. Worked Examples with Full Solutions

### Example 1: Steady-state heat conduction — recover thermal conductivity

#### Problem statement

Let $\Omega \subset \mathbb{R}^n$ be a bounded domain with boundary $\partial\Omega$. The steady-state heat equation with spatially varying conductivity $\kappa(x)$ is

$$-\nabla \cdot (\kappa(x)\nabla u(x)) = 0, \qquad x \in \Omega,$$

with Dirichlet boundary data $u = g$ on $\partial\Omega$. Observations are temperature values at sensor locations $\{x_i\}_{i=1}^M$.

Goal: recover $\kappa(x)$ from measurements $d_i = u(x_i) + \eta_i$.

#### PDE-constrained optimization formulation

Choose parameter $m = \log \kappa$ to enforce positivity, and state $u$ solves

$$-\nabla \cdot (e^{m(x)} \nabla u(x)) = 0 \,\text{ in }\Omega, \qquad u = g \text{ on }\partial\Omega.$$

Observation operator: $(B u)_i = u(x_i)$.

Cost functional:

$$J(u,m) = \frac12 \sum_{i=1}^M (u(x_i) - d_i)^2 + \frac{\alpha}{2}\|m - m_0\|_{H^1(\Omega)}^2.$$ 

Here $m_0$ is a prior guess and $\alpha$ is a regularization weight.

#### Lagrangian and first-order conditions

Define the Lagrangian with adjoint $p(x)$:

$$\mathcal{L}(u,m,p) = J(u,m) + \int_\Omega p\, (-\nabla\cdot(e^{m}\nabla u))\,dx.$$

Integrate by parts to move derivatives onto $p$:

$$\mathcal{L} = \frac12\sum_{i=1}^M (u(x_i)-d_i)^2 + \frac{\alpha}{2}\|m-m_0\|_{H^1}^2 + \int_\Omega e^{m} \nabla u\cdot\nabla p\,dx - \int_{\partial\Omega} e^{m} p \nabla u\cdot n \,ds.$$ 

Assume the boundary integral vanishes because $p|_{\partial\Omega}=0$ or $u$ is fixed.

Stationarity conditions:

1. Forward equation (state):

$-\nabla\cdot(e^{m}\nabla u)=0$ in $\Omega$, $u=g$ on $\partial\Omega$.

2. Adjoint equation:

$$-\nabla\cdot(e^{m}\nabla p) = -\sum_{i=1}^M (u(x_i)-d_i)\,\delta(x-x_i), \qquad p=0 \text{ on }\partial\Omega.$$ 

3. Gradient with respect to $m$:

$$\frac{\partial \mathcal{L}}{\partial m}[\tilde m] = \int_\Omega \tilde m\, e^{m} \nabla u\cdot\nabla p\,dx + \alpha \langle m-m_0, \tilde m\rangle_{H^1} = 0$$

for all variations $\tilde m$. Thus the reduced gradient is

$$g(m) = e^{m} \nabla u\cdot\nabla p - \alpha \Delta m + \alpha (m-m_0).$$

#### Solution procedure

1. Initialize $m^{(0)} = m_0$.
2. Solve the forward PDE for $u^{(k)}$.
3. Solve the adjoint PDE for $p^{(k)}$ with the data residual as point sources.
4. Compute gradient $g(m^{(k)})$.
5. Update $m$ with a line search, e.g. $m^{(k+1)} = m^{(k)} - \tau_k g(m^{(k)})$.

For a linearized demonstration, assume $\kappa(x)$ is piecewise constant on two subregions, $\kappa_1$ and $\kappa_2$.

##### Simplified illustrative solution

Suppose $\Omega = [0,1]$ and $u(0)=0$, $u(1)=1$. If $\kappa$ is constant, the exact solution is $u(x)=x$. Then temperature at any interior point agrees with the boundary linear profile. If measurements $d_i$ deviate from $x_i$, the reconstruction must adjust $\kappa(x)$.

In the general variable-coefficient case, the adjoint residual identifies where the misfit is sensitive to $m$. The product $e^{m}\nabla u\cdot\nabla p$ forms a sensitivity kernel: it is large where both forward and adjoint gradients are large.

##### Remarks

- Because the inverse problem is ill-posed, the regularization term $\|m-m_0\|_{H^1}^2$ is critical.
- The use of $m=\log \kappa$ enforces positivity and often improves optimization.
- In practice, one discretizes $m$ and $u$ and solves the coupled KKT system or uses reduced-space optimization with PDE solves.

### Example 2: Source inversion in the Poisson equation

#### Problem statement

Let $\Omega \subset \mathbb{R}^n$ and consider the Poisson equation with source $s(x)$:

$$-\Delta u(x) = s(x), \qquad x\in \Omega, $$
with boundary condition $u = 0$ on $\partial\Omega$. Observations are noisy measurements of $u$ at sensor points $\{x_i\}_{i=1}^M$.

Goal: recover $s(x)$ from observations $d_i = u(x_i)+\eta_i$.

#### PDE-constrained optimization formulation

State equation:

$$-\Delta u = s \,\text{ in }\Omega, \qquad u=0\text{ on }\partial\Omega.$$ 

Cost functional:

$$J(u,s) = \frac12\sum_{i=1}^M (u(x_i)-d_i)^2 + \frac{\alpha}{2} \|s\|_{L^2(\Omega)}^2. $$

The state and source are linked by the PDE, and $s$ is the control variable.

#### Lagrangian and optimality conditions

Lagrangian with adjoint $p(x)$:

$$\mathcal{L}(u,s,p) = \frac12\sum_{i=1}^M (u(x_i)-d_i)^2 + \frac{\alpha}{2}\|s\|_{L^2}^2 + \int_\Omega p(-\Delta u - s)\,dx. $$

Integrate by parts:

$$\mathcal{L} = \frac12\sum_{i=1}^M (u(x_i)-d_i)^2 + \frac{\alpha}{2}\|s\|_{L^2}^2 + \int_\Omega \nabla p\cdot\nabla u\,dx - \int_{\partial\Omega} p\partial_n u \,ds - \int_\Omega p s\,dx. $$

With $u=0$ on the boundary and $p=0$ on the boundary for the adjoint, the boundary term disappears.

Stationarity conditions:

1. Forward PDE: $-\Delta u = s$ in $\Omega$, $u=0$ on $\partial\Omega$.
2. Adjoint PDE: $-\Delta p = -\sum_{i=1}^M (u(x_i)-d_i)\,\delta(x-x_i)$ in $\Omega$, $p=0$ on $\partial\Omega$.
3. Control optimality: $\alpha s + p = 0$ in $\Omega$.

Thus the optimal source is

$$s = -\frac{1}{\alpha} p.$$ 

Substituting into the forward PDE gives the coupled optimality system:

$$-\Delta u = -\frac{1}{\alpha} p, \qquad -\Delta p = -\sum_{i=1}^M (u(x_i)-d_i)\,\delta(x-x_i).$$

This is a linear system in $(u,p)$.

#### Full solution on a simple domain

Assume $\Omega = (0,1)$ with homogeneous Dirichlet boundary conditions and a single observation at $x_1 = x^*$. The Green's function for $-\frac{d^2}{dx^2}$ on $(0,1)$ is

$$G(x,y) = \begin{cases} x(1-y), & x\le y, \\ y(1-x), & x>y. \end{cases}$$

Then the forward state for source $s$ is

$$u(x) = \int_0^1 G(x,y) s(y)\,dy.$$ 

The adjoint solves

$$-\frac{d^2 p}{dx^2} = -(u(x^*)-d)\,\delta(x-x^*), \qquad p(0)=p(1)=0,$$

giving

$$p(x) = (u(x^*)-d) G(x,x^*).$$

The optimal source is

$$s(x) = -\frac{1}{\alpha} p(x) = -\frac{u(x^*)-d}{\alpha} G(x,x^*).$$

Substitute into the forward equation and evaluate at $x^*$:

$$u(x^*) = \int_0^1 G(x^*,y) s(y)\,dy = -\frac{u(x^*)-d}{\alpha} \int_0^1 G(x^*,y) G(y,x^*)\,dy. $$

Define constant

$$C = \int_0^1 G(x^*,y)^2 \,dy. $$

Then

$$u(x^*) = -\frac{C}{\alpha}(u(x^*)-d).$$

Solve for $u(x^*)$:

$$u(x^*) \left(1 + \frac{C}{\alpha} \right) = \frac{C}{\alpha} d,$$

so

$$u(x^*) = \frac{C}{\alpha + C} d.$$ 

Hence the optimal source is

$$s(x) = -\frac{d}{\alpha + C} G(x,x^*).$$

This illustrates how the data $d$ is filtered by the regularization parameter $\alpha$ and the Green's function structure.

#### Remarks

- The source inversion is linear in $s$ and admits a closed-form analysis on simple domains.
- Regularization prevents arbitrarily oscillatory sources that fit a single noisy observation.
- In higher dimensions, the same adjoint-based gradient computation is used, but the coupling is solved numerically.

## 3. Practice Problems with Solutions

### Problem 1: Conductivity inversion with a 1D rod

Consider the 1D steady diffusion equation on $[0,1]$:

$$-\frac{d}{dx}\left(\kappa(x) \frac{du}{dx}\right) = 0, \qquad u(0)=0,\; u(1)=1.$$ 

Observations are $u(0.25)=0.2$, $u(0.5)=0.45$, and $u(0.75)=0.7$. Suppose the conductivity is piecewise constant with unknown values $\kappa_1$ on $[0,0.5]$ and $\kappa_2$ on $(0.5,1]$. Formulate the Tikhonov inverse problem and derive the normal equations for $(\kappa_1,\kappa_2)$.

#### Solution

The analytic forward solution satisfies continuity of flux at $x=0.5$ and boundary conditions. The state is linear on each interval with slopes:

$$u'(x) = \frac{1}{\kappa_1} C_1, \quad 0<x<0.5; \qquad u'(x) = \frac{1}{\kappa_2} C_2, \quad 0.5<x<1,$$

with flux continuity $\kappa_1 u'(0.5^-) = \kappa_2 u'(0.5^+)$. Using $u(0)=0$ and $u(1)=1$, we obtain

$$u(x) = \begin{cases} \frac{x}{0.5 + 0.5\kappa_1/\kappa_2}, & x\le 0.5, \\ \frac{0.5}{0.5 + 0.5\kappa_1/\kappa_2} + \frac{x-0.5}{0.5 + 0.5\kappa_2/\kappa_1}, & x>0.5. \end{cases}$$

Denote parameters $a=1/\kappa_1$ and $b=1/\kappa_2$; then continuity and boundary conditions lead to a linear relation. The Tikhonov objective is

$$J(a,b) = \frac12 \sum_{i=1}^3 (u(x_i; a,b) - d_i)^2 + \frac{\alpha}{2}((a-a_0)^2 + (b-b_0)^2).$$

The normal equations are

$$\nabla_{a} J = \sum_{i=1}^3 (u(x_i)-d_i) \frac{\partial u(x_i)}{\partial a} + \alpha(a-a_0) = 0,$$

$$\nabla_{b} J = \sum_{i=1}^3 (u(x_i)-d_i) \frac{\partial u(x_i)}{\partial b} + \alpha(b-b_0) = 0.$$ 

Solving those equations yields the regularized estimate for $(a,b)$, which are then inverted to $\kappa_1=1/a$ and $\kappa_2=1/b$.

For measurements $u(0.25)=0.2$, $u(0.5)=0.45$, $u(0.75)=0.7$, with regularization parameter $\alpha=0.01$ and prior $a_0=b_0=1$, the numerical solution gives approximately

$$a \approx 0.8595, \qquad b \approx 1.1094,$$

so

$$\kappa_1 = 1/a \approx 1.1635, \qquad \kappa_2 = 1/b \approx 0.9014.$$ 

The predicted temperatures are then

$$u(0.25) \approx 0.2183, \qquad u(0.5) \approx 0.4365, \qquad u(0.75) \approx 0.7183,$$

showing that regularization produces a stable approximate fit to the noisy observations.

> Note: The exact normal equations depend on the chosen parameterization; this exercise emphasizes the construction of the objective and gradient rather than final numbers.

### Problem 2: Posterior covariance for a linear inverse problem

Let the forward operator be linear, $F(m)=A m$, with Gaussian prior $m\sim \mathcal{N}(m_0,\mathcal{C})$ and Gaussian noise $\eta\sim \mathcal{N}(0,\Gamma)$. Derive the posterior mean and covariance for the Bayesian inverse problem.

#### Solution

The posterior is Gaussian with

- posterior covariance:

$$\mathcal{C}_{\text{post}} = \left(A^T \Gamma^{-1} A + \mathcal{C}^{-1}\right)^{-1},$$

- posterior mean:

$$m_{\text{post}} = \mathcal{C}_{\text{post}} \left(A^T \Gamma^{-1} d + \mathcal{C}^{-1} m_0\right).$$

This follows from completing the square in the exponent of the Gaussian posterior density. In PDE inverse problems, $A$ is the discretized forward map from $m$ to data.

#### 2.1 Bayesian posterior sampling for source inversion

A concrete Bayesian treatment of the Poisson source inversion problem can be obtained by discretizing the source field in a low-dimensional basis. Suppose $s \in \mathbb{R}^3$ is the vector of source coefficients, the prior is $s\sim \mathcal{N}(s_0, \mathcal{C})$, and the data model is

$$d = A s + \eta, \qquad \eta\sim\mathcal{N}(0,\Gamma).$$

Then the posterior is Gaussian with mean $s_{\text{post}}$ and covariance $\mathcal{C}_{\text{post}}$:

$$\mathcal{C}_{\text{post}} = (A^T \Gamma^{-1} A + \mathcal{C}^{-1})^{-1}, \qquad s_{\text{post}} = \mathcal{C}_{\text{post}}(A^T \Gamma^{-1} d + \mathcal{C}^{-1} s_0).$$

For a small numerical example, let

$$A = [0.2,\;0.5,\;0.3], \qquad d = 0.8, \qquad \Gamma = 0.01, \qquad \mathcal{C} = 0.5 I_3, \qquad s_0 = [0,0,0]^T.$$ 

Then the posterior mean and covariance are

$$s_{\text{post}} \approx [0.4,\;1.0,\;0.6]^T,$$
$$\mathcal{C}_{\text{post}} \approx \begin{bmatrix}0.45 & -0.125 & -0.075 \\
-0.125 & 0.1875 & -0.1875 \\
-0.075 & -0.1875 & 0.3875\end{bmatrix}.$$ 

A Metropolis-Hastings sampler for this posterior can be written in pseudo-code as:

```python
initialize s = s_0
for k in 1..N:
    s_prop = s + \epsilon,  # Gaussian random walk proposal
    loglik_prop = -0.5*(d - A@s_prop)**2 / Gamma
    logprior_prop = -0.5*(s_prop - s_0)^T C^{-1} (s_prop - s_0)
    logpost_prop = loglik_prop + logprior_prop
    accept_prob = min(1, exp(logpost_prop - logpost))
    if rand() < accept_prob:
        s = s_prop
    record s
```

For this numerical example, the sampler explores posterior source configurations around $[0.4,1.0,0.6]^T$ with covariance given above. In a PDE setting, $A$ would be assembled from the discretized forward solver and the likelihood evaluation would involve solving the Poisson equation for each proposed $s$.

A more advanced choice is NUTS (No-U-Turn Sampler), which uses gradients of the log posterior with respect to $s$ to generate efficient proposals. In practice, NUTS is preferable for higher-dimensional discretized source fields because it reduces random-walk behavior and improves mixing.

#### 2.2 Concrete Bayesian inversion example at $x=0.5$

To make the Bayesian update more concrete, consider the scalar source value at $x=0.5$ in Example 2. Suppose the prior mean is $m_0 = 0$, the prior variance is $\mathcal{C} = 1.0$, the noise variance is $\Gamma = 0.1$, and the data is $d = 1.0$ at $x=0.5$. Using a simple direct observation model for the source coefficient, the posterior is

$$\mathcal{C}_{\text{post}} = \left( \mathcal{C}^{-1} + \Gamma^{-1} \right)^{-1}, \qquad m_{\text{post}} = \mathcal{C}_{\text{post}} \Gamma^{-1} d.$$ 

Here $\alpha = \Gamma^{-1} = 10$ is the noise precision. With these numbers,

$$\mathcal{C}_{\text{post}} = \left(1 + 10\right)^{-1} = 0.0909, \qquad m_{\text{post}} = 0.0909 \cdot 10 \cdot 1.0 = 0.909.$$

If instead the effective prior variance for the discretized source coefficient is $0.4$ and the noise variance remains $0.1$, then the update becomes

$$\mathcal{C}_{\text{post}} = \frac{0.4 \cdot 0.1}{0.4+0.1} = 0.04, \qquad m_{\text{post}} = \frac{0.4}{0.4+0.1} \cdot 1.0 = 0.8.$$ 

This illustrates that posterior mean and variance depend both on prior covariance and on the noise precision through $\alpha = 1/\Gamma$.

### Problem 3: Ill-posedness and singular values

Consider a discrete inverse problem with measurement matrix $A \in \mathbb{R}^{M\times N}$ and data vector $d$. Explain why small singular values of $A$ amplify noise in the least-squares solution, and show how Tikhonov regularization modifies the singular value filter factors.

#### Solution

The least-squares solution with pseudoinverse is

$$m_{\text{LS}} = A^{\dagger} d = V \Sigma^{-1} U^T d,$$

where $A = U\Sigma V^T$ is the SVD. If $d$ contains noise, components corresponding to small singular values $\sigma_i$ are amplified by $1/\sigma_i$, causing instability.

Tikhonov solution is

$$m_{\alpha} = (A^T A + \alpha I)^{-1} A^T d = V D V^T A^T d,$$

with filter factors

$$D_{ii} = \frac{\sigma_i}{\sigma_i^2 + \alpha}. $$

When $\sigma_i \ll \sqrt{\alpha}$, the factor is small and the noisy components are damped. Thus regularization controls the contribution of poorly determined modes.

## 4. Connections

### 4.1 Connection to optimization theory

Inverse problems governed by PDEs are optimization problems with infinite-dimensional constraints. The Lagrange multiplier framework from Week 2 is essential:

- The PDE constraint is enforced by an adjoint variable, analogous to a multiplier for equality constraints.
- The adjoint equation arises from stationarity with respect to the state variable.
- The gradient with respect to the parameter uses the adjoint state to avoid explicit differentiation of the PDE solution operator.

For example, the reduced gradient formula

$$\nabla_m J(m) = \partial_m \mathcal{L}(u(m),m,p(m))$$

is identical in structure to constrained optimization gradient formulas in the finite-dimensional case.

In Week 2, the Lagrange multiplier method introduced the idea of enforcing constraints by augmenting the objective with a multiplier term

$$L(x,\lambda) = f(x) + \lambda^T g(x).$$

In the PDE-constrained inverse problem, the infinite-dimensional analogue is

$$L(u,m,p) = J(u,m) + \int_\Omega p\,(A(m;u)-f)\,dx,$$

where the adjoint variable $p(x)$ plays the role of the Lagrange multiplier. The adjoint condition is therefore the continuous version of the first-order stationarity condition $\nabla_x L(x,\lambda)=0$.

Beyond first-order conditions, second-order concepts such as Hessians and Gauss-Newton approximations are used for nonlinear inverse problems. The Gauss-Newton method approximates the Hessian by dropping second-order state-dependence terms, giving a computationally tractable optimization scheme.

### 4.2 Connection to statistical learning / Gaussian processes

Inverse problems and statistical learning share the core idea of inferring functions from data under uncertainty.

- Gaussian process regression is a Bayesian inference method for functions, using a prior covariance kernel and data likelihood.
- PDE-constrained inverse problems can be viewed as learning a function $m(x)$ with a prior on a function space and a likelihood induced by the PDE.
- The prior covariance $\mathcal{C}$ in the Bayesian inverse problem is analogous to the kernel in Gaussian process regression.

In particular, the posterior mean of a linear-Gaussian inverse problem is a kernel-based estimate, and the posterior covariance quantifies uncertainty the same way a Gaussian process does. When the forward operator is a PDE solver, the inverse problem may be seen as Gaussian process regression with PDE-informed features.

### 4.3 Connection to numerical linear algebra

Numerical linear algebra underpins solution methods and regularization strategies for inverse problems.

- Singular value decomposition (SVD) reveals the ill-conditioning of the discrete forward operator. Small singular values correspond to directions in parameter space that are weakly informed by the data.
- Regularization (Tikhonov, truncated SVD, iterative regularization) is a stabilization technique to control amplification of noise in the inverse.
- Krylov subspace methods, preconditioning, and low-rank approximations are essential for large-scale PDE-constrained inverse problems.

For PDE discretizations, the forward map often has a compact structure in the continuous limit and a rapidly decaying singular spectrum. Identifying and filtering those directions is the key numerical linear algebra insight.

## 5. Gaps in Alexanderian's coverage

Alexanderian's textbook is strong on the functional-analytic foundations of PDE inverse problems and adjoint-based optimization. Important frontiers that may be underemphasized or absent include:

- Deep learning / Physics-Informed Neural Networks (PINNs) for inverse problems
  - Modern approaches use neural networks to represent unknown fields and enforce PDE constraints with penalty terms or augmented Lagrangian methods. PINNs are especially attractive when data are scarce and one wants mesh-free solution representations.

- Real-time inversion
  - Fast algorithms for real-time or streaming data inversion require model reduction, online sequential Bayesian updating, and low-latency solvers. This is a practical direction for control and digital twins.

- Multi-fidelity methods
  - Combining models at different levels of accuracy (coarse PDE discretizations, surrogate models, reduced bases) can dramatically reduce cost in Bayesian inversion and optimization.

- Uncertainty quantification for nonlinear PDEs
  - Nonlinear inverse problems produce non-Gaussian posteriors and may require advanced sampling (MCMC, sequential Monte Carlo), polynomial chaos, and transport maps. Alexanderian often focuses on Gaussian approximations and linearized uncertainty.

#### Specific research questions

- Q1: Can PINNs outperform adjoint-based methods when the forward PDE is expensive to solve?
- Q2: How can multi-fidelity Monte Carlo reduce variance in Bayesian inversion?
- Q3: What is the impact of model discretization error on posterior uncertainty?

These gaps identify where future study can extend the classical inverse problem framework toward current research trends.

---

### Further reading suggestions

- A. Alexanderian, "A computational framework for PDE-constrained inverse problems." 
- M. B. Giles and E. Süli, "Adjoint Methods for PDEs".
- J. Kaipio and E. Somersalo, "Statistical and Computational Inverse Problems: A Bayesian Approach." Springer, 2005.
- A. M. Stuart, "Inverse problems: A Bayesian perspective," Acta Numerica, vol. 19, pp. 451–559, 2010.
- M. Raissi, P. Perdikaris, and G. E. Karniadakis, "Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations," Journal of Computational Physics, vol. 378, pp. 686–707, 2019.

## Software Recommendations

- `hIPPYlib`: Best for adjoint-based PDE-constrained inversion and automated gradient/Hessian computation.
- `CUQIpy`: Best for Bayesian inverse problems with a strong probabilistic modeling workflow.
- `FEniCS` or `deal.II`: Best for flexible finite element PDE solvers used in forward and inverse simulations.
- `PyMC` or `Stan`: Best for general-purpose MCMC and posterior sampling when the model is not too expensive.

## Common Pitfalls

- Mistake 1: Ignoring the adjoint equation derivation. Without the adjoint, the gradient with respect to the parameter is incorrect or incomplete; always derive the adjoint from the Lagrangian before computing parameter updates.
- Mistake 2: Using the same regularization parameter for all problems. Regularization must be tuned problem by problem, e.g. via the L-curve or the discrepancy principle, because the optimal $\alpha$ depends on data noise and model sensitivity.
- Mistake 3: Confusing MAP estimate with the full posterior. The MAP is a single best-fit point, while the full posterior characterizes uncertainty; in nonlinear problems the MAP can be misleading if the posterior is skewed or multimodal.

## Key Takeaways

- PDE-constrained inverse problems are solved by coupling a data misfit objective with the PDE via adjoint-based Lagrangians.
- Deterministic Tikhonov regularization gives a stable point estimate, while Bayesian inversion gives a full posterior distribution.
- The adjoint variable is the infinite-dimensional analogue of a Lagrange multiplier from Week 2.
- Numerical linear algebra, especially SVD and regularization, explains why inverse problems are ill-posed and how to stabilize them.
- Modern research gaps include PINNs, real-time inversion, multi-fidelity Bayesian methods, and quantitative uncertainty for nonlinear PDEs.