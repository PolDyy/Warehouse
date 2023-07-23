import numpy as np
from pandas import DataFrame

from services.table_task_5 import table_task_5


def table_task_6(data: dict) -> DataFrame:
    """ Метод формирования таблицы согласно условию шестой задачи"""

    df = table_task_5(data)
    conditions = [df['accumulated_percent_profit_product_of_warehouse'] <= 70,
                  (df['accumulated_percent_profit_product_of_warehouse'] > 70) & (
                              df['accumulated_percent_profit_product_of_warehouse'] <= 90)]
    choices = ['A', 'B']
    df['category'] = np.select(conditions, choices, default='C')
    return df
