# Exercício 3 — exemplos

**Técnica:** seção 4.3. **O que observar:** o tratamento dos casos que não foram descritos.

## Passo 1-2 — sem exemplos, só a descrição

Pedido: "normalize nomes de alunos para exibição", sem nenhuma regra escrita. O agente inferiu por conta própria: colapsar espaços, capitalizar cada palavra, e manter minúsculas as partículas `da/de/do/das/dos` (e também `e`) — regras de convenção geral de nomes em português, não algo extraído de um exemplo.

Teste pedido pelo roteiro (`"maria da CONCEICAO"`) → `"Maria da Conceicao"` — **correto**.

## Passo 3-4 — com três exemplos, sem nenhuma regra em prosa

```
<exemplos>
" ana MARIA silva "   -> "Ana Maria Silva"
"JOSE DOS SANTOS"     -> "Jose dos Santos"
"maria da CONCEICAO"  -> "Maria da Conceicao"
</exemplos>
```

O agente extraiu corretamente as regras evidenciadas (trim, capitalização por palavra, `dos`/`da` em minúsculo) e foi honesto sobre o que **não** estava provado pelos exemplos: incluir a conjunção `"e"` na lista de minúsculas foi uma extrapolação por analogia, documentada explicitamente no código como suposição, não como regra confirmada.

## Passo 4 — caso novo, fora dos exemplos: "PEDRO DE ALCANTARA e SILVA"

Testei as duas versões (sem exemplos e com exemplos) com **o mesmo caso novo**, fora da sessão original, para comparação justa:

```
sem_exemplos:  'Pedro de Alcantara e Silva'
com_exemplos:  'Pedro de Alcantara e Silva'
```

**Resultado idêntico nas duas versões** — neste caso específico não houve erro em nenhuma delas, porque a convenção de nomes em português já é bem conhecida do modelo mesmo sem exemplos. A diferença real não apareceu no *resultado*, e sim na *natureza da decisão*: sem exemplos, a regra veio de conhecimento geral de linguagem; com exemplos, a mesma regra (`"e"` minúsculo) teve que ser **extrapolada e declarada como suposição**, ilustrando exatamente o ponto da seção 4.3 — o que não está nos exemplos fica por conta do agente, e se importa para o seu caso, precisa entrar entre os exemplos.

## Resposta do exercício

**Ex3: sem exemplos ele errou em:** nada, neste caso testado (o caso é comum o bastante para já estar na convenção que o modelo conhece) — **com exemplos:** também não errou, mas precisou assumir e documentar uma extrapolação (o "e" minúsculo) que os 3 exemplos não comprovavam. A lição prática do exercício aparece mesmo sem erro observável: few-shot não elimina ambiguidade fora do que foi mostrado, só a torna visível/documentada em vez de silenciosa.
