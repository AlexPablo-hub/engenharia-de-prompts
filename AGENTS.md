# AGENTS.md

Guia para agentes de código trabalhando neste repositório.

## Visão geral

Este repositório contém a prática guiada da Aula 03 (Engenharia de Prompts e de Contexto) da disciplina Tópicos Especiais em Programação. Os exercícios comparam pares de prompts (vago/explícito, sem motivo/com motivo, sem exemplos/com exemplos, sem delimitador/com delimitador, sem critério de aceite/com critério de aceite) para observar o efeito de cada técnica no comportamento do agente.

## Estrutura

- `Aula-03-Engenharia-de-Prompts.pdf` — o material da aula.
- `observacoes.md` — respostas consolidadas dos 7 exercícios práticos, uma linha cada.
- `pratica-guiada/` — código produzido durante os exercícios, organizado por número:
  - `ex1/vago/` e `ex1/explicito/` — conversor de temperatura, comparando prompt vago vs explícito com `[Papel]/[Tarefa]/[Motivo]/[Formato]/[Aceite]`.
  - `ex2/sem_motivo/` e `ex2/com_motivo/` — script que soma a coluna `valor` de um CSV.
  - `ex3/sem_exemplos/` e `ex3/com_exemplos/` — normalizador de nomes de alunos.
  - `ex5/sem_aceite/` e `ex5/com_aceite/` — função de média ponderada.
  - `ex6-7/` — conversor de temperatura com validação estendida (NaN/infinito) e suíte pytest.
  - `note_01.md` a `note_07.md` — anotações de cada exercício.

## Como rodar

- Cada script funciona isoladamente: `python <arquivo>.py`.
- Testes do Exercício 6-7: `cd pratica-guiada/ex6-7 && python -m pytest -v`.
- O comando `pytest` puro não funciona nesta máquina (a pasta de Scripts do usuário não está no PATH) — use sempre `python -m pytest`.
- Testes do Exercício 5 (com_aceite): `cd pratica-guiada/ex5/com_aceite && python test_aceite.py`.

## Convenções de estilo

- Use nomes de variáveis e funções em português, em snake_case.
- Indentação de 4 espaços, nunca tabs.
- Limite as linhas a 79 caracteres quando possível, seguindo a PEP 8.
- Inclua type hints em todas as assinaturas de função.
- Escreva docstrings em todas as funções públicas.
- Evite linhas em branco duplas dentro de uma função.
- Prefira aspas duplas para strings.
- Não deixe código comentado (código morto) nos arquivos finais.

## Observações por exercício

### Exercício 1 — vago vs explícito
O prompt vago ("crie um conversor de temperatura") levou o agente a escolher sozinho: linguagem Python, interface CLI interativa em loop, unidades C/F/K, formato de entrada aceitando vírgula decimal, saída com 2 casas decimais e nome da unidade por extenso, e toda a política de erro (incluindo o valor exato do zero absoluto). Com a versão explícita, o agente entregou exatamente `converte.py` via argumentos de linha de comando, e os 3 casos do `[Aceite]` passaram.

### Exercício 2 — o motivo
Sem motivo, o agente evitou até o módulo `csv` da biblioteca padrão (parsing manual) e ainda assim comentou sobre pandas como opção futura. Com o motivo (servidor sem internet), usou `csv.DictReader` sem hesitar, trocou `float` por `decimal.Decimal` por conta própria, e não mencionou pandas em nenhum momento.

### Exercício 3 — exemplos
Sem exemplos, o agente inferiu as regras de normalização de nomes por convenção geral de português. Com três exemplos (sem nenhuma regra em prosa), extraiu corretamente as regras evidenciadas e documentou como suposição não comprovada a decisão de deixar a conjunção "e" em minúsculo.

### Exercício 4 — delimitadores
Testado com uma tentativa de instrução injetada dentro do texto a classificar. Tanto sem quanto com o delimitador `<dados>`, o agente resistiu à injeção e classificou corretamente como "misto".

### Exercício 5 — critério de aceite
Sem critério de aceite, o agente se autoverificou com testes que ele mesmo inventou. Com o bloco `[Aceite]`, validou exatamente os três casos e valores exigidos.

### Exercício 6 — pensar antes de agir
Em modo Plan, o agente leu o `converte.py` existente antes de escrever qualquer coisa e devolveu 6 perguntas, incluindo um bug real que encontrou sozinho (NaN/infinito passando pela validação sem erro).

### Exercício 7 — auto-correção
Ao revisar o próprio trabalho contra o `[Aceite]`, encontrou um caminho de overflow numérico sem teste, variantes de infinito incompletas, um caso de zero argumentos sem cobertura, e uma divergência entre o `[Aceite]` ("pytest roda") e o ambiente real (só `python -m pytest` funciona).
