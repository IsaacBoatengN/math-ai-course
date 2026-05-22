---
marp: true
---

# Hilbert Spaces: Inner Products, Completeness & Riesz

Functional Analysis – Week 1

---

## Inner Product Spaces & Hilbert Spaces

- Inner product: linearity, conjugate symmetry, positive definiteness  
  Norm: $\|x\| = \sqrt{\langle x, x \rangle}$  
- Hilbert space = complete inner product space (Cauchy sequences converge)  
- Parallelogram law:  
  $\|x+y\|^2 + \|x-y\|^2 = 2(\|x\|^2 + \|y\|^2)$ (holds iff norm comes from inner product)

---

## Banach vs. Hilbert

- Banach space = complete normed space (norm may not come from inner product)
- Example: $\ell^p$ with $p \neq 2$ is Banach but **not** Hilbert (violates parallelogram law)
- Hilbert spaces preserve Euclidean geometry (angles, orthogonality) in infinite dimensions

---

## Riesz Representation Theorem (Display Equation)

> Every bounded linear functional $f$ on a Hilbert space $H$ can be written uniquely as:

$$ f(x) = \langle x, z \rangle \quad \forall x \in H $$

where $z \in H$ depends on $f$. Moreover, $\|f\| = \|z\|$.  
Thus $H' \cong H$ – a property false for general Banach spaces.

---

## Applications & Summary

- Quantum mechanics (state vectors in $L^2$)
- PDEs (weak solutions, Sobolev spaces)
- Machine learning (reproducing kernel Hilbert spaces)
- Signal processing (wavelets)

**Key takeaway:** Hilbert spaces bring geometry to analysis, and Riesz ties functionals to inner products.
