from orchestrator.scheduler import Scheduler
from pipelines.extract import extract_data
from pipelines.transform import transform_data
from pipelines.load import load_data
from orchestrator.logger import get_logger

logger = get_logger()

def run_pipeline():
    logger.info("Starting ETL pipeline")

    df = extract_data()
    df = transform_data(df)
    load_data(df)

    logger.info("Pipeline completed successfully")

if __name__ == "__main__":
    Scheduler().run(run_pipeline)
