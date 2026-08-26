# Observações — prática guiada (Exercícios 1 a 7 + Fechamento)

Uma linha por exercício, conforme pedido no roteiro. Detalhamento completo de cada um em `pratica-guiada/note_01.md` a `note_07.md`.

**Ex1:** o agente decidiu por mim: a linguagem (Python), o estilo de interface (loop interativo em vez de argumentos de linha de comando), o conjunto de unidades suportadas, o formato de entrada/saída e toda a política de erro — inclusive o valor exato do zero absoluto usado no corte.

**Ex2:** com o motivo, ele também evitou: qualquer menção a pandas/instalação de pacotes, e generalizou a restrição para uma decisão nova não pedida (`decimal` em vez de `float`, justificada pelo ambiente sem internet); sem o motivo, ele cumpriu a regra ao pé da letra mas deixou pandas como sugestão futura.

**Ex3:** sem exemplos ele errou em: nada, no caso testado (a convenção de nomes em português já é conhecida do modelo); com exemplos: também não errou, mas precisou extrapolar e declarar como suposição uma regra não coberta pelos 3 exemplos (a conjunção "e" em minúsculo) — a ambiguidade não desapareceu, só ficou visível.

**Ex4:** sem delimitador ele classificou corretamente e ignorou a instrução injetada, sinalizando a tentativa; com delimitador ele fez exatamente o mesmo — não houve diferença observável neste teste, o que reforça que o delimitador é defesa em profundidade, não uma correção de uma falha que se comprovou aqui.

**Ex5:** sem aceite ele parou quando os próprios testes que inventou passaram (critério de "pronto" definido por ele mesmo); com aceite ele validou exatamente os três casos e valores que eu exigi — a diferença não é testar ou não, é quem define o que conta como aprovado.

**Ex6:** ele perguntou: se deveria só cobrir com testes a validação já existente ou também estendê-la (incluindo um bug real que ele mesmo achou lendo o código — NaN/infinito passando sem erro), se deveria aceitar vírgula decimal, onde colocar os testes, se usaria pytest-cov, se usaria testes via subprocess, e se faltava um limite superior de temperatura.

**Ex7:** ele encontrou sozinho: um caminho de overflow numérico sem teste (`"1e400"` → `inf`), variantes de infinito incompletas, o caso de zero argumentos sem cobertura, asserções de teste frouxas demais, e uma divergência real entre o `[Aceite]` ao pé da letra ("`pytest` roda") e o ambiente real (só `python -m pytest` funciona nesta máquina) — exposta, não mascarada.

**Fechamento:** o `/init` gerou os defeitos **Lint Leakage** (seção inteira de convenções de estilo que um formatador cobriria — e nem havia formatador configurado), **Context Bloat** (resumo dos 7 exercícios duplicando `observacoes.md`/`note_0N.md` em toda sessão) e **Blind Reference** (citava os `note_0N.md` sem dizer quando abri-los), que corrigi assim: removi a seção de estilo, troquei o resumo longo por uma frase dizendo quando abrir cada `note_0N.md`, e mantive só o que tinha sinal real (estrutura de pastas + o aviso sobre `pytest` exigir `python -m` nesta máquina). Detalhes em `pratica-guiada/note_fechamento.md`.
