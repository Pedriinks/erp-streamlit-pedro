import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

conn = sqlite3.connect("erp_finance.db", detect_types = sqlite3.PARSE_DECLTYPES)
    
# As clausulas Where sao para pegar o mes atual
query_receitas = """
SELECT SUM(valor) AS total_receitas
FROM contas_receber
WHERE strftime('%Y-%m', vencimento) = strftime('%Y-%m', 'now')
"""

query_despesas = """
SELECT SUM(valor) AS total_despesas
FROM contas_pagar
WHERE strftime('%Y-%m', vencimento) = strftime('%Y-%m', 'now')
"""

total_receitas = pd.read_sql_query(query_receitas, conn).iloc[0, 0] or 0
total_despesas = pd.read_sql_query(query_despesas, conn).iloc[0, 0] or 0

conn.close()

categorias = ['Receitas', 'Despesas']

valores = [total_receitas, total_despesas]

plt.figure(figsize=(8, 6))
plt.bar(categorias, valores, color=['skyblue', 'salmon'])
plt.xlabel('Categoria')
plt.ylabel('Valor (R$)')
plt.title('Comparação Receita vs Despesa - Mês Atual')
plt.tight_layout()
st.pyplot(plt)
