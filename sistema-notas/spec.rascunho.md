# Especificação — Sistema de Acompanhamento de Notas

> RASCUNHO gerado a partir das respostas da entrevista guiada. Revise cada seção e reescreva o que não estiver do seu jeito antes de promover este conteúdo a `spec.md` — o arquivo final precisa ser seu.

## 1. Visão geral

Sistema web para professores acompanharem notas de turmas: cadastro de turmas, alunos e avaliações, cálculo de médias ponderadas com regras por turma, classificação de situação, e estatísticas atualizadas a cada lançamento.

## 2. Plataforma

**Web.** [DECIDIR: é uma aplicação de página única (SPA) com backend de API, ou server-rendered tradicional (cada ação recarrega a página)? Quem acessa — só o professor, ou também alunos consultando a própria situação? Precisa de login/autenticação, ou é uso local de uma única pessoa?]

## 3. Persistência

**Firebase** (assumindo **Cloud Firestore**, o banco de documentos do Firebase — é o mais comum para dados estruturados com relações como este; [CONFIRMAR: é isso mesmo, ou a intenção era Firebase Realtime Database? São bancos diferentes]). Dados sobrevivem entre execuções porque ficam na nuvem, não em arquivo local — isso muda o "persiste entre execuções" do enunciado para "persiste entre sessões/dispositivos", o que é ainda mais forte.

Coleções mínimas (ajustar conforme achar necessário):
- **turmas**: id, nome, pesos das avaliações (ex: {"prova1": 0.3, "prova2": 0.3, "trabalho": 0.4} — soma deve dar 1.0 ou 100%), limite de aprovação, limite de exame (faixa entre reprovado e aprovado direto).
- **alunos**: id, nome, id da turma (referência ao documento da turma).
- **avaliacoes**: id, id do aluno, id da turma, tipo/nome da avaliação (deve bater com uma das chaves de peso da turma), nota (pode estar ausente = "não lançada") — ou, alternativa mais idiomática em Firestore: notas como subcoleção dentro do documento do aluno. [DECIDIR: qual das duas modelagens usar]

[DECIDIR: os pesos e limites de uma turma podem ser alterados depois que já existem avaliações lançadas? O que acontece com as médias já calculadas nesse caso?]

[DECIDIR: as estatísticas da seção 5 (média, mediana, distribuição) são recalculadas no cliente a cada leitura, ou salvas de volta no Firestore a cada lançamento de nota (ex: via Cloud Function)? Isso muda bastante a arquitetura.]

[DECIDIR: regras de segurança do Firestore — mesmo sendo uso de um único professor, o Firestore por padrão fica com leitura/escrita bloqueadas; alguma autenticação (Firebase Auth) é necessária para liberar acesso, ou vai ficar em modo de teste/aberto?]

## 4. Regras de cálculo

- **Média ponderada por aluno**: soma de (nota × peso) / soma dos pesos das avaliações **já lançadas** — mas ver a regra de nota pendente abaixo, que já resolve isso tratando pendente como zero (então na prática a média sempre usa a soma total dos pesos da turma, mesmo com nota faltando).
- **Nota pendente (avaliação ainda não lançada): tratada como 0** no cálculo da média. [Confirmar: isso vale desde o primeiro dia da turma, mesmo antes de qualquer prazo de entrega? Ou só depois de uma data limite?]
- **Arredondamento**: 2 casas decimais, arredondamento matemático padrão (0.005 arredonda para cima).
- **Classificação**: aprovado / exame / reprovado, conforme os limites definidos por turma (ex: média ≥ limite_aprovacao → aprovado; limite_exame ≤ média < limite_aprovacao → exame; média < limite_exame → reprovado). [DECIDIR: os limites são os mesmos "≥" nos dois pontos de corte, ou algum é estrito "<"? O enunciado não define isso.]

## 5. Estatísticas (recalculadas a cada lançamento de nota)

Por turma:
- Média das médias dos alunos.
- Mediana das médias dos alunos.
- Distribuição por situação (quantos aprovados / exame / reprovados).
- Lista de alunos a menos de 0,5 ponto do limite de aprovação (nos dois sentidos? só abaixo, querendo aprovar? ou também logo acima, em risco de cair? — [DECIDIR]).

## 6. Validação de entrada

- Nota deve estar em uma faixa válida (ex: 0 a 10) — rejeitar fora disso com mensagem dizendo qual o intervalo aceito.
- Pesos de uma turma devem somar 1.0 (ou 100%) — rejeitar cadastro/edição de turma que não bata essa soma, com mensagem mostrando a soma atual.
- Nome de aluno/turma não pode ser vazio.
- Avaliação lançada para um tipo que não existe nos pesos da turma é rejeitada, listando os tipos válidos.
- [Outras validações que você achar necessárias]

## 7. Fora de escopo (o que este sistema explicitamente NÃO faz)

[DECIDIR: ex. não faz autenticação multi-usuário / não gera boletim em PDF / não envia notificação por email / etc. — liste o que você está deliberadamente deixando de fora, para não virar ambiguidade depois]
