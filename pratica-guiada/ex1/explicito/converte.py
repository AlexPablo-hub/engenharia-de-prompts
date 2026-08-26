#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
converte.py - Conversor de temperatura entre Celsius, Fahrenheit e Kelvin.

Uso:
    python converte.py <valor> <unidade_origem> <unidade_destino>

Exemplo:
    python converte.py 100 C F
    -> 212.0

Unidades aceitas (não diferencia maiúsculas/minúsculas):
    C - Celsius
    F - Fahrenheit
    K - Kelvin

Este script usa apenas a biblioteca padrão do Python. O foco principal
é a validação de entrada (formato numérico, unidade e limite físico do
zero absoluto), não o cálculo em si, que é trivial.
"""

import sys

# Unidades reconhecidas pelo programa.
UNIDADES_VALIDAS = ("C", "F", "K")

# Valor do zero absoluto expresso em cada uma das unidades suportadas.
# Serve para recusar temperaturas fisicamente impossíveis.
ZERO_ABSOLUTO = {
    "C": -273.15,
    "F": -459.67,
    "K": 0.0,
}


def erro(mensagem: str) -> None:
    """Imprime uma mensagem de erro em stderr e encerra o programa (código 1).

    Centralizar a saída de erro aqui garante que toda falha de validação
    termine o programa da mesma forma, o que facilita testar e ler o código.
    """
    print(f"Erro: {mensagem}", file=sys.stderr)
    sys.exit(1)


def validar_unidade(unidade: str) -> str:
    """Confere se `unidade` é uma das unidades suportadas.

    Aceita minúsculas ou maiúsculas (ex.: "c" e "C" são equivalentes).
    Se a unidade não existir, o programa é encerrado com uma mensagem
    que lista as unidades válidas, conforme exigido no enunciado.
    """
    unidade_normalizada = unidade.strip().upper()
    if unidade_normalizada not in UNIDADES_VALIDAS:
        erro(
            f"unidade '{unidade}' desconhecida. "
            f"Unidades válidas: {', '.join(UNIDADES_VALIDAS)} "
            "(C = Celsius, F = Fahrenheit, K = Kelvin)."
        )
    return unidade_normalizada


def validar_valor(valor_texto: str) -> float:
    """Converte o texto recebido para float, validando o formato numérico.

    Qualquer texto que não represente um número (ex.: "abc", "10,5")
    é rejeitado com uma mensagem clara em vez de deixar o Python
    lançar um ValueError "cru" para o usuário.
    """
    try:
        return float(valor_texto)
    except ValueError:
        erro(
            f"'{valor_texto}' não é um número válido. "
            "Use ponto como separador decimal, ex.: 36.5"
        )


def validar_fisicamente(valor: float, unidade: str) -> None:
    """Garante que `valor` não está abaixo do zero absoluto na `unidade` dada.

    O zero absoluto é o limite físico mais baixo possível de temperatura;
    qualquer valor menor que isso é inválido, independentemente da escala
    em que foi informado.
    """
    minimo = ZERO_ABSOLUTO[unidade]
    if valor < minimo:
        erro(
            f"{valor} {unidade} está abaixo do zero absoluto "
            f"({minimo} {unidade}). Essa temperatura não existe fisicamente."
        )


def para_celsius(valor: float, unidade: str) -> float:
    """Converte um valor de qualquer unidade suportada para Celsius.

    Celsius é usado aqui como unidade intermediária: toda conversão
    passa primeiro por Celsius e depois vai para a unidade de destino.
    Isso evita ter que escrever uma fórmula para cada um dos 6 pares
    possíveis de conversão.
    """
    if unidade == "C":
        return valor
    if unidade == "F":
        return (valor - 32) * 5 / 9
    if unidade == "K":
        return valor - 273.15
    raise ValueError(f"unidade não suportada: {unidade}")


def de_celsius(valor_celsius: float, unidade: str) -> float:
    """Converte um valor em Celsius para a unidade de destino solicitada."""
    if unidade == "C":
        return valor_celsius
    if unidade == "F":
        return valor_celsius * 9 / 5 + 32
    if unidade == "K":
        return valor_celsius + 273.15
    raise ValueError(f"unidade não suportada: {unidade}")


def converter(valor: float, origem: str, destino: str) -> float:
    """Converte `valor` de `origem` para `destino`, passando por Celsius."""
    valor_em_celsius = para_celsius(valor, origem)
    return de_celsius(valor_em_celsius, destino)


def main(argumentos: list) -> None:
    if len(argumentos) != 3:
        erro(
            "número de argumentos inválido.\n"
            "Uso: python converte.py <valor> <unidade_origem> <unidade_destino>\n"
            "Exemplo: python converte.py 100 C F\n"
            f"Unidades válidas: {', '.join(UNIDADES_VALIDAS)} "
            "(C = Celsius, F = Fahrenheit, K = Kelvin)."
        )

    valor_texto, origem_texto, destino_texto = argumentos

    valor = validar_valor(valor_texto)
    origem = validar_unidade(origem_texto)
    destino = validar_unidade(destino_texto)
    validar_fisicamente(valor, origem)

    resultado = converter(valor, origem, destino)
    print(round(resultado, 2))


if __name__ == "__main__":
    main(sys.argv[1:])
