import logging
import pandas as pd

# Simulated database connection (generic and safe)
class DatabaseClient:
    def __init__(self):
        self.logger = logging.getLogger("db")

    def insert_rows(self, table_name: str, df: pd.DataFrame):
        """
        Simulates inserting rows into a database table.
        This is a safe, generic implementation for demonstration purposes.
        """
        self.logger.info(f"Inserting {len(df)} rows into table '{table_name}'")
        # Simulated insert
        for _, row in df.iterrows():
            pass  # No real DB operations here

        self.logger.info(f"Insert completed for table '{table_name}'")

# Global instance
db_client = DatabaseClient()

def insert_rows(table_name: str, df: pd.DataFrame):
    """
    Public function used by the ETL pipeline.
    """
    db_client.insert_rows(table_name, df)
