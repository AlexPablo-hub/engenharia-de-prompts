"""
Le um arquivo CSV com as colunas: data,produto,valor
e soma os valores da coluna 'valor'.

Abordagem escolhida: parsing manual, linha a linha, usando apenas
recursos nativos da linguagem (open, str.split, float) - sem importar
nem mesmo o modulo `csv` da biblioteca padrao do Python. Isso segue a
instrucao "nao use bibliotecas externas" da forma mais restrita
possivel (nenhum "import" alem do `sys`, que serve so para ler o nome
do arquivo pela linha de comando).

Observacao / limitacao dessa escolha:
- Por nao usar o modulo `csv`, este script assume um CSV "simples":
  separador por virgula, sem valores entre aspas e sem virgulas
  dentro dos campos (ex: nomes de produto como "Caneta, azul" ou
  numeros como "1.234,56" quebrariam esse parsing manual).
- O modulo `csv` (import csv) faz parte da biblioteca padrao do
  Python - ou seja, nao e uma biblioteca externa/terceira e nao
  precisa ser instalado - e resolve esses casos de forma mais
  robusta. Se o requisito "sem bibliotecas externas" for interpretado
  como "sem pacotes de terceiros" (ex: pandas), o ideal seria usar
  `import csv` em vez deste parsing manual.
- Para analises maiores ou mais completas (agrupar por produto, por
  data, filtros, etc.), bibliotecas como pandas facilitariam bastante,
  mas exigiriam instalacao (`pip install pandas`) e não sao
  necessarias para esta tarefa simples de somar uma coluna.
"""

import sys


def somar_coluna_valor(caminho_csv):
    """Le o CSV e retorna (soma_total, linhas_validas, linhas_com_erro)."""
    total = 0.0
    linhas_processadas = 0
    linhas_com_erro = []

    with open(caminho_csv, "r", encoding="utf-8") as arquivo:
        cabecalho = arquivo.readline()
        if not cabecalho:
            raise ValueError("Arquivo CSV vazio.")

        colunas = [c.strip() for c in cabecalho.strip().split(",")]
        try:
            indice_valor = colunas.index("valor")
        except ValueError:
            raise ValueError(
                f"Coluna 'valor' nao encontrada no cabecalho: {colunas}"
            )

        for numero_linha, linha in enumerate(arquivo, start=2):
            linha = linha.strip()
            if not linha:
                continue  # ignora linhas em branco

            campos = linha.split(",")
            if len(campos) <= indice_valor:
                linhas_com_erro.append((numero_linha, linha))
                continue

            valor_texto = campos[indice_valor].strip()
            try:
                valor = float(valor_texto)
            except ValueError:
                linhas_com_erro.append((numero_linha, linha))
                continue

            total += valor
            linhas_processadas += 1

    return total, linhas_processadas, linhas_com_erro


def main():
    caminho_csv = sys.argv[1] if len(sys.argv) > 1 else "vendas.csv"

    try:
        total, linhas_processadas, linhas_com_erro = somar_coluna_valor(caminho_csv)
    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho_csv}' nao encontrado.")
        sys.exit(1)
    except ValueError as erro:
        print(f"Erro: {erro}")
        sys.exit(1)

    print(f"Arquivo: {caminho_csv}")
    print(f"Linhas somadas: {linhas_processadas}")
    print(f"Soma da coluna 'valor': {total:.2f}")

    if linhas_com_erro:
        print(f"\nAviso: {len(linhas_com_erro)} linha(s) ignorada(s) por erro de formato:")
        for numero, linha in linhas_com_erro:
            print(f"  linha {numero}: {linha}")


if __name__ == "__main__":
    main()
