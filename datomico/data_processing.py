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


def correct_state_ids(df, df_column=None):
    mx_json_order = {"Entidad_Federativa":
                     ["Aguascalientes", "Baja California",
                      "Baja California Sur", "Campeche", "Coahuila",
                      "Colima", "Chiapas", "Chihuahua", "Ciudad de México",
                      "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco",
                      "México", "Michoacán", "Morelos", "Nayarit", "Nuevo León",
                      "Oaxaca", "Puebla", "Queretaro", "Quintana Roo",
                      "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco",
                      "Tamaulipas", "Tlaxcala",
                      "Veracruz", "Yucatán", "Zacatecas"],
                     "state": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                               15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                               27, 28, 29, 30, 31, 32]
                     }
    correct = pd.DataFrame.from_dict(mx_json_order)
    df = df.merge(correct, on="Entidad_Federativa")
    try:
        df.drop(df_column, axis=1, inplace=True)
    except ValueError:
        print("Favor de proveer el nombre de la columna que \
              contiene los ids de los estados en tu df")
    return df


def df_to_d3map(df, columns):
    """
    It gives you the df ready to put alongside mx.json fro d3
    Parameters
    -----------
    df: df to process
    columns: a list of the desired columns
    Example:
    df_to_d3(df, ["state", "TPV"])
    """
    df = df[columns]
    return df
