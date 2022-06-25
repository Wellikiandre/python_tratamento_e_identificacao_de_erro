# %%

# imports
import requests
import backoff
import json
# %%
url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
ret = requests.get(url)

# %%
# Usando decorador


@backoff.on_exception(backoff.expo, (), max_tries=1)
def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except Exception as e:
            print(f"Falhou na Função : {func.__name__} , no Argumento: {e}  ")
    return inner_func

# %%


@error_check
def cotacaomoeda(valor, moeda):
    url = f'''https://economia.awesomeapi.com.br/last/{moeda}'''
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-', '')]
    print(
        f" {valor} {moeda[:3]}, hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}. ")


# %%
cotacaomoeda(20, 'USD-BRL')
cotacaomoeda(10, 'USD-BRL')
cotacaomoeda(15, 'TPP-TPP')
cotacaomoeda(20, 'MOEDATESTE')
cotacaomoeda(10, 'BRL-USD')
