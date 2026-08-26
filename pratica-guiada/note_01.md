# Exercício 1 — o vago e o explícito

**Técnica:** seção 4.1. **O que observar:** quantas decisões o agente tomou no lugar de quem pediu.

## Passo 1-2 — prompt vago: "crie um conversor de temperatura"

Sem nenhuma outra informação, o agente teve que decidir sozinho:

- **Linguagem:** Python (não foi pedido).
- **Interface:** CLI *interativa em loop* (pergunta valor → pergunta unidade → mostra resultado), em vez de uma chamada única por argumentos de linha de comando.
- **Unidades suportadas:** Celsius, Fahrenheit e Kelvin — escolha razoável, mas arbitrária (poderia ter sido só C/F).
- **Formato de entrada:** aceita tanto ponto quanto vírgula decimal.
- **Formato de saída:** 2 casas decimais, nome da unidade por extenso.
- **Tratamento de entrada inválida:** mensagens específicas para texto não numérico, unidade desconhecida e valor abaixo do zero absoluto — todas inventadas por conta própria, incluindo o próprio valor de corte (-273,15 °C).
- **Idioma** das mensagens: português, por inferência do idioma do pedido.

Nenhum desses pontos estava no pedido original — todos são decisões implícitas.

## Passo 3-4 — prompt explícito ([Papel]/[Tarefa]/[Motivo]/[Formato]/[Aceite])

Com a estrutura explícita, o agente entregou exatamente o formato pedido (`converte.py`, CLI por argumentos, só biblioteca padrão) e os três casos do `[Aceite]` foram testados e **passaram de verdade** (conferido de forma independente, fora da sessão que gerou o código):

```
$ python converte.py 100 C F
212.0

$ python converte.py -280 C F
Erro: -280.0 C está abaixo do zero absoluto (-273.15 C)...
(exit code 1)

$ python converte.py 100 C X
Erro: unidade 'X' desconhecida. Unidades válidas: C, F, K...
(exit code 1)
```

## Resposta do exercício

**Ex1: o agente decidiu por mim:** a linguagem, o estilo de interface (loop interativo em vez de argumentos), o conjunto de unidades, o formato de entrada/saída e toda a política de erro — inclusive o valor exato do zero absoluto usado no corte. Com `[Papel]/[Tarefa]/[Motivo]/[Formato]/[Aceite]`, todas essas decisões desaparecem: o único grau de liberdade que sobrou foi a organização interna do código (ele escolheu converter tudo via Celsius como intermediário, em vez de 6 fórmulas diretas — uma decisão de design, não de comportamento observável).
