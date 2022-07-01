import pandas as pd
import numpy as np

#criar uma Series
s = pd.Series ([1,2], index = ['a', 'b'])

int_series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

#operações aritiméticas com series
int_series.add(2.5)
int_series.sub(0.7)
int_series.mul(3)
int_series.div(9)

# criar um dicionário
engtosp = {}
engtosp['one'] = 'uno'
engtosp['two'] = 'dos'
engtosp['three'] = 'tres'

#criando com outra sintaxe
engtopt = {'three': 'três', 'one': 'um', 'two': 'dois'}

#retorna as chaves
engtopt.keys()

#retorna os valores
engtopt.values()

#retorna os pares
engtopt.items()

#retorna o valor associado à chave
engtopt.get('one')

#colocar as chaves em uma lista
inventory = {'apples':'430', 'bananas':'312', 'oranges':'525', 'pears':'217'}
ks = list(inventory.keys())

# passando um dict para uma series
population_dict = {'Camboriú': 3833252,
                   'Indaial': 2644819,
                   'Florianópolis': 19552860,
                   'Brusque': 1288213}

population = pd.Series(population_dict)

#criar um dataframe de uma lista
nomes = ['João', 'Fernando', 'Gilberto', 'Felipe', 'Maria']
df = pd.DataFrame(nomes)

# criar um dataframe de um dict
data = {'Nome': ['Henrique', 'Joana', 'Filipe', 'Jane'],
        'Idade':[20, 21, 19, 18]}
df2 = pd.DataFrame(data)

#criar um df de valores
df_num = pd.DataFrame(np.random.rand(3, 2), columns=['foo', 'bar'], index=['a', 'b','c'])

#criar um df de um arquivo csv
dados = pd.read_csv('/home/sol/Documentos/datasets/angulos.csv')


#métodos
dados.head()
dados.sum()
dados.mean()
dados.min()
dados.max()
dados.describe()
dados.shape
dados.index
dados.columns
dados.count()
dados['nova_coluna'] = 'textoaqui'
#dados.plot()
col = ['angulo', 'seno', 'cosseno']
#dados[col].plot





# utilizando query
notas = pd.read_csv('/home/sol/Documentos/datasets/notas.csv')
print(notas.query('produto <= 30'))
print(notas.query('nota_matematica >= 7'))

#filtrar valores pares de uma coluna
print(notas[notas['nota_matematica'] % 2 == 0])

#selecionando com loc
#valores da linha
notas.loc[2]

# valor linha e coluna
notas.loc[6, 'produto']

# seleção de linhas e colunas por índices
dados.iloc[3, 2]











