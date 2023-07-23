from services.get_data import GetData
from services.table_task_3 import table_task_3

"""
    Задание: Составить табличку со столбцами 'order_id' (id заказа) и 'order_profit' (прибыль полученная с заказа). 
    А также вывести среднюю прибыль заказов
"""

data = GetData.get_data()
df, average_profit = table_task_3(data)

print(df)
print(average_profit)

df.to_csv('results/task_3_table.txt', sep='\t', index=False)

