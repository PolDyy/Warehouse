from pandas import DataFrame

from services.table_task_4 import table_task_4


def table_task_5(data: dict) -> DataFrame:
    """ Метод формирования таблицы согласно условию пятой задачи"""
    df = table_task_4(data)

    result_df = df.sort_values(by=['warehouse_name', 'percent_profit_product_of_warehouse'], ascending=[True, False])
    result_df['accumulated_percent_profit_product_of_warehouse'] =\
        result_df.groupby('warehouse_name')['percent_profit_product_of_warehouse'].cumsum()

    return result_df

