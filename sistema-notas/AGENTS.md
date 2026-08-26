# AGENTS.md

Guia para agentes de código trabalhando neste projeto.

## Visão geral

Sistema web de acompanhamento de notas: professores cadastram turmas, alunos e avaliações; o sistema calcula médias ponderadas (pesos por turma), classifica alunos (aprovado/exame/reprovado, limites por turma) e mostra estatísticas atualizadas a cada lançamento. Ver `spec.md` para a especificação completa.

Este projeto ainda não tem código — está na fase de especificação. Este AGENTS.md descreve as decisões já tomadas na spec, para orientar a implementação quando ela começar.

## Stack

`spec.md` decide só: SPA + API backend, Supabase (Postgres + Auth). Framework de frontend/backend, linguagem e gerenciador de pacotes **ainda não foram escolhidos** — não presuma React/Node/TypeScript/npm até isso ser decidido (na especificação ou no modo Plan). Quando a stack for definida, os comandos de rodar/testar/lint entram aqui.

## Onde estão as regras

Toda regra de negócio, modelagem de dados e escopo já está em `spec.md` — não duplicado aqui. Abra `spec.md` antes de implementar qualquer parte do sistema; ele é curto o bastante para ler inteiro.
