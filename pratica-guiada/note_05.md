# Exercício 5 — critério de aceite

**Técnica:** seção 4.5. **O que observar:** se o agente executa algo para conferir antes de devolver.

## Passo 1-2 — sem critério de aceite: "Faça uma função Python de média ponderada."

O agente, por iniciativa própria, **rodou o código antes de finalizar**: executou o exemplo embutido (`6.95`) e ainda escreveu testes ad hoc extras cobrindo caminho feliz, listas de tamanhos diferentes, listas vazias e soma de pesos zero — tudo com casos que ele mesmo inventou.

## Passo 3-4 — com `[Aceite]` explícito (3 casos com valores exatos)

O agente testou exatamente os 3 casos pedidos, em um script de verificação dedicado, e reportou o resultado real (confirmado de forma independente, fora da sessão que gerou o código):

```
caso1: 8.1
caso2: ValueError OK
caso3: ValueError OK
```

## Resultado real (diferente do esperado pelo roteiro)

O roteiro assume que, sem critério de aceite, o agente "entrega e para". **Não foi o que aconteceu**: mesmo sem `[Aceite]`, este modelo já se autoverifica por hábito. A diferença real não é *se* testou, e sim *o quê* testou e *contra o quê comparou*:

- **Sem aceite:** os casos de teste foram escolhidos pelo próprio agente, sem nenhum valor-alvo externo — ele decide sozinho o que "está certo".
- **Com aceite:** os casos e os valores esperados (`8.1`, os dois `ValueError`) vieram de fora, então a verificação é objetiva e reprodutível — qualquer pessoa (ou outra sessão) pode conferir o mesmo resultado exato.

## Resposta do exercício

**Ex5: sem aceite ele parou quando** os próprios testes que inventou passaram (critério de "pronto" definido por ele mesmo); **com aceite ele** validou exatamente os três casos que eu especifiquei, com os valores exatos que eu exigi — a diferença não é testar ou não testar, é quem define o que conta como aprovado.
