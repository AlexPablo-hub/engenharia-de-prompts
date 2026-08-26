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
  - `note_01.md` a `note_07.md` — o que foi observado em cada exercício especificamente. Abra o `note_0N.md` correspondente só se for mexer naquele exercício; não é necessário para tarefas em outras pastas.

## Como rodar

- Cada script funciona isoladamente: `python <arquivo>.py`.
- Testes do Exercício 6-7: `cd pratica-guiada/ex6-7 && python -m pytest -v`.
- O comando `pytest` puro não funciona nesta máquina (a pasta de Scripts do usuário não está no PATH) — use sempre `python -m pytest`.
- Testes do Exercício 5 (com_aceite): `cd pratica-guiada/ex5/com_aceite && python test_aceite.py`.
