import pandas as pd

from services.get_data import GetData

""" 
    Задание: Найти тариф стоимости доставки для каждого склада 
    Комментарий: Условие задания понял как 'Найти сколько каждый склад потратил на доставку'
"""


df = pd.json_normalize(GetData.get_data())

tariffs = df.groupby('warehouse_name')['highway_cost'].sum()
tariffs = tariffs.to_frame().reset_index()
print(tariffs)
tariffs.to_csv('results/task_1.txt', sep='\t', index=False)
