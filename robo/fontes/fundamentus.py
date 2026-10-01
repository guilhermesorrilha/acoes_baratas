import lxml.html
import pandas as pd
import requests

URL = "https://www.fundamentus.com.br/resultado.php"

CABECALHOS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    )
}

COLUNAS = {
    "Papel": "papel",
    "Cotação": "cotacao",
    "P/L": "p_l",
    "P/VP": "p_vp",
    "PSR": "psr",
    "Div.Yield": "div_yield",
    "P/Ativo": "p_ativo",
    "P/Cap.Giro": "p_cap_giro",
    "P/EBIT": "p_ebit",
    "P/Ativ Circ.Liq": "p_ativ_circ_liq",
    "EV/EBIT": "ev_ebit",
    "EV/EBITDA": "ev_ebitda",
    "Mrg Bruta": "mrg_bruta",
    "Mrg Ebit": "mrg_ebit",
    "Mrg. Líq.": "mrg_liq",
    "Liq. Corr.": "liq_corr",
    "ROIC": "roic",
    "ROE": "roe",
    "Liq.2meses": "liq_media_diaria",
    "Patrim. Líq": "patrim_liq",
    "Dív.Líq/ Patrim.": "div_liq_patrim",
    "Cresc. Rec.5a": "cresc_rec_5a",
}

ZERO_QUER_DIZER_VAZIO = [
    "cotacao", "p_l", "p_vp", "psr", "p_ativo", "p_cap_giro", "p_ebit",
    "p_ativ_circ_liq", "ev_ebit", "ev_ebitda", "mrg_bruta", "mrg_ebit",
    "mrg_liq", "liq_corr", "roic", "roe",
]

MINIMO_DE_LINHAS = 500


def buscar() -> pd.DataFrame:
    tabela = ler_tabela(baixar())
    if len(tabela) < MINIMO_DE_LINHAS:
        raise ValueError(
            f"O Fundamentus devolveu só {len(tabela)} ações (esperado: ~990)."
        )
    return tabela


def baixar() -> bytes:
    resposta = requests.get(URL, headers=CABECALHOS, timeout=60)
    resposta.raise_for_status()
    return resposta.content


def ler_tabela(conteudo: bytes) -> pd.DataFrame:
    html = conteudo.decode("latin-1")
    tabela = lxml.html.fromstring(html).find(".//table[@id='resultado']")
    if tabela is None:
        raise ValueError("A página do Fundamentus veio sem a tabela de ações.")

    cabecalho = [th.text_content().strip() for th in tabela.findall("./thead/tr/th")]
    faltando = [nome for nome in COLUNAS if nome not in cabecalho]
    if faltando:
        raise ValueError(f"Colunas sumiram da tabela do Fundamentus: {faltando}")

    linhas = []
    for tr in tabela.findall("./tbody/tr"):
        celulas = [td.text_content().strip() for td in tr.findall("./td")]
        linha = dict(zip(cabecalho, celulas))
        balao = tr.find("./td/span[@title]")
        linha["empresa"] = balao.get("title").strip() if balao is not None else linha["Papel"]
        linhas.append(linha)

    df = pd.DataFrame(linhas, columns=[*COLUNAS, "empresa"]).rename(columns=COLUNAS)
    for coluna in COLUNAS.values():
        if coluna != "papel":
            df[coluna] = df[coluna].map(para_numero)
    df[ZERO_QUER_DIZER_VAZIO] = df[ZERO_QUER_DIZER_VAZIO].replace(0, float("nan"))
    return df


def para_numero(texto: str) -> float:
    if texto in ("", "-"):
        return float("nan")
    porcentagem = texto.endswith("%")
    numero = float(texto.removesuffix("%").replace(".", "").replace(",", "."))
    return numero / 100 if porcentagem else numero


if __name__ == "__main__":
    tabela = buscar()
    print(f"{len(tabela)} ações\n")
    print(tabela[tabela["papel"].isin(["PETR4", "VALE3", "ITUB4"])].set_index("papel").T)
