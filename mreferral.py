import os
import json
import psycopg2
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


# Function to save referral data from JSON to the database
def save_data_to_db(referral_data_list):
    try:
        # Connect to the PostgreSQL database using the URL from .env
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()


        # SQL query to insert the generated data into the vercelreferrals table
        insert_query = """
            INSERT INTO vercelreferrals (
                e_referral_id, referral_datetime, clinician_name,
                clinician_contact_details, healthcare_provider_number,
                practice_name, practice_contact_details, secure_messaging_provider,
                secure_messaging_endpoint, patient_first_name, patient_last_name,
                patient_contact_details, patient_alternate_contact_name,
                patient_alternate_contact_details, target_organisation_name,
                target_faculty, referral_reason, medication_history,
                comorbidity, patient_dob, medicare_number, medicare_expiry,
                atsi_code, primary_language_code, additional_info,
                patient_full_address, patient_email, patient_postcode,
                patient_state, referral_status, referral_accepted_rejected_date
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s);
        """


        # Iterate over each referral record and insert it into the database
        for referral_data in referral_data_list:
            cursor.execute(insert_query, (
                referral_data['e_referral_id'],
                referral_data['referral_datetime'],
                referral_data['clinician_name'],
                referral_data['clinician_contact_details'],
                referral_data['healthcare_provider_number'],
                referral_data['practice_name'],
                referral_data['practice_contact_details'],
                referral_data['secure_messaging_provider'],
                referral_data['secure_messaging_endpoint'],
                referral_data['patient_first_name'],
                referral_data['patient_last_name'],
                referral_data['patient_contact_details'],
                referral_data['patient_alternate_contact_name'],
                referral_data['patient_alternate_contact_details'],
                referral_data['target_organisation_name'],
                referral_data['target_faculty'],
                referral_data['referral_reason'],
                referral_data['medication_history'],
                referral_data['comorbidity'],
                referral_data['patient_dob'],
                referral_data['medicare_number'],
                referral_data['medicare_expiry'],
                referral_data['atsi_code'],
                referral_data['primary_language_code'],
                referral_data['additional_info'],
                referral_data['patient_full_address'],
                referral_data['patient_email'],
                referral_data['patient_postcode'],
                referral_data['patient_state'],
                referral_data['referral_status'],
                referral_data['referral_accepted_rejected_date'],
            ))


        # Commit the transaction
        connection.commit()
        print(f"{len(referral_data_list)} records saved successfully!")


    except Exception as e:
        print(f"Error saving data to the database: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Main function to read the JSON file and save the data
def main():
    json_file_path = 'faker_synth_data.json'  # Make sure this file contains an array of records
   
    try:
        # Load the data from the JSON file
        with open(json_file_path, 'r') as file:
            referral_data_list = json.load(file)


        # Check if the loaded data is a list
        if isinstance(referral_data_list, list):
            # Save the data to the database
            save_data_to_db(referral_data_list)
        else:
            print("Error: The JSON data is not a list of referral records.")


    except FileNotFoundError:
        print(f"Error: The file {json_file_path} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {json_file_path}.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()