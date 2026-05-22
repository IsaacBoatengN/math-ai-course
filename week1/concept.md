# Hilbert Spaces: Infinite‑Dimensional Geometry for Functional Analysis

## Motivation

In finite‑dimensional Euclidean spaces $\mathbb{R}^n$, we have both a norm (distance) and an inner product (angles, orthogonality). Hilbert spaces generalize these concepts to infinite dimensions, providing the natural setting for quantum mechanics, signal processing, and partial differential equations.

## Definition of Inner Product Space

Let $X$ be a linear space over $\mathbb{C}$ (or $\mathbb{R}$). An **inner product** is a mapping $\langle \cdot, \cdot \rangle : X \times X \to \mathbb{C}$ satisfying:

1. **Linearity in the first argument:**  
   $\langle \alpha x + \beta y, z \rangle = \alpha \langle x, z \rangle + \beta \langle y, z \rangle$ for all $x,y,z \in X$, $\alpha,\beta \in \mathbb{C}$.
2. **Conjugate symmetry:** $\langle x, y \rangle = \overline{\langle y, x \rangle}$.
3. **Positive definiteness:** $\langle x, x \rangle \ge 0$, and $\langle x, x \rangle = 0$ iff $x = 0$.

A vector space with an inner product is called an **inner product space**. The natural norm induced by the inner product is given by

$$ \|x\| = \sqrt{\langle x, x \rangle}. $$

For example, $\ell^2 = \{ (x_n)_{n=1}^\infty \mid \sum_{n=1}^\infty |x_n|^2 < \infty \}$ with $\langle x, y \rangle = \sum_{n=1}^\infty x_n \overline{y_n}$ is an inner product space.

## Hilbert Space Definition

A **Hilbert space** is an inner product space that is **complete** with respect to the induced norm. Completeness means every Cauchy sequence converges to a point inside the space. $\ell^2$ and $L^2(\mathbb{R})$ (square‑integrable functions) are Hilbert spaces.

## Key Difference: Banach vs. Hilbert

A Banach space is a complete normed space, but not every norm comes from an inner product. The parallelogram law identifies Hilbert spaces:

$$ \|x+y\|^2 + \|x-y\|^2 = 2(\|x\|^2 + \|y\|^2). $$

The sequence space $\ell^p$ with $p \neq 2$ satisfies the triangle inequality but violates the parallelogram law; hence $\ell^p$ (for $p\neq 2$) is Banach but not Hilbert.

## Riesz Representation Theorem

Every **bounded linear functional** $f$ on a Hilbert space $H$ can be represented uniquely via the inner product with a fixed vector $z \in H$:

$$ f(x) = \langle x, z \rangle \quad \forall x \in H. $$

Moreover, $\|f\| = \|z\|$. This theorem identifies the dual space $H'$ with $H$ itself, a property that fails for general Banach spaces.

### Immediate Consequence

If $x_1 \neq x_2$ in $H$, there exists a bounded linear functional $f$ such that $f(x_1) \neq f(x_2)$ (the Hahn–Banach corollary, but in Hilbert spaces we can construct $f$ explicitly using the inner product).

## Importance

Hilbert spaces are the foundation of:
- **Quantum mechanics** (state vectors in $L^2$)
- **Wavelet theory** and **signal processing**
- **Partial differential equations** (weak solutions in Sobolev spaces)
- **Machine learning** (reproducing kernel Hilbert spaces)

Understanding Hilbert space geometry is essential for advanced functional analysis and its applications.
