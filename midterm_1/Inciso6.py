import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Datos en millones
Elementos = [5.09, 5.09 * 2, 5.09 * 3, 5.09 * 4, 5.09 * 5]  # Tamaños de las instancias en millones
ocurrencias_search = [5.09, 10.81, 15.27, 20.36, 25.45]  # Ocurrencias en millones
ocurrencias_pop = [0.000001, 0.000001, 0.000001, 0.000001, 0.000001]  # Ocurrencias en millones

plt.figure(figsize=(8, 5))
plt.plot(Elementos, ocurrencias_search, marker='o', linestyle='-', color='b', label='Search')
plt.plot(Elementos, ocurrencias_pop, marker='s', linestyle='--', color='r', label='Pop')

plt.xlabel("Elementos (millones)")
plt.ylabel("Ocurrencias (millones)")
plt.title("Comparación de Search y Pop")
plt.legend()
plt.grid(True)

plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:.1f}M'))

# Guardar la gráfica como PNG
plt.savefig("grafica.png", dpi=300)  # dpi=300 para mayor calidad

plt.show()
