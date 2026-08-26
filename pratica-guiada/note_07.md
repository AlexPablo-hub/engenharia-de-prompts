# Exercício 7 — auto-correção

**Técnica:** seção 5.3. **O que observar:** o que o agente encontra sozinho.

## Passo 1 — pedido de auto-revisão (mesma sessão do Exercício 6)

"Revise o que você escreveu contra o bloco [Aceite], item por item. Diga o que cumpre e o que não cumpre antes de corrigir qualquer coisa."

## Passo 2 — o que ele encontrou sozinho (bugs reais, confirmados de forma independente)

Antes desta revisão, os testes já passavam (50/50) e ele já tinha reportado sucesso — ou seja, os problemas abaixo **não apareceriam** se eu tivesse aceitado o primeiro "está pronto" sem pedir a auto-correção:

1. **Overflow numérico não coberto:** `float("1e400")` também vira `inf` em Python (não só a string literal `"inf"`), e esse caminho não tinha teste nem tratamento explícito verificado ponta a ponta via `main()`.
2. **Variantes de infinito incompletas:** `"+inf"`, `"+Infinity"`, `"INF"`, `"-nan"` não estavam cobertas — só as formas mais óbvias tinham teste.
3. **Caso de zero argumentos** (`main([])`) não estava testado, só "número errado" em geral.
4. **Assertivas de teste frouxas:** alguns testes aceitavam qualquer uma de duas mensagens de erro (`"X" in err or "Y" in err`), o que mascararia uma regressão futura na mensagem exata.
5. **Um item do próprio `[Aceite]` não se sustentava ao pé da letra:** o item 1 dizia "`pytest` roda... sem falhas" — mas o comando `pytest` puro **não existe no PATH desta máquina** (confirmado de forma independente: `pytest: command not found`); só `python -m pytest` funciona. Em vez de simplesmente declarar sucesso, ele isolou a causa raiz (a pasta com `pytest.exe` não está no `PATH` do usuário), explicou que corrigir isso seria mexer em configuração da máquina fora do escopo do diretório do exercício, e **pediu confirmação antes de alterar algo fora do projeto** — não "consertou" silenciosamente nem ignorou a divergência.

## Passo 2 (continuação) — resultado após a correção

Depois de corrigir os itens 1-4, a suíte foi de 50 para **59 testes, todos passando** (`python -m pytest`) — confirmado de forma independente, fora da sessão que fez a correção.

## Resposta do exercício

**Ex7: ele encontrou sozinho:** um caminho de overflow numérico (`"1e400"` → `inf`) sem teste, variantes de infinito incompletas, o caso de zero argumentos sem cobertura, testes com asserções frouxas demais para pegar regressão futura, e uma divergência real entre o que o `[Aceite]` pedia ao pé da letra ("`pytest` roda") e o ambiente real (só `python -m pytest` funciona nesta máquina) — que ele expôs em vez de mascarar, e não corrigiu sozinho por estar fora do escopo dos arquivos do exercício.
