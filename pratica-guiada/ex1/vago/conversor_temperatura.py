"""
Conversor de Temperatura
=========================

Converte valores entre Celsius (C), Fahrenheit (F) e Kelvin (K).

Uso:
    python conversor_temperatura.py

O programa e interativo: pede um valor numerico e a unidade de origem,
e mostra o resultado convertido para as outras duas unidades.

Digite "sair" a qualquer momento para encerrar o programa.
"""

ZERO_ABSOLUTO_C = -273.15
ZERO_ABSOLUTO_F = -459.67
ZERO_ABSOLUTO_K = 0.0

UNIDADES_VALIDAS = ("C", "F", "K")


# ---------------------------------------------------------------------------
# Funcoes de conversao
# ---------------------------------------------------------------------------

def celsius_para_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32


def celsius_para_kelvin(c: float) -> float:
    return c + 273.15


def fahrenheit_para_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


def fahrenheit_para_kelvin(f: float) -> float:
    return celsius_para_kelvin(fahrenheit_para_celsius(f))


def kelvin_para_celsius(k: float) -> float:
    return k - 273.15


def kelvin_para_fahrenheit(k: float) -> float:
    return celsius_para_fahrenheit(kelvin_para_celsius(k))


def converter(valor: float, unidade_origem: str) -> dict:
    """Converte 'valor' (na unidade_origem) para as outras duas unidades.

    Retorna um dicionario {"C": ..., "F": ..., "K": ...} contendo tambem
    o proprio valor de origem, para facilitar a exibicao.
    """
    unidade_origem = unidade_origem.upper()

    if unidade_origem == "C":
        return {
            "C": valor,
            "F": celsius_para_fahrenheit(valor),
            "K": celsius_para_kelvin(valor),
        }
    elif unidade_origem == "F":
        return {
            "C": fahrenheit_para_celsius(valor),
            "F": valor,
            "K": fahrenheit_para_kelvin(valor),
        }
    elif unidade_origem == "K":
        return {
            "C": kelvin_para_celsius(valor),
            "F": kelvin_para_fahrenheit(valor),
            "K": valor,
        }
    else:
        raise ValueError(f"Unidade desconhecida: {unidade_origem}")


# ---------------------------------------------------------------------------
# Validacao de entrada
# ---------------------------------------------------------------------------

def validar_valor_fisico(valor: float, unidade: str) -> None:
    """Lanca ValueError se o valor for fisicamente impossivel
    (abaixo do zero absoluto) para a unidade informada.
    """
    limites = {
        "C": ZERO_ABSOLUTO_C,
        "F": ZERO_ABSOLUTO_F,
        "K": ZERO_ABSOLUTO_K,
    }
    limite = limites[unidade]
    if valor < limite:
        raise ValueError(
            f"Valor invalido: {valor} {unidade} esta abaixo do zero absoluto "
            f"({limite} {unidade}). Nao existe temperatura mais baixa que essa."
        )


def ler_valor(mensagem: str):
    """Pede um numero ao usuario. Retorna float, ou None se o usuario
    quiser sair. Repete a pergunta enquanto a entrada nao for valida.
    """
    while True:
        entrada = input(mensagem).strip()
        if entrada.lower() in ("sair", "exit", "quit", "q"):
            return None
        entrada_normalizada = entrada.replace(",", ".")
        try:
            return float(entrada_normalizada)
        except ValueError:
            print(
                f'  Entrada invalida: "{entrada}" nao e um numero. '
                'Use apenas digitos (ex: 25 ou 25.5). Tente novamente.'
            )


def ler_unidade(mensagem: str):
    """Pede uma unidade (C, F ou K) ao usuario. Retorna a letra em
    maiusculo, ou None se o usuario quiser sair.
    """
    while True:
        entrada = input(mensagem).strip()
        if entrada.lower() in ("sair", "exit", "quit", "q"):
            return None
        unidade = entrada.upper()
        if unidade in UNIDADES_VALIDAS:
            return unidade
        print(
            f'  Unidade invalida: "{entrada}". '
            'Digite C (Celsius), F (Fahrenheit) ou K (Kelvin).'
        )


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------

NOME_UNIDADE = {
    "C": "Celsius",
    "F": "Fahrenheit",
    "K": "Kelvin",
}


def executar():
    print("=" * 50)
    print("           CONVERSOR DE TEMPERATURA")
    print("=" * 50)
    print("Unidades suportadas: Celsius (C), Fahrenheit (F), Kelvin (K)")
    print('Digite "sair" a qualquer momento para encerrar.\n')

    while True:
        valor = ler_valor("Digite o valor da temperatura: ")
        if valor is None:
            break

        unidade_origem = ler_unidade(
            "Digite a unidade de origem (C/F/K): "
        )
        if unidade_origem is None:
            break

        try:
            validar_valor_fisico(valor, unidade_origem)
        except ValueError as erro:
            print(f"  {erro}\n")
            continue

        resultados = converter(valor, unidade_origem)

        print(f"\n  {valor:g} {NOME_UNIDADE[unidade_origem]} equivale a:")
        for unidade in UNIDADES_VALIDAS:
            if unidade == unidade_origem:
                continue
            print(f"    {resultados[unidade]:.2f} {NOME_UNIDADE[unidade]} ({unidade})")
        print()

    print("Encerrando o conversor de temperatura. Ate mais!")


if __name__ == "__main__":
    executar()
