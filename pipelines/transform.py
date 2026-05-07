from utils.validation import validate_not_null
from utils.helpers import timer

@timer
def transform_data(df):
    df["value"] = df["value"].fillna(0)
    validate_not_null(df, "value")
    return df

