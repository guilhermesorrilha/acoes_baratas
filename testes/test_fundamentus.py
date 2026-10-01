import math
from pathlib import Path

import pytest

from robo.fontes.fundamentus import ler_tabela, para_numero

AMOSTRA = Path(__file__).parent / "dados" / "fundamentus_amostra.html"


@pytest.fixture
def tabela():
    return ler_tabela(AMOSTRA.read_bytes()).set_index("papel")


def test_numero_no_formato_brasileiro():
    assert para_numero("1.455.190.000,00") == 1_455_190_000
    assert para_numero("4,75") == 4.75
    assert para_numero("-23,98") == -23.98
    assert para_numero("19,69%") == pytest.approx(0.1969)
    assert math.isnan(para_numero("-"))


def test_le_os_numeros_da_petrobras(tabela):
    petr4 = tabela.loc["PETR4"]
    assert petr4["cotacao"] == 49.12
    assert petr4["liq_media_diaria"] == 2_050_300_000
    assert petr4["patrim_liq"] == 480_950_000_000
    assert petr4["roic"] == pytest.approx(0.1969)
    assert petr4["p_cap_giro"] == -23.98


def test_prejuizo_continua_negativo(tabela):
    assert tabela.loc["IRBR3", "p_l"] == -34.31


def test_nome_escondido_da_empresa(tabela):
    assert tabela.loc["PETR3", "empresa"] == "PETROBRAS"
    assert tabela.loc["PETR4", "empresa"] == "PETROBRAS"


def test_acentos(tabela):
    assert tabela.loc["CSTB3", "empresa"] == "COMPANHIA SIDERÚRGICA DE TUBARÃO"


def test_zero_de_banco_vira_vazio(tabela):
    itub4 = tabela.loc["ITUB4"]
    assert math.isnan(itub4["ev_ebit"])
    assert math.isnan(itub4["roic"])
    assert math.isnan(itub4["mrg_ebit"])
    assert itub4["p_l"] == 10.48
    assert itub4["roe"] == pytest.approx(0.2245)


def test_dividendo_zero_continua_zero(tabela):
    assert tabela.loc["HAPV3", "div_yield"] == 0


def test_traco_vira_vazio(tabela):
    assert math.isnan(tabela.loc["PITI4", "div_liq_patrim"])


def test_coluna_que_sumiu_da_erro():
    pagina = AMOSTRA.read_bytes().replace(b">ROIC<", b">Retorno<")
    with pytest.raises(ValueError, match="ROIC"):
        ler_tabela(pagina)


def test_pagina_sem_tabela_da_erro():
    captcha = b"<html><body>Digite os caracteres que voce ve na figura</body></html>"
    with pytest.raises(ValueError, match="sem a tabela"):
        ler_tabela(captcha)
