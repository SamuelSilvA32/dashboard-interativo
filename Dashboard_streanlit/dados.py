import numpy as np
import pandas as pd
import streamlit as st

@st.cache_data
def criar_dados():
    np.random.seed(42)
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho','julho','agosto','setembro','outubro','novembro','dezembro']
    
    dados = {
        'Mês': meses,
        'Vendas':[45000, 52000, 48000, 61000, 55000, 67000, 52000, 45000, 45000, 45000, 45000, 48000],
        'Clientes':[450, 520, 480, 610, 550, 670, 520, 450, 450, 450, 450, 480],
        'notebooks':[15000, 18000, 16000, 21000, 19000, 23000, 16000, 15000, 15000, 15000, 15000, 18000],
        'smartphones':[20000, 22000, 21000, 25000, 23000, 28000, 21000, 20000, 20000, 20000, 20000, 22000],
        'tvs': [10000, 12000, 11000, 15000, 13000, 16000, 11000, 10000, 10000, 10000, 10000, 12000]
    }
    return pd.DataFrame(dados)

df = criar_dados()
