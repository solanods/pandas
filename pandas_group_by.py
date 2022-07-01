import pandas as pd
import numpy as np
df = pd.DataFrame({'classe': np.array([10, 20, 30, 40, 50]),
                   'dados':[1, 3, 9, 15, 27],
                   'frequência':[2, 3, 2, 3, 2],
                   'fa':[2, 6, 8, 11, 12]})
print(df)

#media da coluna classe com os rótulos da coluna frequencia
grouped = df['classe'].groupby(df['frequência'])
print('média agrupada:', grouped.mean())
print('soma agrupada:', grouped.sum())



#iteração- nesse exemplo vamos agrupar os dados pelos valores de 'frequência'
for name, group in df.groupby('frequência'):
    print(name)
    print('_____________')
    print(group)





