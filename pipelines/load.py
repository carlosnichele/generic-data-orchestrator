from utils.db import insert_rows
from utils.helpers import timer

@timer
def load_data(df):
    insert_rows("target_table", df)
