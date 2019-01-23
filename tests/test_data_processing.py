import pandas as pd
from datomico.data_processing import addr_to_lat_log

df = pd.read_csv('andrea_230119.csv', encoding='latin-1')

def test_addrtolatlong(df=df):
    geocode = addr_to_lat_log(df, Number='Número', Street='Calle (Búsqueda)', Col="Colonia")
    
    assert len(df) == len(geocode)