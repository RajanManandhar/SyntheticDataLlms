import json
import ollama  # Ensure this import works without errors


# Function to generate synthetic referral data using Ollama
def generate_referral():
    prompt = """
    Generate a synthetic referral record for a patient from Australia with the following fields.
    - e_referral_id: a unique referral ID
    - referral_datetime: a timestamp in ISO format
    - clinician_name: a fictional clinician name
    - clinician_contact_details: a fictional phone number
    - healthcare_provider_number: a fictional provider number
    - practice_name: a fictional medical practice name
    - practice_contact_details: a fictional practice phone number
    - secure_messaging_provider: a fictional secure messaging provider
    - secure_messaging_endpoint: a URL for the messaging provider
    - patient_first_name: a fictional first name
    - patient_last_name: a fictional last name
    - patient_contact_details: a fictional phone number
    - patient_alternate_contact_name: a fictional alternate contact name
    - patient_alternate_contact_details: a fictional alternate contact phone number
    - target_organisation_name: a fictional organization name
    - target_faculty: a fictional faculty name
    - referral_reason: a fictional reason for the referral
    - medication_history: a fictional medication history
    - comorbidity: a fictional comorbidity
    - patient_dob: a fictional date of birth
    - medicare_number: a fictional Medicare number
    - medicare_expiry: a fictional expiration date for the Medicare card
    - atsi_code: a fictional ATSI code
    - primary_language_code: a fictional primary language code
    - additional_info: additional notes
    - patient_full_address: a realistic full address in Australia
    - patient_email: a fictional email address
    - patient_postcode: a fictional postcode
    - patient_state: a fictional state in Australia
    - referral_status: a fictional status for the referral
    - referral_accepted_rejected_date: a timestamp for acceptance or rejection
    """


    try:
        # Call Ollama to generate the data
        response = ollama.chat(model="llama2", messages=[{"role": "system", "content": prompt}])
       
        # Check if the response is valid
        if 'message' in response and 'content' in response['message']:
            generated_text = response['message']['content']
            return generated_text
        else:
            print("Error: The 'content' field is missing in the Ollama response.")
            return None
    except Exception as e:
        print(f"Error interacting with Ollama: {e}")
        return None


# Function to save the generated data to a JSON file
def save_data_to_json(data, filename='synth_data.json'):
    try:
        data_dict = {}
       
        for line in data.splitlines():
            line = line.strip()  # Remove leading and trailing whitespace
            if line:  # Ignore empty lines
                if ':' in line:  # Ensure the line contains a colon
                    key, value = line.split(':', 1)  # Split only on the first occurrence of ':'
                    data_dict[key.strip()] = value.strip()  # Clean and store the key-value pair
                else:
                    print(f"Skipping line due to unexpected format: {line}")
       
        with open(filename, 'w') as json_file:
            json.dump(data_dict, json_file, indent=4)
       
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving data to JSON: {e}")


# Main function to generate and save referral data
def main():
    generated_data = generate_referral()
   
    if generated_data:
        save_data_to_json(generated_data)


if __name__ == "__main__":
    main()
