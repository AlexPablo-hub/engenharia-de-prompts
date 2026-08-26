# Especificação — Sistema de Acompanhamento de Notas

## 1. Visão geral

Sistema web para professores acompanharem notas de turmas: cadastro de turmas, alunos e avaliações, cálculo de médias ponderadas com regras por turma, classificação de situação, e estatísticas atualizadas a cada lançamento.

## 2. Plataforma

**Web, SPA (frontend) + API backend.** Login obrigatório: professor e aluno acessam autenticados. O professor cadastra turmas, alunos e avaliações e vê tudo. O aluno só enxerga, em modo leitura, a própria situação (notas lançadas, média atual, classificação) — não edita nada.

## 3. Persistência

**Supabase** (Postgres relacional). Dados persistem na nuvem, entre sessões e dispositivos.

Tabelas mínimas (ajustar conforme achar necessário):
- **turmas**: id, nome, id do professor dono, pesos das avaliações (ex: `{"prova1": 0.3, "prova2": 0.3, "trabalho": 0.4}` — soma deve dar 1.0 ou 100%), limite de aprovação, limite de exame.
- **alunos**: id, nome, id da turma (chave estrangeira), id do usuário Supabase Auth correspondente (para o aluno logar e ver a própria situação).
- **avaliacoes**: id, id do aluno (chave estrangeira), tipo/nome da avaliação (deve bater com uma das chaves de peso da turma), nota (pode estar ausente = "não lançada").

## 4. Regras de cálculo

- **Média ponderada por aluno**: soma de (nota × peso) / soma dos pesos das avaliações da turma.
- **Nota pendente (avaliação ainda não lançada): tratada como 0** no cálculo da média.
- **Arredondamento**: 2 casas decimais, arredondamento matemático padrão (0,005 arredonda para cima).
- **Classificação**: `média ≥ limite_aprovacao` → aprovado; `limite_exame ≤ média < limite_aprovacao` → exame; `média < limite_exame` → reprovado.

## 5. Estatísticas (recalculadas a cada lançamento de nota)

Por turma:
- Média das médias dos alunos.
- Mediana das médias dos alunos.
- Distribuição por situação (quantos aprovados / exame / reprovados).
- Lista de alunos a menos de 0,5 ponto do limite de aprovação.

## 6. Validação de entrada

- Nota deve estar em uma faixa válida (ex: 0 a 10) — rejeitar fora disso com mensagem dizendo qual o intervalo aceito.
- Pesos de uma turma devem somar 1.0 (ou 100%) — rejeitar cadastro/edição de turma que não bata essa soma, com mensagem mostrando a soma atual.
- Nome de aluno/turma não pode ser vazio.
- Avaliação lançada para um tipo que não existe nos pesos da turma é rejeitada, listando os tipos válidos.

## 7. Fora de escopo

- Não permite múltiplos professores na mesma turma (cada turma pertence a um único professor).
- Aluno tem acesso somente de leitura à própria situação; não edita nada.
- Não gera boletim em PDF nem exporta dados.
- Não envia notificação (email/push) quando uma nota é lançada.
- Não implementa fluxo de recuperação de senha além do padrão do Supabase Auth.
- Não trata edição simultânea da mesma nota por dois usuários (sem resolução de conflito além do último salvamento vencer).