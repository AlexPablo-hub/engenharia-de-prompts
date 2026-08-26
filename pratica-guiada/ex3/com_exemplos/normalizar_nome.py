"""
Normalizacao de nomes de alunos para exibicao.

Regras inferidas a partir dos exemplos fornecidos (nenhuma regra em prosa
foi dada, apenas os pares entrada -> saida):

1. Espacos extras (no inicio, no fim, ou repetidos entre palavras) sao
   removidos.
2. Cada palavra e capitalizada: primeira letra maiuscula, demais letras
   minusculas - independentemente de como a palavra foi digitada
   originalmente (tudo maiusculo, tudo minusculo, misto).
3. Excecao: conectivos/preposicoes comuns em nomes de lingua portuguesa
   ("de", "da", "do", "das", "dos") permanecem inteiramente em minusculas,
   mesmo que tenham sido digitados em maiusculas (ex.: "DOS" -> "dos").
   Isso foi observado diretamente no exemplo "JOSE DOS SANTOS" ->
   "Jose dos Santos" e "maria da CONCEICAO" -> "Maria da Conceicao".
4. Por extensao dessa mesma familia de conectivos portugueses, tambem
   incluimos "e" (a conjuncao "e", como em "Pedro de Alcantara e Silva").
   Isso NAO aparece nos exemplos originais - e uma generalizacao/assuncao
   feita para cobrir nomes compostos comuns, e esta documentada aqui para
   deixar essa escolha explicita.
"""

CONECTIVOS = {"de", "da", "do", "das", "dos", "e"}


def normalizar_nome(nome: str) -> str:
    """
    Normaliza um nome de aluno para exibicao.

    - Remove espacos extras (inicio, fim e entre palavras).
    - Capitaliza cada palavra (primeira letra maiuscula, resto minuscula).
    - Mantem conectivos portugueses ("de", "da", "do", "das", "dos", "e")
      em minusculas.

    >>> normalizar_nome(" ana MARIA silva ")
    'Ana Maria Silva'
    >>> normalizar_nome("JOSE DOS SANTOS")
    'Jose dos Santos'
    >>> normalizar_nome("maria da CONCEICAO")
    'Maria da Conceicao'
    """
    palavras = nome.split()  # split() sem argumento ja remove espacos extras

    resultado = []
    for palavra in palavras:
        palavra_lower = palavra.lower()
        if palavra_lower in CONECTIVOS:
            resultado.append(palavra_lower)
        else:
            resultado.append(palavra_lower.capitalize())

    return " ".join(resultado)


if __name__ == "__main__":
    exemplos = [
        (" ana MARIA silva ", "Ana Maria Silva"),
        ("JOSE DOS SANTOS", "Jose dos Santos"),
        ("maria da CONCEICAO", "Maria da Conceicao"),
    ]

    print("Verificando exemplos fornecidos:")
    for entrada, esperado in exemplos:
        saida = normalizar_nome(entrada)
        status = "OK" if saida == esperado else "FALHOU"
        print(f"  {status}: {entrada!r} -> {saida!r} (esperado {esperado!r})")

    print()
    print("Teste com entrada fora dos exemplos:")
    teste = "PEDRO DE ALCANTARA e SILVA"
    saida = normalizar_nome(teste)
    print(f"  {teste!r} -> {saida!r}")
