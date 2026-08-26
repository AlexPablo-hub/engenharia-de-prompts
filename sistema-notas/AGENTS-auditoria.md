# Auditoria do AGENTS.md — sistema-notas (Exercício 8)

Auditoria contra a tabela da seção 6.2, no mesmo espírito do Fechamento dos Exercícios 1-7.

| Defeito | Apareceu? | Onde |
|---|---|---|
| **Lint Leakage** | **Sim** | Seção "Convenções de estilo" inteira (2 espaços, PascalCase/camelCase, aspas simples, `const`/`let`) — regras mecânicas que um linter/formatter garante, e nem havia stack decidida ainda para configurar um. |
| **Context Bloat** | **Sim** | As seções "Estrutura de dados" e "Regras de negócio" duplicavam quase palavra por palavra o `spec.md`, carregando o mesmo conteúdo duas vezes em toda sessão. |
| **Blind Reference** | **Parcial** | `spec.md` era citado várias vezes, mas nunca dizia "abra este arquivo antes de implementar" — cada citação linkava um pedaço específico sem apontar para o documento como um todo. |

**Achado extra (fora das 6 categorias do catálogo, mas real e mais grave que os três acima):** o rascunho inicial **inventou uma stack inteira que o `spec.md` nunca decidiu** — React, Node/Express, TypeScript, npm. A especificação só fala em "SPA + API backend"; framework, linguagem e gerenciador de pacotes continuam em aberto. Um agente seguindo esse AGENTS.md ao pé da letra teria implementado uma escolha técnica não autorizada por ninguém do grupo. Isso é mais perigoso que os defeitos catalogados porque não é ruído (custo de contexto) — é uma decisão de projeto fabricada, apresentada como se já tivesse sido tomada.

**Correção aplicada:**
1. Removida a seção "Convenções de estilo" (Lint Leakage) — sem stack definida, não há o que padronizar ainda.
2. Removidas "Estrutura de dados" e "Regras de negócio" (Context Bloat), substituídas por uma linha dizendo para abrir `spec.md` antes de implementar (resolve também o Blind Reference).
3. A seção "Stack" foi reescrita para dizer explicitamente o que a spec decide e o que **não** decide, com aviso para não presumir React/Node/TypeScript/npm até isso ser resolvido.

Resultado: 50 → 17 linhas, e a fabricação de stack foi removida em vez de só reduzida.
