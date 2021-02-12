

# **1 - Bibliotecas**

!pip install yfinance --upgrade --no-cache-dir
import yfinance as yf
import pandas_datareader.data as web
yf.pdr_override()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


!pip install git+https://github.com/quantopian/pyfolio
import pyfolio as pf
import warnings
warnings.filterwarnings('ignore')

# **2 - Obtendo e tratando os dados**

tickers = ["ABEV3.SA", "ITSA4.SA", "USIM5.SA", "VALE3.SA", "WEGE3.SA", '^BVSP']

dados_yahoo = web.get_data_yahoo(tickers, period="5y")["Adj Close"]


dados_yahoo

retorno = dados_yahoo.pct_change()
retorno

retorno_acumulado = (1 + retorno).cumprod()
retorno_acumulado.iloc[0] = 1
retorno_acumulado

carteira = 10000*retorno_acumulado.iloc[:,:5]
carteira["saldo"] = carteira.sum(axis=1)
carteira["retorno"] = carteira["saldo"].pct_change()
carteira

# **3 - Resultados**

pf.create_full_tear_sheet(carteira["retorno"], benchmark_rets=retorno["^BVSP"])


fig, ax1 = plt.subplots(figsize=(16,8))
pf.plot_rolling_beta(carteira["retorno"], factor_returns=retorno["^BVSP"], ax=ax1)
plt.ylim((0.8, 1.8))