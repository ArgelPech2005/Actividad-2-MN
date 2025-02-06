"""   Autor:
   Argel Jesus Pech Manrique
   argelpech098@gmail.com
   Version 2.0 : 03/02/2025 00:50am
"""

from logging import error # Importa la función de error del módulo logging
import numpy as np # Importa la librería NumPy para operaciones numéricas
import matplotlib.pyplot as plt # Importa la librería Matplotlib para visualizar gráficos

# Definición de la función para aproximar pi utilizando la serie de Leibniz
def leibniz_pi(n):
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))

true_pi = np.pi # Valor verdadero de pi
N_values = [10, 100, 1000, 10000] # Valores de N a utilizar en la aproximación
errors_abs = [] # Lista para guardar los errores absolutos
errors_rel = [] # Lista para guardar los errores relativos
errors_cua = [] # Lista para guardar los errores cuadrados

# Bucle para calcular y guardar los errores para cada valor de N
for N in N_values:
    approx_pi = leibniz_pi(N) # Aproximación de pi usando la función de Leibniz
    error_abs = abs(true_pi - approx_pi) # Cálculo del error absoluto
    error_rel = error_abs / true_pi # Cálculo del error relativo
    error_cua = error_abs**2 # Cálculo del error cuadrático
    errors_abs.append(error_abs) # Guarda el error absoluto en la lista
    errors_rel.append(error_rel) # Guarda el error relativo en la lista
    errors_cua.append(error_cua) # Guarda el error cuadrático en la lista
    print(f"N={N}: Error absoluto={error_abs}, Error relativo={error_rel}, Error cuadrático={error_cua}")

# Crear la figura para el gráfico
plt.figure()
# Graficar los errores absolutos, relativos y cuadrados en función de N
plt.plot(N_values, errors_abs, label='Error absoluto', marker='o')
plt.plot(N_values, errors_rel, label='Error relativo', marker='s')
plt.plot(N_values, errors_cua, label='Error cuadrático', marker='^')
plt.xscale('log') # Escala logarítmica en el eje x
plt.yscale('log') # Escala logarítmica en el eje y
plt.xlabel('N') # Etiqueta del eje x
plt.ylabel('Error') # Etiqueta del eje y
plt.legend() # Mostrar leyenda
plt.title('Errores en la aproximación de pi') # Título del gráfico
plt.show() 