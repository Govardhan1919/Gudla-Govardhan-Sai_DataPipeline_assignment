def validate_data(df):

    print("\n--- DATA VALIDATION ---")

    # Check required columns
    required_columns = [
        "patient_id",
        "age",
        "gender",
        "department"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    # Check missing values
    print("\nMissing values:")
    print(df.isnull().sum())

    # Check duplicate records
    duplicates = df.duplicated().sum()
    print("\nDuplicate records:", duplicates)

    # Check age
    if "age" in df.columns:
        invalid_age = ((df["age"] < 0) | (df["age"] > 120)).sum()
        print("Invalid age records:", invalid_age)

    # Check Patient ID
    if df["patient_id"].isnull().any():
        print("Warning: Patient ID contains missing values")

    print("\nValidation completed")

    return df