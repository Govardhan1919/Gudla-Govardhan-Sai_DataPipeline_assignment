import pandas as pd


def transform_data(df):

    print("\n--- DATA TRANSFORMATION ---")

    df = df.copy()

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove records without Patient ID
    df = df.dropna(subset=["patient_id"])

    # Convert numeric columns
    numeric_columns = [
        "age",
        "glucose",
        "cholesterol",
        "heart_rate",
        "spo2",
        "temperature"
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column].astype(str).str.extract(r"([-+]?\d*\.?\d+)")[0],
                errors="coerce"
            )

    # Validate age
    df.loc[
        (df["age"] < 0) | (df["age"] > 120),
        "age"
    ] = None

    # Convert date/time
    datetime_columns = [
        "appointment_time",
        "consultation_start_time"
    ]

    for column in datetime_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    # Calculate waiting time
    df["waiting_time"] = (
        df["consultation_start_time"]
        - df["appointment_time"]
    ).dt.total_seconds() / 60

    # Fill missing numeric values with median
    for column in numeric_columns:
        if column in df.columns:
            df[column] = df[column].fillna(
                df[column].median()
            )

    # Fill missing text values
    text_columns = [
        "gender",
        "doctor",
        "department",
        "diagnosis",
        "treatment"
    ]

    for column in text_columns:
        if column in df.columns:
            df[column] = df[column].fillna("Unknown")

    print("Transformation completed")

    return df