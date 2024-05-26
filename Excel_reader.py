import pandas as pd
from robot.api.deco  import keyword

@keyword
def read_excel(filepath):
    df = pd.read_excel(filepath,dtype=str)
    lst = []
    for cols in df.columns:
        lst.append(cols)

    return lst