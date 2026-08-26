# Resposta ao plano do Exercício 6

1. Estenda a validação — cubra também o caso de NaN/infinito que você encontrou.
2. Mantenha a rejeição do formato decimal brasileiro como está; não é o foco desta tarefa.
3. Arquivo único `test_converte.py` ao lado do script, sem pasta `tests/`.
4. Só `pytest` puro, sem `pytest-cov`.
5. Não precisa de testes via `subprocess`; testar as funções internas e `main()` diretamente é suficiente.
6. Não é necessário limite superior de temperatura.

[Aceite]
1. `pytest` roda dentro de `pratica-guiada/ex6-7` sem falhas.
2. Valor `"nan"`, `"inf"` e `"-inf"` são rejeitados com mensagem de erro clara (não podem mais atravessar a validação em silêncio).
3. Os testes cobrem, no mínimo: conversão correta nos 3 pares de unidades (nos dois sentidos), unidade inválida, valor não numérico, valor abaixo do zero absoluto, e número de argumentos incorreto.
4. Os 3 casos de aceite originais do Exercício 1 continuam funcionando sem regressão:
   - `python converte.py 100 C F` → `212.0`
   - valor abaixo de -273.15 C é recusado
   - unidade desconhecida lista as unidades válidas

Pode implementar.
