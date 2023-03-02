import pandas as pd

# Dados de exemplo
data = {'tensao_ac_l1': [220, 230, 240],
        'tensao_ac_l2': [210, 220, 230],
        'tensao_ac_l3': [215, 225, 235],
        'corrente_ac_l1': [1.5, 2.0, 2.5],
        'corrente_ac_l2': [1.4, 1.9, 2.4],
        'energia_ac_l1': [100, 200, 300],
        'energia_ac_l2': [150, 250, 350],
        'energia_ac_l3': [120, 220, 320],
        'potencia_ac_l1': [1000, 1500, 2000],
        'potencia_ac_l2': [1200, 1700, 2200],
        'potencia_ac_l3': [1100, 1600, 2100]}

# Cria um dataframe a partir dos dados
df = pd.DataFrame(data)

# Gera estatísticas descritivas
stats = df.describe()

# Adiciona unidades
units = {'tensao_ac_l1': 'V',
         'tensao_ac_l2': 'V',
         'tensao_ac_l3': 'V',
         'corrente_ac_l1': 'A',
         'corrente_ac_l2': 'A',
         'energia_ac_l1': 'kWh',
         'energia_ac_l2': 'kWh',
         'energia_ac_l3': 'kWh',
         'potencia_ac_l1': 'W',
         'potencia_ac_l2': 'W',
         'potencia_ac_l3': 'W'}

for col in df.columns:
    stats.loc['unit', col] = units[col]

# Salva o dataframe em um arquivo CSV
df.to_csv('dados.csv', index=False)
