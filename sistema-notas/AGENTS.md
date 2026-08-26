# AGENTS.md

Guia para agentes de código trabalhando neste projeto.

## Visão geral

Sistema web de acompanhamento de notas: professores cadastram turmas, alunos e avaliações; o sistema calcula médias ponderadas (pesos por turma), classifica alunos (aprovado/exame/reprovado, limites por turma) e mostra estatísticas atualizadas a cada lançamento. Ver `spec.md` para a especificação completa.

Este projeto ainda não tem código — está na fase de especificação. Este AGENTS.md descreve as decisões já tomadas na spec, para orientar a implementação quando ela começar.

## Stack

- Frontend: SPA (React) consumindo uma API.
- Backend: API própria (Node/Express).
- Persistência: Supabase (Postgres) + Supabase Auth para login.
- Gerenciador de pacotes: npm.

## Como rodar

- `npm install` para instalar dependências.
- `npm run dev` para rodar o frontend em desenvolvimento.
- `npm test` para rodar os testes.
- `npm run lint` para checar estilo de código.

## Estrutura de dados (de `spec.md`, seção 3)

- **turmas**: id, nome, id do professor dono, pesos das avaliações (soma deve dar 1.0 ou 100%), limite de aprovação, limite de exame.
- **alunos**: id, nome, id da turma, id do usuário Supabase Auth.
- **avaliacoes**: id, id do aluno, tipo/nome da avaliação, nota (pode estar ausente).

## Regras de negócio (de `spec.md`, seções 4-6)

- Média ponderada: soma de (nota × peso) / soma dos pesos da turma.
- Nota pendente (avaliação não lançada) conta como 0 na média.
- Arredondamento: 2 casas decimais, arredondamento matemático padrão.
- Classificação: `média ≥ limite_aprovacao` → aprovado; `limite_exame ≤ média < limite_aprovacao` → exame; `média < limite_exame` → reprovado.
- Estatísticas por turma (seção 5): média das médias, mediana das médias, distribuição por situação, lista de alunos a menos de 0,5 ponto do limite de aprovação — recalculadas a cada lançamento de nota.
- Validação de entrada: nota em faixa válida (0-10), soma dos pesos da turma = 1.0/100%, nomes não vazios, tipo de avaliação precisa existir nos pesos da turma — sempre rejeitar com mensagem dizendo o que está errado.

## Convenções de estilo

- Use TypeScript em vez de JavaScript puro.
- Componentes React em PascalCase, funções e variáveis em camelCase.
- Indentação de 2 espaços.
- Prefira aspas simples em strings JavaScript/TypeScript.
- Sempre use `const`/`let`, nunca `var`.
- Exporte um componente por arquivo.
- Escreva testes para toda função de cálculo (média, classificação, estatísticas).

## Fora de escopo (de `spec.md`, seção 7)

Múltiplos professores por turma, boletim em PDF, notificações por email/push, recuperação de senha customizada, resolução de conflito em edição simultânea — ver `spec.md` para a lista completa.
