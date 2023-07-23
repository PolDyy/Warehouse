from services.get_data import GetData
from services.table_task_5 import table_task_5

""" 
    Задание: Взять предыдущую табличку и отсортировать 'percent_profit_product_of_warehouse' по убыванию, 
    после посчитать накопленный процент. Накопленный процент - это новый столбец в этой табличке, который 
    должен называться 'accumulated_percent_profit_product_of_warehouse'. 
    По своей сути это постоянно растущая сумма отсортированного 
    по убыванию столбца 'percent_profit_product_of_warehouse'.
"""

data = GetData.get_data()
df = table_task_5(data)

print(df)
df.to_csv('results/task_5.txt', sep='\t', index=False)
