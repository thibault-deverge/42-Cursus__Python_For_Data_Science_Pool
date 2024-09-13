import pandas as pd
from pandas.errors import EmptyDataError, ParserError


def load(path: str) -> pd.DataFrame:
    '''Load csv data file, print its dimensions and return it'''
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except FileNotFoundError as error:
        print(f'FileNotFoundError: {error}')
    except EmptyDataError as error:
        print(f'EmptyDataError: {error}')
    except ParserError as error:
        print(f'ParserError: {error}')
    except Exception as error:
        print(f'error: {error}')
    return None
