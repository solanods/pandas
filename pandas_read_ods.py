import pandas as pd
import ezodf

def read_ods(filename, sheet_no=0, header=0):
    tab = ezodf.opendoc(filename=filename).sheets[sheet_no]
    return pd.DataFrame({col[header].value:[x.value for x in col[header+1:]]
                         for col in tab.columns()})

df = read_ods('cpf.ods')
cpf_list = list(df['cpf'])
print(cpf_list)

df2 = read_ods('cpf.ods', sheet_no=1)
print(df2)