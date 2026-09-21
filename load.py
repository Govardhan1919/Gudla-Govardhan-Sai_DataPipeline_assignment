import mysql.connector
import pandas as pd

from config import (
    DB_HOST,
    DB_USER,
    DB_PASSWORD,
    DB_NAME
)


def load_data(df):

    print("\n--- LOADING DATA ---")

    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    cursor = connection.cursor()

    query = """
    INSERT INTO patient_data (
        patient_id,
        age,
        gender,
        doctor,
        department,
        appointment_time,
        consultation_start_time,
        waiting_time,
        glucose,
        cholesterol,
        heart_rate,
        spo2,
        temperature,
        diagnosis,
        treatment
    )
    VALUES (
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s
    )
    """

    for _, row in df.iterrows():

        values = (
            row["patient_id"],
            row["age"],
            row["gender"],
            row["doctor"],
            row["department"],
            row["appointment_time"],
            row["consultation_start_time"],
            row["waiting_time"],
            row["glucose"],
            row["cholesterol"],
            row["heart_rate"],
            row["spo2"],
            row["temperature"],
            row["diagnosis"],
            row["treatment"]
        )

        # Convert pandas NaN / NaT to Python None
        values = tuple(
            None if pd.isna(value) else value
            for value in values
        )

        cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    print("Data loaded successfully into MySQL")