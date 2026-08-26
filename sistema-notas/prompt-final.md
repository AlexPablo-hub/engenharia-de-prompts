# prompt-final.md

Versão lapidada com IA a partir de `prompt-humano.md`, para entregar ao agente em modo Plan.

---

[Papel] Você é um agente de desenvolvimento, em modo de planejamento (Plan mode) — não vai escrever nem editar nenhum arquivo de código nesta etapa.

[Tarefa] Leia a especificação em `spec.md` (sistema web de acompanhamento de notas) e produza um plano de implementação. Em separado, liste todos os pontos da especificação que ficaram ambíguos, incompletos ou não decididos.

[Motivo] O projeto ainda está na fase de especificação. Antes de qualquer código, queremos ver o plano e fechar as ambiguidades reais que a spec deixou em aberto.

[Formato] Responda em duas seções: "Plano" (passos de implementação, na ordem, com as decisões técnicas que cada passo exige) e "Ambiguidades" (perguntas concretas — uma por item — sobre o que `spec.md` não resolve).

[Aceite]
1. Nenhum arquivo é criado ou editado nesta etapa.
2. Toda ambiguidade real do `spec.md` aparece na lista (ex.: framework de frontend/backend ainda não escolhido, regras de acesso do Supabase não detalhadas).
3. Cada passo do plano referencia a seção do `spec.md` em que se baseia.

---

## O que mudou em relação ao prompt-humano.md, e por quê

- **Mudei:** troquei a frase corrida (com a duplicação "especificações espesificações") pela estrutura `[Papel]/[Tarefa]/[Motivo]/[Formato]/[Aceite]`, e substituí "coisas que você pode analisar que faltam" por duas seções explícitas na resposta ("Plano" e "Ambiguidades"), com um critério de aceite dizendo que nenhum arquivo pode ser tocado.
- **Por quê:** o próprio Exercício 1 já mostrou que um pedido sem formato definido deixa o agente escolher a estrutura da resposta sozinho — aqui isso importa porque, sem "duas seções" separadas, plano e perguntas viriam misturados no texto, dificultando extrair as perguntas para o `clarificacoes.md` no próximo passo. O critério de aceite "nenhum arquivo é criado" também deixa objetivamente verificável que o agente respeitou o modo Plan, em vez de confiar só na instrução em prosa.
