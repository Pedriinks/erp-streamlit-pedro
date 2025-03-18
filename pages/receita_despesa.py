import pandas as pd
import streamlit as st
import sqlite3
import plotly.express as px

conn = sqlite3.connect("erp_finance.db", detect_types = sqlite3.PARSE_DECLTYPES)

receita = pd.read_sql_query("SELECT * FROM contas_receber", conn)

despesas = pd.read_sql_query("SELECT * FROM contas_pagar", conn)

#grafico so para testar se estava tudo certo com as queries
grafico_pizza = px.pie(receita, names = "status", title = "Teste")

grafico_barras = px.bar(receita, x = "status", y = "valor", title = "Receita x Despesa")

st.plotly_chart(grafico_barras)