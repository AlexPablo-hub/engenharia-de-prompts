from media_ponderada import media_ponderada

# Caso 1: valor esperado 8.1
resultado1 = media_ponderada([8, 7, 9], [3, 3, 4])
print(f"Caso 1 -> resultado={resultado1!r}, esperado=8.1, ok={resultado1 == 8.1}")

# Caso 2: tamanhos diferentes devem levantar ValueError
try:
    media_ponderada([8, 7, 9], [3, 3])
    print("Caso 2 -> FALHOU: nao levantou ValueError")
except ValueError as e:
    print(f"Caso 2 -> OK: ValueError levantado ({e})")
except Exception as e:
    print(f"Caso 2 -> FALHOU: excecao errada levantada: {type(e).__name__}: {e}")

# Caso 3: soma dos pesos igual a zero deve levantar ValueError
try:
    media_ponderada([8, 7, 9], [1, -1, 0])
    print("Caso 3 -> FALHOU: nao levantou ValueError")
except ValueError as e:
    print(f"Caso 3 -> OK: ValueError levantado ({e})")
except Exception as e:
    print(f"Caso 3 -> FALHOU: excecao errada levantada: {type(e).__name__}: {e}")
