import pandas as pd

pd.set_option('display.max_rows', 3000)
df = pd.read_csv('databases/progress.opera____o_de_trens.csv')

#renomear uma coluna
df = df.rename({'Unnamed: 0': 'Nome completo'}, axis = 1)
#remover as colunas com base na string
df.drop([col for col in df.columns if "Unnamed" in col], axis=1, inplace=True)
# Ordena pelo campo nome e salva em um novo DataFrame
df = df.sort_values(by='Nome completo')
#normalizando as strings da coluna nome
df['Nome completo'] = df['Nome completo'].str.title()
#transpor o df inteiro
df = df.T
#passar a primeira linha para nome de colunas
df.columns = df.iloc[0]
#remover a primeira linha
df = df.iloc[1:]
#função lambda para contagem de porcentagem de atividades concluídas
f = lambda y: y.str.contains('Concluído').sum()/len(df)*100
porcentagem_conclusao_aluno = df.apply(f)
porcentagem_conclusao_aluno = porcentagem_conclusao_aluno.to_frame().round(decimals=2)
#enviar a saida para arquivo excel local
porcentagem_conclusao_aluno.to_excel('moodle_rate_setra.xlsx')