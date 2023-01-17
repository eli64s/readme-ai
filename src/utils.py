"""
src/utils.py
"""
from typing import Dict

import pandas as pd


def dict_to_df(data: Dict[str, str]) -> pd.DataFrame:
    df = pd.DataFrame()
    df = df.append(data, ignore_index=True)
    return df
