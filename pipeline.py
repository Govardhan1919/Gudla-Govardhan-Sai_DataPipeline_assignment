from extract import extract_data
from validate import validate_data
from transform import transform_data
from load import load_data


def run_pipeline():

    print("==============================")
    print("HOSPITAL ETL PIPELINE")
    print("==============================")

    # 1. Extract
    df = extract_data()

    # 2. Validate
    df = validate_data(df)

    # 3. Transform
    df = transform_data(df)

    # 4. Load
    load_data(df)

    print("\n==============================")
    print("ETL PIPELINE COMPLETED")
    print("==============================")


if __name__ == "__main__":
    run_pipeline()