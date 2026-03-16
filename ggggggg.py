notas = []
notas.append(5)
print(notas)
[5]
notas.append(7)
[5, 7]
notas.append(9)
print(notas)
[5, 7, 9]
notas.append(10)
print(notas)
[5, 7, 9, 10]
notas[0] = 10
print(notas)
[10, 7, 9, 10]

# Exemplo prático
v1, v2, v3, v4 = 5, 7, 9, 10  # Valores (notas)
p1, p2, p3, p4 = 1, 2, 2, 2    # Pesos
media_ponderada = (v1 * p1 + v2 * p2 + v3 * p3 + v4 * p4) / (p1 + p2 + p3 + p4)
print(media_ponderada) # Resultado
print(f'{media_ponderada:.2f}')

