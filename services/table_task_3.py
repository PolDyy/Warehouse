import pandas as pd


def table_task_3(data: dict) -> tuple:
    """ Метод формирования таблицы согласно условию третьей задачи"""

    df = pd.json_normalize(data, record_path='products', meta=[
        'order_id',
        'highway_cost'
    ])

    df["order_profit"] = (df["price"] - df["highway_cost"]) * df["quantity"]
    df = df.groupby('order_id').agg({
        'order_profit': 'sum'
    }).reset_index()
    result_df = df[['order_id', 'order_profit']]

    average_profit = result_df['order_profit'].mean()

    return result_df, average_profit
