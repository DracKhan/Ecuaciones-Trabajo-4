import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 0.5, 1000)

# Coeficientes de la serie de potencias
a0 = -2
a1 = 1
a2 = 12
a3 = -104/3
a4 = 160/3
a5 = -288/5
a6 = 2176/45
a7 = -5088/105
a8 = 76384/245

# Solución exacta
y_exact = -2 * np.exp(-4*x) - 7*x * np.exp(-4*x)

# Soluciones por serie truncada
y_1_term = a0 * np.ones_like(x)
y_2_terms = a0 + a1*x
y_3_terms = a0 + a1*x + a2*x**2
y_5_terms = a0 + a1*x + a2*x**2 + a3*x**3 + a4*x**4
y_7_terms = a0 + a1*x + a2*x**2 + a3*x**3 + a4*x**4 + a5*x**5 + a6*x**6

plt.style.use('default')
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (8, 6)

# Figura 1: 1 término
plt.figure(1)
plt.plot(x, y_1_term, 'b-', linewidth=2)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Solución por Serie Truncada a 1 Término')
plt.grid(True, alpha=0.3)
plt.xlim(0, 0.5)

# Figura 2: 2 términos
plt.figure(2)
plt.plot(x, y_2_terms, 'r-', linewidth=2)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Solución por Serie Truncada a 2 Términos')
plt.grid(True, alpha=0.3)
plt.xlim(0, 0.5)

# Figura 3: 3 términos
plt.figure(3)
plt.plot(x, y_3_terms, 'g-', linewidth=2)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Solución por Serie Truncada a 3 Términos')
plt.grid(True, alpha=0.3)
plt.xlim(0, 0.5)

# Figura 4: 5 términos
plt.figure(4)
plt.plot(x, y_5_terms, 'm-', linewidth=2)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Solución por Serie Truncada a 5 Términos')
plt.grid(True, alpha=0.3)
plt.xlim(0, 0.5)

# Figura 5: 7 términos
plt.figure(5)
plt.plot(x, y_7_terms, 'c-', linewidth=2)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Solución por Serie Truncada a 7 Términos')
plt.grid(True, alpha=0.3)
plt.xlim(0, 0.5)

# Figura 6: Solución exacta
plt.figure(6)
plt.plot(x, y_exact, 'k-', linewidth=2)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Solución Exacta por Ecuación Característica')
plt.grid(True, alpha=0.3)
plt.xlim(0, 0.5)

# Figura 7: Comparación sobrepuesta
plt.figure(7)
plt.plot(x, y_exact, 'k-', linewidth=2.5, label='Solución exacta')
plt.plot(x, y_1_term, 'b--', linewidth=1.5, label='1 término')
plt.plot(x, y_2_terms, 'r--', linewidth=1.5, label='2 términos')
plt.plot(x, y_3_terms, 'g--', linewidth=1.5, label='3 términos')
plt.plot(x, y_5_terms, 'm--', linewidth=1.5, label='5 términos')
plt.plot(x, y_7_terms, 'c--', linewidth=1.5, label='7 términos')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Comparación: Solución Exacta vs Series Truncadas')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 0.5)

plt.tight_layout()
plt.show()

# Figura 8: Comparación en un intervalo extendido
x_long = np.linspace(0, 1.5, 1000)

y_exact_long = -2 * np.exp(-4*x_long) - 7*x_long * np.exp(-4*x_long)
y_1_term_long = a0 * np.ones_like(x_long)
y_2_terms_long = a0 + a1*x_long
y_3_terms_long = a0 + a1*x_long + a2*x_long**2
y_5_terms_long = a0 + a1*x_long + a2*x_long**2 + a3*x_long**3 + a4*x_long**4
y_7_terms_long = a0 + a1*x_long + a2*x_long**2 + a3*x_long**3 + a4*x_long**4 + a5*x_long**5 + a6*x_long**6

plt.figure(8)
plt.plot(x_long, y_exact_long, 'k-', linewidth=2.5, label='Solución exacta')
plt.plot(x_long, y_1_term_long, 'b--', linewidth=1.5, label='1 término')
plt.plot(x_long, y_2_terms_long, 'r--', linewidth=1.5, label='2 términos')
plt.plot(x_long, y_3_terms_long, 'g--', linewidth=1.5, label='3 términos')
plt.plot(x_long, y_5_terms_long, 'm--', linewidth=1.5, label='5 términos')
plt.plot(x_long, y_7_terms_long, 'c--', linewidth=1.5, label='7 términos')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Comparación extendida: Solución Exacta vs Series Truncadas')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 1.5)

