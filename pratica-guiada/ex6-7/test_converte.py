#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_converte.py - Testes automatizados (pytest) para converte.py.

Cobre:
    - As funções de conversão pura (para_celsius, de_celsius, converter)
      nos 3 pares de unidades, nos dois sentidos, incluindo identidades.
    - As funções de validação (validar_unidade, validar_valor,
      validar_fisicamente), incluindo o caso de NaN/infinito.
    - main() de ponta a ponta, cobrindo os casos de aceite originais do
      Exercício 1 (conversão correta, zero absoluto, unidade desconhecida)
      e o número de argumentos incorreto.

Como o script usa `erro()` -> `sys.exit(1)` para sinalizar falhas de
validação, os testes de caminho de erro usam `pytest.raises(SystemExit)`
combinado com `capsys` para inspecionar a mensagem impressa em stderr.
"""

import pytest

import converte


# ---------------------------------------------------------------------------
# Funções de conversão pura
# ---------------------------------------------------------------------------

class TestConversao:
    def test_celsius_para_fahrenheit(self):
        assert converte.converter(100, "C", "F") == pytest.approx(212.0)

    def test_fahrenheit_para_celsius(self):
        assert converte.converter(212, "F", "C") == pytest.approx(100.0)

    def test_celsius_para_kelvin(self):
        assert converte.converter(0, "C", "K") == pytest.approx(273.15)

    def test_kelvin_para_celsius(self):
        assert converte.converter(273.15, "K", "C") == pytest.approx(0.0)

    def test_fahrenheit_para_kelvin(self):
        assert converte.converter(32, "F", "K") == pytest.approx(273.15)

    def test_kelvin_para_fahrenheit(self):
        assert converte.converter(273.15, "K", "F") == pytest.approx(32.0)

    def test_identidade_celsius(self):
        assert converte.converter(25, "C", "C") == pytest.approx(25.0)

    def test_identidade_fahrenheit(self):
        assert converte.converter(98.6, "F", "F") == pytest.approx(98.6)

    def test_identidade_kelvin(self):
        assert converte.converter(300, "K", "K") == pytest.approx(300.0)


# ---------------------------------------------------------------------------
# validar_unidade
# ---------------------------------------------------------------------------

class TestValidarUnidade:
    @pytest.mark.parametrize(
        "entrada,esperado",
        [
            ("C", "C"),
            ("c", "C"),
            ("F", "F"),
            ("f", "F"),
            ("K", "K"),
            ("k", "K"),
            (" c ", "C"),
        ],
    )
    def test_unidades_validas_sao_normalizadas(self, entrada, esperado):
        assert converte.validar_unidade(entrada) == esperado

    def test_unidade_desconhecida_encerra_programa_com_codigo_1(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            converte.validar_unidade("X")
        assert exc_info.value.code == 1

    def test_unidade_desconhecida_lista_unidades_validas(self, capsys):
        with pytest.raises(SystemExit):
            converte.validar_unidade("X")
        saida = capsys.readouterr()
        assert "Erro" in saida.err
        assert "C" in saida.err and "F" in saida.err and "K" in saida.err


# ---------------------------------------------------------------------------
# validar_valor
# ---------------------------------------------------------------------------

class TestValidarValor:
    def test_numero_inteiro_valido(self):
        assert converte.validar_valor("100") == pytest.approx(100.0)

    def test_numero_negativo_valido(self):
        assert converte.validar_valor("-40") == pytest.approx(-40.0)

    def test_numero_com_ponto_decimal(self):
        assert converte.validar_valor("36.5") == pytest.approx(36.5)

    def test_texto_nao_numerico_encerra_programa(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            converte.validar_valor("abc")
        assert exc_info.value.code == 1
        saida = capsys.readouterr()
        assert "não é um número válido" in saida.err

    def test_virgula_decimal_continua_rejeitada(self, capsys):
        # Formato brasileiro ("10,5") permanece fora de escopo: deve ser
        # tratado como número inválido, sem conversão automática de vírgula.
        with pytest.raises(SystemExit):
            converte.validar_valor("10,5")
        saida = capsys.readouterr()
        assert "não é um número válido" in saida.err

    @pytest.mark.parametrize("texto", ["nan", "NaN", "NAN", "-nan"])
    def test_nan_e_rejeitado(self, texto, capsys):
        with pytest.raises(SystemExit) as exc_info:
            converte.validar_valor(texto)
        assert exc_info.value.code == 1
        saida = capsys.readouterr()
        assert "não é uma temperatura numérica válida" in saida.err

    @pytest.mark.parametrize(
        "texto",
        [
            "inf",
            "Infinity",
            "-inf",
            "-Infinity",
            "+inf",
            "+Infinity",
            "INF",
        ],
    )
    def test_infinito_e_rejeitado(self, texto, capsys):
        with pytest.raises(SystemExit) as exc_info:
            converte.validar_valor(texto)
        assert exc_info.value.code == 1
        saida = capsys.readouterr()
        assert "não é uma temperatura numérica válida" in saida.err

    def test_overflow_numerico_para_infinito_e_rejeitado(self, capsys):
        # Um número finito, porém grande demais para representar em float,
        # "estoura" silenciosamente para infinito em Python (float("1e400")
        # == inf, sem lançar ValueError). Este é o caso realista que motivou
        # a validação de NaN/infinito: um usuário digitando um valor grande
        # demais, não literalmente a palavra "inf".
        with pytest.raises(SystemExit) as exc_info:
            converte.validar_valor("1e400")
        assert exc_info.value.code == 1
        saida = capsys.readouterr()
        assert "não é uma temperatura numérica válida" in saida.err


# ---------------------------------------------------------------------------
# validar_fisicamente
# ---------------------------------------------------------------------------

class TestValidarFisicamente:
    def test_valores_acima_do_zero_absoluto_nao_geram_erro(self):
        # Não deve levantar SystemExit.
        converte.validar_fisicamente(25.0, "C")
        converte.validar_fisicamente(0.0, "K")
        converte.validar_fisicamente(32.0, "F")

    def test_valor_exatamente_no_zero_absoluto_e_aceito(self):
        converte.validar_fisicamente(-273.15, "C")
        converte.validar_fisicamente(0.0, "K")
        converte.validar_fisicamente(-459.67, "F")

    @pytest.mark.parametrize(
        "valor,unidade",
        [
            (-300, "C"),
            (-1, "K"),
            (-500, "F"),
        ],
    )
    def test_valor_abaixo_do_zero_absoluto_encerra_programa(
        self, valor, unidade, capsys
    ):
        with pytest.raises(SystemExit) as exc_info:
            converte.validar_fisicamente(valor, unidade)
        assert exc_info.value.code == 1
        saida = capsys.readouterr()
        assert "zero absoluto" in saida.err


# ---------------------------------------------------------------------------
# main() - testes de ponta a ponta (equivalem ao uso via CLI)
# ---------------------------------------------------------------------------

class TestMain:
    def test_criterio_de_aceite_100_celsius_para_fahrenheit(self, capsys):
        """Critério de aceite original: `python converte.py 100 C F` -> 212.0"""
        converte.main(["100", "C", "F"])
        saida = capsys.readouterr()
        assert saida.out.strip() == "212.0"

    def test_criterio_de_aceite_abaixo_do_zero_absoluto_e_recusado(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            converte.main(["-300", "C", "F"])
        assert exc_info.value.code == 1
        saida = capsys.readouterr()
        assert "zero absoluto" in saida.err

    def test_criterio_de_aceite_unidade_desconhecida_lista_unidades_validas(
        self, capsys
    ):
        with pytest.raises(SystemExit) as exc_info:
            converte.main(["100", "X", "F"])
        assert exc_info.value.code == 1
        saida = capsys.readouterr()
        assert "Unidades válidas" in saida.err
        assert "C" in saida.err and "F" in saida.err and "K" in saida.err

    def test_numero_de_argumentos_incorreto_zero(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            converte.main([])
        assert exc_info.value.code == 1
        saida = capsys.readouterr()
        assert "número de argumentos inválido" in saida.err

    def test_numero_de_argumentos_incorreto_poucos(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            converte.main(["100", "C"])
        assert exc_info.value.code == 1
        saida = capsys.readouterr()
        assert "número de argumentos inválido" in saida.err

    def test_numero_de_argumentos_incorreto_muitos(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            converte.main(["100", "C", "F", "extra"])
        assert exc_info.value.code == 1
        saida = capsys.readouterr()
        assert "número de argumentos inválido" in saida.err

    def test_valor_nao_numerico_via_main(self, capsys):
        with pytest.raises(SystemExit):
            converte.main(["abc", "C", "F"])
        saida = capsys.readouterr()
        assert "não é um número válido" in saida.err

    @pytest.mark.parametrize("texto", ["nan", "inf", "-inf", "+inf"])
    def test_nan_e_infinito_via_main_sao_rejeitados(self, texto, capsys):
        with pytest.raises(SystemExit) as exc_info:
            converte.main([texto, "C", "F"])
        assert exc_info.value.code == 1
        saida = capsys.readouterr()
        assert "não é uma temperatura numérica válida" in saida.err

    def test_overflow_numerico_via_main_e_rejeitado(self, capsys):
        with pytest.raises(SystemExit) as exc_info:
            converte.main(["1e400", "C", "F"])
        assert exc_info.value.code == 1
        saida = capsys.readouterr()
        assert "não é uma temperatura numérica válida" in saida.err

    def test_unidade_minuscula_e_aceita_via_main(self, capsys):
        converte.main(["0", "c", "f"])
        saida = capsys.readouterr()
        assert saida.out.strip() == "32.0"

    @pytest.mark.parametrize(
        "valor,origem,destino,esperado",
        [
            ("100", "C", "F", "212.0"),
            ("32", "F", "C", "0.0"),
            ("0", "C", "K", "273.15"),
            ("273.15", "K", "C", "0.0"),
            ("32", "F", "K", "273.15"),
            ("273.15", "K", "F", "32.0"),
        ],
    )
    def test_main_converte_corretamente_todos_os_pares_de_unidades(
        self, valor, origem, destino, esperado, capsys
    ):
        converte.main([valor, origem, destino])
        saida = capsys.readouterr()
        assert saida.out.strip() == esperado
