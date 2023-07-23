from services.get_data import GetData
from services.table_task_6 import table_task_6

""" 
    Задание:Присвоить A,B,C - категории на основании значения накопленного процента 
    ('accumulated_percent_profit_product_of_warehouse'). 
    Если значение накопленного процента меньше или равно 70, то категория A.
    Если от 70 до 90 (включая 90), то категория Б. Остальное - категория C. 
    Новый столбец обозначить в таблице как 'category'
"""

data = GetData.get_data()
df = table_task_6(data)

print(df)
df.to_csv('results/task_6.txt', sep='\t', index=False)
