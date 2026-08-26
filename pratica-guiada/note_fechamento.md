# Fechamento — auditoria do próprio AGENTS.md

**Passo 1:** rodei `/init` na pasta raiz do repositório. Ele leu a estrutura de `pratica-guiada/` (7 exercícios, cada um com pares de variantes) e gerou o `AGENTS.md` inicial (ver histórico do git, commit "chore: gera AGENTS.md via /init").

**Passo 2 — auditoria contra a tabela da seção 6.2:**

| Defeito | Apareceu? | Onde |
|---|---|---|
| **Lint Leakage** | **Sim** | Seção inteira "Convenções de estilo": snake_case, indentação de 4 espaços, limite de 79 colunas, aspas duplas, ausência de linhas em branco duplas — tudo isso é exatamente o que um formatador (ex.: `black`/`ruff`) garante automaticamente. O repositório nem tem um formatador configurado, o que tornava essas regras letra morta: ninguém as impunha, elas só ocupavam janela de contexto em toda sessão. |
| **Context Bloat** | **Sim** | Seção "Observações por exercício": um resumo de cada um dos 7 exercícios, duplicando quase palavra por palavra o que já está em `observacoes.md` e em cada `note_0N.md`. Isso carrega, em **toda** sessão (mesmo uma que só mexe no Exercício 3), o histórico completo dos outros 6 exercícios — o oposto do "menor conjunto possível de tokens de alto sinal" citado na aula. |
| **Blind Reference** | **Sim** | A lista de `note_01.md` a `note_07.md` na seção "Estrutura" citava os arquivos sem dizer quando abri-los — um agente lendo o AGENTS.md não saberia se precisa carregar todos, nenhum, ou só o relevante para a tarefa atual. |

Os outros três defeitos do catálogo (Skill Leakage, Conflicting Instructions, Init Fossilization) não se aplicam aqui: não há instrução rara/específica isolada em arquivo separado (Skill Leakage não fazia sentido no tamanho do arquivo gerado), não havia contradição entre instruções, e o defeito de Init Fossilization é justamente o que este próprio exercício evita — o arquivo está sendo revisto, não fossilizado.

**Passo 3 — correção aplicada:**

1. Removida inteiramente a seção "Convenções de estilo" (Lint Leakage) — se um formatador for adicionado ao projeto no futuro, a configuração deve viver nele, não no AGENTS.md.
2. A seção "Observações por exercício" (7 parágrafos) foi removida e substituída por uma frase na entrada de `note_01.md`...`note_07.md`: "abra o `note_0N.md` correspondente só se for mexer naquele exercício; não é necessário para tarefas em outras pastas" (corrige Context Bloat e Blind Reference ao mesmo tempo — agora o arquivo diz para que serve e quando abrir).
3. Mantido o que tem sinal real e não é óbvio: a estrutura de pastas, e o aviso sobre o `pytest` puro não funcionar nesta máquina (isso não é coberto por nenhum linter/formatador e evitaria retrabalho de qualquer pessoa — inclusive um agente — que tentasse rodar `pytest` sem o `python -m`).

Resultado: o arquivo caiu de ~55 linhas para 27, sem perder nenhuma informação que um agente realmente precisaria para orientar uma tarefa futura no repositório.
