import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


# Connect to the database
connection = psycopg2.connect(os.getenv("DATABASE_URL"))
cursor = connection.cursor()


# Data to insert
data = {
    "e_referral_id": "E12345",
    "referral_datetime": "2024-09-23 10:00:00",
    "clinician_name": "Dr. John Doe",
    "clinician_contact_details": "555-1234",
    "healthcare_provider_number": "HCP12345",
    "practice_name": "my Clinic",
    "practice_contact_details": "555-5678",
    "secure_messaging_provider": "ProviderX",
    "secure_messaging_endpoint": "endpoint123",
    "patient_first_name": "Jane",
    "patient_last_name": "Doe",
    "patient_contact_details": "555-8765",
    "patient_alternate_contact_name": "John Smith",
    "patient_alternate_contact_details": "555-4321",
    "target_organisation_name": "General Hospital",
    "target_faculty": "Cardiology",
    "referral_reason": "Routine Checkup",
    "medication_history": "None",
    "comorbidity": "Hypertension",
    "patient_dob": "1985-08-15",
    "medicare_number": "123456789",
    "medicare_expiry": "2025-09-23",
    "atsi_code": "N",
    "primary_language_code": "EN",
    "additional_info": "No known allergies",
    "patient_full_address": "123 Main St, Sydney",
    "patient_email": "jane.doe@example.com",
    "patient_postcode": "2000",
    "patient_state": "NSW",
    "referral_status": "Pending",
    "referral_accepted_rejected_date": None
}


# SQL query to insert data
query = sql.SQL("""
    INSERT INTO Vercelreferrals (
        e_referral_id, referral_datetime, clinician_name, clinician_contact_details, healthcare_provider_number,
        practice_name, practice_contact_details, secure_messaging_provider, secure_messaging_endpoint, patient_first_name,
        patient_last_name, patient_contact_details, patient_alternate_contact_name, patient_alternate_contact_details,
        target_organisation_name, target_faculty, referral_reason, medication_history, comorbidity, patient_dob,
        medicare_number, medicare_expiry, atsi_code, primary_language_code, additional_info, patient_full_address,
        patient_email, patient_postcode, patient_state, referral_status, referral_accepted_rejected_date
    ) VALUES (
        {e_referral_id}, {referral_datetime}, {clinician_name}, {clinician_contact_details}, {healthcare_provider_number},
        {practice_name}, {practice_contact_details}, {secure_messaging_provider}, {secure_messaging_endpoint}, {patient_first_name},
        {patient_last_name}, {patient_contact_details}, {patient_alternate_contact_name}, {patient_alternate_contact_details},
        {target_organisation_name}, {target_faculty}, {referral_reason}, {medication_history}, {comorbidity}, {patient_dob},
        {medicare_number}, {medicare_expiry}, {atsi_code}, {primary_language_code}, {additional_info}, {patient_full_address},
        {patient_email}, {patient_postcode}, {patient_state}, {referral_status}, {referral_accepted_rejected_date}
    );
""").format(
    **{key: sql.Literal(value) for key, value in data.items()}
)


try:
    cursor.execute(query)
    connection.commit()
    print("Data inserted successfully!")
except Exception as e:
    print("Error inserting data:", e)
finally:
    cursor.close()
    connection.close()
