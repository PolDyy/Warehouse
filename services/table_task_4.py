import pandas as pd
from pandas import DataFrame


def table_task_4(data: dict) -> DataFrame:
    """ Метод формирования таблицы согласно условию четвертой задачи"""

    df = pd.json_normalize(data, record_path='products', meta=['order_id', 'warehouse_name', 'highway_cost'])

    df['profit'] = (df['price'] + df['highway_cost']) * df['quantity']

    grouped_df = df.groupby(['warehouse_name', 'product']).agg({
        'quantity': 'sum',
        'profit': 'sum'
    }).reset_index()

    grouped_df['warehouse_profit'] = grouped_df.groupby('warehouse_name')['profit'].transform('sum')

    grouped_df['percent_profit_product_of_warehouse'] = grouped_df['profit'] / grouped_df['warehouse_profit'] * 100
    grouped_df['percent_profit_product_of_warehouse'] = grouped_df['percent_profit_product_of_warehouse'].astype(float)

    result_df = grouped_df[['warehouse_name', 'product', 'quantity', 'profit', 'percent_profit_product_of_warehouse']]

    return result_df
