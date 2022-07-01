import pandas as pd
from datetime import  datetime

df_logs = pd.read_csv('databases/logs_004 - Marcha à Ré_20220620-1120.csv')
#tratamento dos dados
df_logs['Nome completo'] = df_logs['Nome completo'].str.title()
interacoes_aluno = df_logs['Nome completo'].value_counts()
atividades_mais_acessadas = df_logs['Contexto do Evento'].value_counts()
total_interacoes = interacoes_aluno.sum()
date = datetime.now()
# Transforma a coluna para hora
df_logs['Hora'] = pd.to_datetime(df_logs['Hora'])
df_logs['Data'] = df_logs['Hora'].dt.strftime('%Y-%m-%d')
interacoes_por_data = df_logs.groupby('Data')['Nome completo'].value_counts()
eventos_por_aluno = df_logs.groupby('Nome do evento')['Nome completo'].value_counts()

# Mandar as series para uma tabela pivot com várias sheets
date = datetime.now()
with pd.ExcelWriter(f'moodle_logs_table_pivot_{date}.xlsx') as writer:
    interacoes_aluno.to_excel(writer, sheet_name='n_interações')
    atividades_mais_acessadas.to_excel(writer, sheet_name='atividades')
    interacoes_por_data.to_excel(writer, sheet_name='interações por data')
    eventos_por_aluno.to_excel(writer, sheet_name='eventos por aluno')

















#with open ('/home/sol/Downloads/logs.text', 'w') as file:
    #file.write(str(df_logs.groupby('Data')['Nome completo'].value_counts()))




































