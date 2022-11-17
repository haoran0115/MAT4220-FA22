# MAT4220 FA22 Notes

## Chapter 6
### Series solution on rectangles
Consider following equation on $\Omega=(0, a)\times(0, b)$.
$$
\begin{cases}
    \Delta u &= 0\\
    \Delta &= \partial_x^2 + \partial_y^2
\end{cases}
$$

Let $u(x,y)=X(x)Y(y)$, then

$$
X''Y + Y''X = 0\quad
\frac{X''}{X} = -\frac{Y''}{Y} = -\lambda
$$

**Example:** $\Omega=(0, a)\times(0, b)\times(0, c)$ on 3-D. Take Dirichlet boundary condition on the cube,

$$
u(\pi, y, z) = g(y, z)\quad
u(0, y, z) = u(x, 0, z) = u(x, \pi, z) = u(x, y, 0) = u(x, y, \pi) = 0\\
\frac{X''}{X} + \frac{Y''}{Y} + \frac{Z''}{Z} = 0\quad
X(0) = Y(0) = Y(\pi) = Z(0) = Z(\pi) = 0\\
$$

Then

$$
Y(y) = \sin my\quad Z(z) = \sin nz
\Rightarrow X''(x) = (m^2+n^2)X(x),\
X(x) = A\sinh(\sqrt{m^2+n^2} x) + B\cosh(\sqrt{m^2+n^2}x)
$$

Since $X(x)=0$, we have $X(x)=A\sinh(\sqrt{m^2+n^2}x)$.
Summing up the solution

$$
u(x, y, z) = \sum_{n=1}^\infty\sum_{m=1}^\infty
A_{nm}\sinh(\sqrt{m^2+n^2}x)\sin my \sin nz
$$

### Disk domain, Poisson's formula
$D_a={r^2 < a^2}$, $U(r,\theta)=u(x(r,\theta), y(r, \theta))$.
Let $U(r,\theta) = R(r)\Theta(\theta)$, then

$$
R''\Theta + \frac{1}{r}R'\Theta + \frac{1}{r^2}R\Theta'' = 0
\Rightarrow
-\frac{r^2R'' + rR'}{R} = \frac{\Theta''}{\Theta} = -\lambda
$$

Periodic boundary condition

$$
\begin{cases}
    U(r,\theta) &= U(r, \theta+2\pi)\\
    \partial_\theta U(r, \theta) &= 
    \partial_\theta U(r, \theta+2\pi)
\end{cases}
$$

Choose $\theta_0=0$, then

$$
\Theta'' + \lambda\Theta = 0\quad
\Theta(0) = \Theta(2\pi)\quad
\Theta'(0) = \Theta'(2\pi)
\Rightarrow
\Theta_n = A_n\cos(n\theta) + B_n\sin(n\theta),
\lambda_n = n^2
$$

Regarding $R_n$, we have a Euler type ODE of $R$.

$$
r^2R'' + rR' = \lambda R = n^2R
$$

Suppose $R=r^\alpha$, then we get $\alpha^2=n^2$, which means $\alpha=\pm n$.
Hence if $n>0$, we have

$$
R_n(r) = C_nr^n + D_nr^{-n}
$$

If $n=0$, we have 

$$
R_0(r) = C_1\ln r + D_1
$$

Ignoring $\ln r$ and $r^{-n}$ terms, set boundary condition $U(a, \theta) =     h(\theta)$, then

$$
h(\theta) = \frac{A_0}{2} + \sum_{n=1}^\infty
(A_n\cos(n\theta) + B_n\sin(n\theta))a^n
$$

with

$$
\begin{aligned}
    A_n &= \frac{1}{a^n}\frac{1}{\pi}\int_0^{2\pi}h(\phi)\cos(n\phi)\mathrm{d}\phi\\
    B_n &= \frac{1}{a^n}\frac{1}{\pi}\int_0^{2\pi}h(\phi)\sin(n\phi)\mathrm{d}\phi\\
\end{aligned}
$$

Note that for $n=0,1,\dots$

$$
I_n = A_n\cos(n\theta) + B_n\sin(n\theta) = 
\frac{1}{\pi a^n}\int_0^{2\pi}h(\phi)
[\cos(n\phi) \cos(n\phi) + \sin(n\phi)\sin(n\phi)]\mathrm{d}\phi
= \frac{1}{\pi a^n}\int_0^{2\pi} h(\phi)\cos(n(\phi-\theta))\mathrm{d}\phi
$$


Therefore 

$$
h(\theta) = \frac{A_0}{2} + \sum_{n=0}^\infty
I_na^n\quad
U(r, \theta) = \frac{A_0}{2} + \sum_{n=0}^\infty
I_n r^n
= 
\frac{1}{2\pi}\int_0^{2\pi}h(\phi)
\left[
1 + 2\sum_{n=1}^\infty \cos(n(\phi-\theta))r^n
\right]\mathrm{d}\phi
$$

By calculating the geometric series, we can further simplify the expression to Poisson's formula

$$
U(r, \theta) = \frac{a^2-r^2}{2\pi}\int_0^{2\pi}
\frac{h(\phi)}{a^2 - 2ar\cos(\theta-\phi) + r^2}\mathrm{d}\phi
= \frac{1}{2\pi}\int_0^{2\pi}P_a(\theta-\phi, r)h(\phi)\mathrm{d}\phi
$$

Geometric interpretation: let $\mathbf{x}=(r,\theta)$, $\mathbf{x}'=(a,\phi)$, we have $u(r,\theta)=u(\mathbf{x})$ in the form of

$$
u(\mathbf{x}) = 
\frac{a^2 - |\mathbf{x}|^2}{2\pi a}\int_{\partial D_a}
\frac{u(\mathbf{x}')}{|\mathbf{x}-\mathbf{x}'|^2}\mathrm{d}s'
$$

where $s'= a\phi$, which is the arc length.

*Theorem.* If $u(x) = h(\phi)$ on $\partial D_a$ is continuous, then Poission's formula provides the only harmonic function in $D_a$ for which 

$$
\lim_{\mathbf{x}\rightarrow\mathbf{x}_0} = h(\mathbf{x}_0)
\quad \forall \mathbf{x}_0\in D_a
$$

This means $u(\mathbf{x})$ is a continuous function on $\bar{D_a}$.

