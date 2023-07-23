from services.table_task_2 import table_task_2
from services.get_data import GetData


"""
    Задание: Найти суммарное количество , суммарный доход , суммарный расход и суммарную прибыль для каждого товара 
    (представить как таблицу со столбцами 'product', 'quantity', 'income', 'expenses', 'profit')
"""

data = GetData.get_data()
df = table_task_2(data)

print(df)
df.to_csv('results/task_2.txt', sep='\t', index=False)
