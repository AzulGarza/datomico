import pandas as pd
import numpy as np


def read_tables(table_names):
    """Read a bunch of files listed in table_names and
    return a list with the files for latter processing"""
    tables = [pd.read_csv(f'{PATH}{fname}.csv') for fname in table_names]
    return tables


def convert_types(df):
    """ Assign apropiate type of df columns for memory
    reduction """
    for c in df:

        if (df[c].dtype == 'object') and (df[c].nunique() < df.shape[0]):
            df[c] = df[c].astype('category')

        elif set(df[c].unique()) == {0, 1}:
            df[c] = df[c].astype(bool)

        elif df[c].dtype == float:
            df[c] = df[c].astype(np.float32)

        elif df[c].dtype == int:
            df[c] = df[c].astype(np.int32)

    return df
