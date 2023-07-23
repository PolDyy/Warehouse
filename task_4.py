from services.get_data import GetData
from services.table_task_4 import table_task_4

""" 
    Задание: Составить табличку типа 'warehouse_name' , 'product','quantity', 'profit', 
    'percent_profit_product_of_warehouse' 
    (процент прибыли продукта заказанного из определенного склада к прибыли этого склада)
"""


data = GetData.get_data()
df = table_task_4(data)

print(df)
df.to_csv('results/task_4.txt', sep='\t', index=False)


