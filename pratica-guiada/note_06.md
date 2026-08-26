# Exercício 6 — pensar antes de agir

**Técnica:** seção 5. **O que observar:** as perguntas que o agente faz.

## Passo 1-2 — modo Plan, tarefa multi-arquivo

Pedido: "Acrescente validação de entrada ao converte.py e cubra com testes em pytest. Antes de escrever qualquer arquivo, liste as decisões que você vai tomar e os pontos do pedido que estiverem ambíguos. Aguarde a minha confirmação."

## Passo 3 — perguntas feitas pelo agente (resultado do exercício)

Antes de escrever qualquer coisa, ele leu o `converte.py` existente e devolveu 6 perguntas reais, todas pertinentes:

1. **"Validação de entrada" — estender ou só testar o que já existe?** (o código já validava bastante coisa)
2. Aceitar vírgula como separador decimal (formato BR) ou manter a rejeição atual?
3. Testes em arquivo único ao lado do script, ou pasta `tests/` separada? Nome exigido pela disciplina?
4. Só `pytest` puro, ou também `pytest-cov`?
5. Testar só as funções internas/`main()`, ou também via `subprocess` (uso real da CLI)?
6. Só existe validação de limite **inferior** (zero absoluto) — quer também um limite superior?

Ele também identificou sozinho, só de ler o código, uma lacuna real que a tarefa nem mencionava: `float("nan")` e `float("inf")` passam pela validação atual sem erro, e uma comparação com `nan` nunca é verdadeira — ou seja, um valor `NaN` conseguiria atravessar a validação de zero absoluto sem ser barrado. Isso não era um bug pedido para caçar; apareceu como efeito colateral de ele ler o código antes de agir.

## Passo 4 — resposta e liberação para implementar

Respondi (registrado em `pratica-guiada/ex6-7/resposta-plano.md`): estender a validação (incluir o caso de NaN/infinito), manter a rejeição do formato BR como está, testes em arquivo único `test_converte.py`, só `pytest` puro, sem `subprocess`, sem limite superior — e defini um `[Aceite]` explícito para a implementação, já pensando no Exercício 7.

## Resposta do exercício

**Ex6: ele perguntou:** se deveria só cobrir com testes a validação já existente ou também estendê-la (incluindo um caso real de bug que ele mesmo achou — NaN/infinito passando sem erro), se deveria aceitar vírgula decimal, onde colocar os testes, se usaria `pytest-cov` e testes via `subprocess`, e se faltava validar um limite superior de temperatura.
