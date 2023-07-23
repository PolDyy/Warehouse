import pandas as pd
from pandas import DataFrame


def table_task_2(data: dict) -> DataFrame:
    """ Метод формирования таблицы согласно условию второй задачи"""

    df = pd.json_normalize(data, record_path='products', meta=[
        'warehouse_name',
        'highway_cost'
    ])

    df["income"] = df["price"] * df["quantity"]
    df["expenses"] = df["highway_cost"] * df["quantity"]
    df['profit'] = df['income'] + df['expenses']

    result_df = df.groupby('product').agg({
        'quantity': 'sum',
        'income': 'sum',
        'expenses': 'sum',
        'profit': 'sum'
    }).reset_index()

    return result_df
