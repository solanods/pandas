import pandas as pd
from pandas.io.sql import to_sql
from sqlalchemy import create_engine, types
from itertools import chain
import mysql.connector

df_teste = pd.read_csv('/home/sol/PycharmProjects/pandas/moodle/databases/logs_004 - Marcha à Ré_20220620-1120.csv')
#tratamento dos dados brutos
#divisão das colunas em data e hora e realocação
df_teste['Hora'] = pd.to_datetime(df_teste['Hora'])
df_teste['Data'] = df_teste['Hora'].dt.strftime('%Y-%m-%d')
df_teste['Hora'] = df_teste['Hora'].dt.strftime('%H:%M:%S')
df_teste = df_teste[['Data', 'Hora', 'Nome completo', 'Usuário afetado', 'Contexto do Evento', 'Componente', 'Nome do evento', 'Descrição', 'Origem', 'endereço IP']]
df = df_teste[['Data', 'Hora', 'Nome completo','Nome do evento']]

#==========================CONEXAO==========================================================================================
# iniciando a conexão com o banco usando sqlalchemy
# atenção à string passada na função abaixo:  user  pass        schema
conn = create_engine('mysql+mysqlconnector://root:Macondo2022@@localhost/projeto_api', connect_args={'auth_plugin': 'mysql_native_password'})

# Método to_sql transforma o DataFrame em um insert automaticamente, passando a engine criada acima para conectar ao banco

#-----------------table_name------database_name--------
to_sql(df_teste, 'logs_re', conn, schema='projeto_api')



