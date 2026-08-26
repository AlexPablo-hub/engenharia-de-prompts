# Clarificações — Exercício 8

Perguntas levantadas pelo agente em modo Plan (sessão nova, a partir de `prompt-final.md` entregando `spec.md`), e as respostas do grupo. Nenhum arquivo de código foi criado nessa sessão de planejamento — confirmado.

O plano completo (12 passos) que acompanhou essas perguntas está registrado abaixo das respostas, para referência.

## Perguntas e respostas

**1. Framework de frontend?**
→ React.

**2. Como o frontend fala com os dados — API própria ou direto no Supabase?**
→ SPA fala direto com Supabase (SDK), sem API própria. Regras de negócio em funções/views Postgres.

**3. Gerenciador de pacotes?**
→ npm.

**4. Tabela de professores própria, ou aponta direto pra `auth.users`?**
→ Tabela própria `professores`, simétrica a `alunos` (id interno + id do Supabase Auth).

**5. Cadastro do professor — self-signup ou provisionamento manual?**
→ Self-signup (email/senha via Supabase Auth).

**6. Quem vincula o aluno à conta do Supabase Auth, e quando?**
→ Professor cadastra o aluno (nome); sistema gera convite para o aluno criar a própria senha, e o vínculo é feito nesse momento.

**7. Como o sistema distingue professor de aluno no login?**
→ Pela existência da linha: se o id do usuário aparece em `professores`, é professor; se aparece em `alunos`, é aluno. Sem tabela de papel separada.

**8. Onde as regras de acesso (professor só vê as próprias turmas, aluno só a própria linha) são impostas?**
→ Row Level Security (RLS) do Supabase, no próprio banco.

**9. "Nota ausente/não lançada" — linha não existe, ou linha existe com `nota = NULL`?**
→ Linha não existe. Só há registro em `avaliacoes` quando a nota é lançada.

**10. Pode haver mais de uma nota do mesmo tipo pro mesmo aluno?**
→ Não — constraint única `(aluno, tipo)`.

**11. Pesos das avaliações — fração (0-1) ou percentual (0-100)?**
→ Fração 0-1, armazenado assim; interface pode exibir como % sem mudar o armazenamento.

**12. Tolerância ao validar se a soma dos pesos bate 1.0/100%?**
→ Pequena margem (ex.: ±0,001), para não rejeitar por erro de ponto flutuante.

**13. Faixa de nota válida (0-10) é fixa ou configurável por turma?**
→ Fixa, 0 a 10 para todo o sistema.

**14. Uma nota já lançada pode ser editada/excluída depois?**
→ Sim, o professor pode editar ou excluir; médias e estatísticas recalculam automaticamente.

**15. Pesos/limites de uma turma podem mudar depois que já existe nota lançada?**
→ Sim, e a edição recalcula a média e a classificação de todos os alunos da turma com a nova regra.

**16. Ao excluir aluno ou turma, o que acontece com as avaliações relacionadas?**
→ Cascata: excluir aluno remove suas avaliações; excluir turma remove alunos e avaliações da turma.

**17. Estatísticas da turma — recalculadas sob demanda ou persistidas via trigger?**
→ Sob demanda, ao carregar a tela (view/query direta, sem trigger).

**18. O aluno vê estatísticas agregadas da turma, ou só a própria situação?**
→ Só a própria situação — mantém exatamente o que a seção 2 do `spec.md` já garantia, sem expandir escopo.

**19. A lista de "a menos de 0,5 ponto do limite de aprovação" inclui quem?**
→ Só quem está abaixo do limite, perto de aprovar (não inclui quem está acima em risco de cair).

**20. Nomes duplicados (aluno/turma) são permitidos?**
→ Sim — nome é só exibição, o `id` é o identificador real.

**21. Onde o frontend fica hospedado?**
→ Vercel.

## Plano completo do agente (referência)

1. Decidir a stack e a forma de comunicação SPA↔dados — **resolvido**: React, Supabase direto (sem API própria), npm.
2. Modelar o schema Postgres/Supabase — **resolvido**: perguntas 9-12.
3. Definir autenticação e autorização — **resolvido**: perguntas 4-8.
4. Implementar as regras de cálculo (Seção 4 do spec) — atenção ao arredondamento "0,005 sobe": a maioria das linguagens usa round-half-even por padrão e ponto flutuante binário não representa 0,005 exatamente; vai precisar de tipo `numeric`/decimal no Postgres, não `float`.
5. Implementar as estatísticas por turma — **resolvido**: pergunta 17-19.
6. Implementar validação de entrada — **resolvido**: perguntas 12-13, 20.
7. Desenhar a API (ou, com a decisão da pergunta 2, desenhar as views/funções Postgres que o frontend chama).
8. Construir as telas do professor (CRUD + dashboard).
9. Construir a tela do aluno (somente leitura).
10. Revisar contra a seção 7 do spec.md ("fora de escopo") antes de fechar o plano.
11. Testes: cálculo/arredondamento, estatísticas, validações, e RLS (garantir que um aluno não lê dados de outro aluno/turma).
12. Deploy — **resolvido**: pergunta 21 (Vercel para o frontend; Supabase já hospeda banco/auth).
