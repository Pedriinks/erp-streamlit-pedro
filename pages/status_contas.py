import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect("erp_finance.db", detect_types = sqlite3.PARSE_DECLTYPES)

query_pagar = """
SELECT status, SUM(valor) AS total
FROM contas_pagar
WHERE status IN ('Pendente', 'Pago')
GROUP BY status
"""

query_receber = """
SELECT status, SUM(valor) AS total
FROM contas_receber
WHERE status IN ('Pendente', 'Recebido')
GROUP BY status
"""

df_pagar = pd.read_sql_query(query_pagar, conn)
df_receber = pd.read_sql_query(query_receber, conn)

conn.close()

df_pagar['Categoria'] = 'Contas a Pagar'
df_receber['Categoria'] = 'Contas a Receber'

df = pd.concat([df_pagar, df_receber])

plt.figure(figsize = (10, 6))
for categoria in df['Categoria'].unique():
    categoria_df = df[df['Categoria'] == categoria]
    plt.bar(categoria_df['status'] + " - " + categoria_df['Categoria'],
            categoria_df['total'], label = categoria)

plt.xlabel('Status das Contas')
plt.ylabel('Valor Total (R$)')
plt.title('Status das Contas a Pagar e a Receber')
plt.xticks(rotation = 45, ha = "right")
plt.tight_layout()
st.pyplot(plt)