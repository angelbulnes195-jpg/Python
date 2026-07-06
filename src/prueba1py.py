gravedad = 9.8
tiempo = 2
velocidad_inicial_y = 25  


posicion_y = (velocidad_inicial_y * tiempo) - (0.5 * gravedad * (tiempo ** 2))

print("--- RESULTADO DE LA SIMULACIÓN ---")
print(f"A los {tiempo} segundos, la altura del proyectil es: {posicion_y} metros.")
