"""
Soma a coluna "valor" de um arquivo CSV com colunas: data,produto,valor.

Usa apenas a biblioteca padrão do Python (csv, decimal, argparse, sys),
para poder rodar em servidores sem acesso à internet / sem permissão
para instalar pacotes (ex.: pandas).

Uso:
    python soma_valores.py caminho/para/arquivo.csv
    python soma_valores.py caminho/para/arquivo.csv --delimiter ";"

Formato de número aceito na coluna "valor":
    - "1234.56"   (ponto como separador decimal)
    - "1234,56"   (vírgula como separador decimal, padrão BR)
    - "1.234,56"  (ponto de milhar + vírgula decimal, padrão BR)
    - "R$ 1.234,56" (prefixo de moeda é ignorado)
"""

import argparse
import csv
import sys
from decimal import Decimal, InvalidOperation

COLUNAS_ESPERADAS = {"data", "produto", "valor"}


def parse_valor(valor_bruto: str) -> Decimal:
    """
    Converte uma string de valor monetário em Decimal.

    Decimal é usado (em vez de float) para evitar erros de arredondamento
    binário ao somar muitos valores monetários -- ver observação no
    relatório final sobre essa escolha.
    """
    texto = valor_bruto.strip()

    # Remove símbolos de moeda e espaços comuns.
    for simbolo in ("R$", "$", " "):
        texto = texto.replace(simbolo, "")

    if not texto:
        raise InvalidOperation("valor vazio")

    # Heurística para formato brasileiro (1.234,56) vs internacional (1234.56).
    if "," in texto and "." in texto:
        # Assume que o último separador é o decimal.
        if texto.rfind(",") > texto.rfind("."):
            texto = texto.replace(".", "").replace(",", ".")
        else:
            texto = texto.replace(",", "")
    elif "," in texto:
        # Só vírgula: trata como separador decimal (padrão BR).
        texto = texto.replace(",", ".")
    # Se só tiver ponto (ou nenhum separador), usa como está.

    return Decimal(texto)


def somar_csv(caminho: str, delimiter: str = ",") -> tuple[Decimal, int, list[str]]:
    """
    Lê o CSV e soma a coluna "valor".

    Retorna (total, quantidade_de_linhas_validas, lista_de_avisos).
    """
    total = Decimal("0")
    linhas_validas = 0
    avisos: list[str] = []

    with open(caminho, newline="", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=delimiter)

        if leitor.fieldnames is None:
            raise ValueError("Arquivo CSV vazio ou sem cabeçalho.")

        colunas_encontradas = {c.strip() for c in leitor.fieldnames}
        faltando = COLUNAS_ESPERADAS - colunas_encontradas
        if faltando:
            raise ValueError(
                f"Colunas obrigatórias ausentes no CSV: {sorted(faltando)}. "
                f"Colunas encontradas: {sorted(colunas_encontradas)}"
            )

        for numero_linha, linha in enumerate(leitor, start=2):  # linha 1 = cabeçalho
            valor_bruto = linha.get("valor", "")
            if valor_bruto is None or valor_bruto.strip() == "":
                avisos.append(f"Linha {numero_linha}: valor vazio, ignorada.")
                continue
            try:
                total += parse_valor(valor_bruto)
                linhas_validas += 1
            except InvalidOperation:
                avisos.append(
                    f"Linha {numero_linha}: valor inválido "
                    f"({valor_bruto!r}), ignorada."
                )

    return total, linhas_validas, avisos


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Soma a coluna 'valor' de um CSV com colunas data,produto,valor "
            "(apenas biblioteca padrão)."
        )
    )
    parser.add_argument("arquivo_csv", help="Caminho para o arquivo CSV de entrada.")
    parser.add_argument(
        "--delimiter",
        default=",",
        help="Delimitador usado no CSV (padrão: ',').",
    )
    args = parser.parse_args()

    try:
        total, linhas_validas, avisos = somar_csv(args.arquivo_csv, args.delimiter)
    except FileNotFoundError:
        print(f"Erro: arquivo não encontrado: {args.arquivo_csv}", file=sys.stderr)
        return 1
    except ValueError as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        return 1

    for aviso in avisos:
        print(f"Aviso: {aviso}", file=sys.stderr)

    print(f"Linhas somadas: {linhas_validas}")
    print(f"Total da coluna 'valor': {total}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
