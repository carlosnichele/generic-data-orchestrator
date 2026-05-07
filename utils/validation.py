import pandas as pd
import logging

logger = logging.getLogger("validation")

def validate_not_null(df: pd.DataFrame, column: str):
    """
    Basic data quality check: ensures no null values in a column.
    """
    null_count = df[column].isnull().sum()
    if null_count > 0:
        logger.warning(f"Column '{column}' contains {null_count} null values.")
    else:
        logger.info(f"Column '{column}' passed NOT NULL validation.")

def validate_positive(df: pd.DataFrame, column: str):
    """
    Ensures numeric values are positive.
    """
    invalid = (df[column] < 0).sum()
    if invalid > 0:
        logger.warning(f"Column '{column}' contains {invalid} negative values.")
    else:
        logger.info(f"Column '{column}' passed POSITIVE validation.")
