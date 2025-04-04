import pandas as pd
import numpy as np

def abc_analys(df, index, cols):
    group_df = df.groupby(index).agg({col: 'sum' for col in cols})
    for col in cols:
        group_df[f'rel_{col}'] = group_df[col] / sum(group_df[col])
        group_df.sort_values(by=f'rel_{col}', ascending=False, inplace=True)
        group_df[f'cumsum_{col}'] = group_df[f'rel_{col}'].cumsum()
        group_df[f'{col}_abc'] = np.where(group_df[f'cumsum_{col}'] < 0.8, 'A', 
                                         np.where(group_df[f'cumsum_{col}'] < 0.95, 'B', 'C'))
    return group_df[[f'{col}_abc' for col in cols]]

'''В функцию передается исходный dataframe, index - название поля для группировки, cols - список полей для анализа.
На выходе мы получаем многомерный ABC анализ по каждому полю из cols.'''
