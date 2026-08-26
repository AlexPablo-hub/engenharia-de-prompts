"""Normalização de nomes de alunos para exibição."""

# Preposições/conectivos que devem permanecer em minúsculas,
# exceto quando forem a primeira palavra do nome.
PARTICULAS_MINUSCULAS = {"da", "de", "do", "das", "dos", "e"}


def normalizar_nome(nome: str) -> str:
    """Normaliza um nome de aluno para exibição.

    Regras aplicadas:
    - Remove espaços em branco no início/fim e colapsa espaços internos
      múltiplos em um único espaço.
    - Converte cada palavra para o formato "Capitalizado" (primeira letra
      maiúscula, restante minúsculo), tratando corretamente entradas em
      caixa alta, baixa ou mista (ex.: "CONCEICAO" -> "Conceicao").
    - Mantém em minúsculas as preposições/conectivos comuns em nomes
      compostos (da, de, do, das, dos, e), exceto quando aparecem como a
      primeira palavra do nome.

    Args:
        nome: nome bruto do aluno, possivelmente com espaçamento ou
            capitalização irregulares.

    Returns:
        O nome normalizado, pronto para exibição. Retorna string vazia
        se a entrada for vazia ou contiver apenas espaços.
    """
    if not nome:
        return ""

    # Colapsa espaços múltiplos e remove espaços nas bordas.
    palavras = nome.split()
    if not palavras:
        return ""

    resultado = []
    for indice, palavra in enumerate(palavras):
        palavra_lower = palavra.lower()
        if indice > 0 and palavra_lower in PARTICULAS_MINUSCULAS:
            resultado.append(palavra_lower)
        else:
            resultado.append(palavra_lower.capitalize())

    return " ".join(resultado)


if __name__ == "__main__":
    entrada = "maria da CONCEICAO"
    print(normalizar_nome(entrada))
