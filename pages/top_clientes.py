import sqlite3
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

conn = sqlite3.connect("erp_finance.db", detect_types = sqlite3.PARSE_DECLTYPES)

query = """
SELECT c.nome, SUM(cr.valor) AS total_receita
FROM contas_receber cr
JOIN clientes c ON cr.cliente_id = c.id
GROUP BY cr.cliente_id
ORDER BY total_receita DESC
LIMIT 5;
"""

df = pd.read_sql_query(query, conn)

conn.close()

plt.figure(figsize=(10, 6))
grafico = plt.bar(df['nome'], df['total_receita'], color='skyblue')
plt.xlabel('Cliente')
plt.ylabel('Total de Receita')
plt.title('Top 5 Clientes com Maior Receita')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()  # Ajusta o layout garantindo que as legendas não fiquem cortadas
st.pyplot(plt)
