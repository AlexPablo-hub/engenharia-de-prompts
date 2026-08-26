# Exercício 2 — o motivo

**Técnica:** seção 4.2. **O que observar:** se a restrição se generaliza para o que não foi dito.

## Passo 1 — sem motivo: "não use bibliotecas externas"

O agente interpretou a instrução da forma **mais restritiva possível**: evitou até o módulo `csv` da biblioteca padrão, fazendo parsing manual linha a linha com `open()` + `split(",")`. E, apesar de a tarefa não pedir nada além de somar uma coluna, ele **comentou espontaneamente sobre pandas**, deixando no docstring do script:

> "Para análises maiores ou mais completas (agrupar por produto, por data, filtros, etc.), bibliotecas como pandas facilitariam bastante, mas exigiriam instalação (`pip install pandas`)..."

Ou seja: mesmo sem usar, ele **abriu a porta** para pandas como próximo passo natural.

## Passo 2 — com motivo: "...porque este script vai rodar num servidor sem acesso à internet"

Com o motivo explícito, o agente:

- Usou `csv.DictReader` da biblioteca padrão **sem hesitar e sem comentar sobre pandas em nenhum momento**.
- Foi além do pedido, mas na direção certa: trocou `float` por `decimal.Decimal` para evitar erro de arredondamento em soma monetária, justificando que isso **também é biblioteca padrão** (`decimal`) — ou seja, ele generalizou a restrição ("sem instalar nada") para uma decisão nova que nem havia sido perguntada.
- Adicionou tratamento para formatos numéricos BR (vírgula decimal, milhar) e validação de cabeçalho ausente — robustez extra, coerente com "vai rodar sozinho num servidor", sem sugerir nenhuma dependência.

## Resposta do exercício

**Ex2: com o motivo, ele também evitou:** qualquer menção a pandas ou a instalar pacotes — e generalizou a restrição "sem bibliotecas externas" para escolher deliberadamente `decimal` (padrão) no lugar de `float`, algo que não foi pedido, mas que se alinha com o motivo dado ("servidor sem internet, precisa ser robusto por conta própria"). Sem o motivo, a mesma restrição foi cumprida ao pé da letra, mas o agente deixou pandas como sugestão futura — o motivo não só evitou a sugestão como mudou uma decisão técnica que a instrução sozinha não cobria.
