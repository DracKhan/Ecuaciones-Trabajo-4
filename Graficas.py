import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 0.5, 1000)

a0 = -2
a1 = 1
a2 = 12
a3 = -104/3
a4 = 160/3
a5 = -288/5
a6 = 2176/45
a7 = -10496/315
a8 = 2048/105
a9 = -5632/567

# Solución exacta
y_exact = -2 * np.exp(-4*x) - 7*x * np.exp(-4*x)

# Soluciones por serie truncada
y_1_term = a0 * np.ones_like(x)
y_2_terms = a0 + a1*x
y_3_terms = y_2_terms + a2*x**2
y_5_terms = y_3_terms + a3*x**3 + a4*x**4
y_7_terms = y_5_terms + a5*x**5 + a6*x**6
y_10_terms = y_7_terms + a7*x**7 + a8*x**8 + a9*x**9

plt.style.use('default')
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (8, 6)

plt.figure(1)
plt.plot(x, y_1_term, 'b-', linewidth=2)
plt.title('Solución por Serie Truncada a 1 Término')
plt.xlabel('x'); plt.ylabel('y(x)'); plt.grid(True, alpha=0.3); plt.xlim(0, 0.5)

plt.figure(2)
plt.plot(x, y_2_terms, 'r-', linewidth=2)
plt.title('Solución por Serie Truncada a 2 Términos')
plt.xlabel('x'); plt.ylabel('y(x)'); plt.grid(True, alpha=0.3); plt.xlim(0, 0.5)

plt.figure(3)
plt.plot(x, y_3_terms, 'g-', linewidth=2)
plt.title('Solución por Serie Truncada a 3 Términos')
plt.xlabel('x'); plt.ylabel('y(x)'); plt.grid(True, alpha=0.3); plt.xlim(0, 0.5)

plt.figure(4)
plt.plot(x, y_5_terms, 'm-', linewidth=2)
plt.title('Solución por Serie Truncada a 5 Términos')
plt.xlabel('x'); plt.ylabel('y(x)'); plt.grid(True, alpha=0.3); plt.xlim(0, 0.5)

plt.figure(5)
plt.plot(x, y_7_terms, 'c-', linewidth=2)
plt.title('Solución por Serie Truncada a 7 Términos')
plt.xlabel('x'); plt.ylabel('y(x)'); plt.grid(True, alpha=0.3); plt.xlim(0, 0.5)

plt.figure(6)
plt.plot(x, y_exact, 'k-', linewidth=2)
plt.title('Solución Exacta por Ecuación Característica')
plt.xlabel('x'); plt.ylabel('y(x)'); plt.grid(True, alpha=0.3); plt.xlim(0, 0.5)

plt.figure(9)
plt.plot(x, y_10_terms, 'orange', linewidth=2)
plt.title('Solución por Serie Truncada a 10 Términos')
plt.xlabel('x'); plt.ylabel('y(x)'); plt.grid(True, alpha=0.3); plt.xlim(0, 0.5)

plt.figure(7)
plt.plot(x, y_exact, 'k-', linewidth=2.5, label='Solución exacta')
plt.plot(x, y_1_term, 'b--', linewidth=1.5, label='1 término')
plt.plot(x, y_2_terms, 'r--', linewidth=1.5, label='2 términos')
plt.plot(x, y_3_terms, 'g--', linewidth=1.5, label='3 términos')
plt.plot(x, y_5_terms, 'm--', linewidth=1.5, label='5 términos')
plt.plot(x, y_7_terms, 'c--', linewidth=1.5, label='7 términos')
plt.plot(x, y_10_terms, 'orange', linewidth=1.5, linestyle='--', label='10 términos')
plt.title('Comparación: Solución Exacta vs Series Truncadas')
plt.xlabel('x'); plt.ylabel('y(x)'); plt.legend(); plt.grid(True, alpha=0.3); plt.xlim(0, 0.5)

x_long = np.linspace(0, 1.5, 1000)
y_exact_long = -2 * np.exp(-4*x_long) - 7*x_long * np.exp(-4*x_long)
y_1_term_long = a0 * np.ones_like(x_long)
y_2_terms_long = a0 + a1*x_long
y_3_terms_long = y_2_terms_long + a2*x_long**2
y_5_terms_long = y_3_terms_long + a3*x_long**3 + a4*x_long**4
y_7_terms_long = y_5_terms_long + a5*x_long**5 + a6*x_long**6
y_10_terms_long = y_7_terms_long + a7*x_long**7 + a8*x_long**8 + a9*x_long**9

plt.figure(10)
plt.plot(x_long, y_exact_long, 'k-', linewidth=2.5, label='Solución exacta')
plt.plot(x_long, y_1_term_long, 'b--', linewidth=1.5, label='1 término')
plt.plot(x_long, y_2_terms_long, 'r--', linewidth=1.5, label='2 términos')
plt.plot(x_long, y_3_terms_long, 'g--', linewidth=1.5, label='3 términos')
plt.plot(x_long, y_5_terms_long, 'm--', linewidth=1.5, label='5 términos')
plt.plot(x_long, y_7_terms_long, 'c--', linewidth=1.5, label='7 términos')
plt.plot(x_long, y_10_terms_long, 'orange', linewidth=1.5, linestyle='--', label='10 términos')
plt.title('Comparación extendida: Solución Exacta vs Series Truncadas')
plt.xlabel('x'); plt.ylabel('y(x)'); plt.legend(); plt.grid(True, alpha=0.3); plt.xlim(0, 1.5)

plt.tight_layout()
plt.show()
