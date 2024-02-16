from simple_salesforce import Salesforce
import pandas as pd

# Salesforce login credentials
username = 'your_username'
password = 'your_password'
is_sandbox = True
security_token = ''
domain = 'test' if is_sandbox else None

# Replace 'your_report_id_here' with the actual Report ID
report_id = '00O8b00001234567890'

# Initialize Salesforce connection
sf = Salesforce(username=username, password=password, security_token=security_token, domain=domain)

def download_salesforce_report(report_id):
    # Fetch the report metadata
    report_metadata = sf.restful(f"analytics/reports/{report_id}")
    
    # Extract report name for the file name
    report_name = report_metadata['attributes']['reportName'].replace(' ', '_')
    
    # Fetch the report data without 'includeDetails' to get metadata for headers
    report_data = sf.restful(f"analytics/reports/{report_id}")
    
    # Extract column headers from 'detailColumnInfo'
    detail_column_info = report_data['reportExtendedMetadata']['detailColumnInfo']
    headers = [detail_column_info[key]['label'] for key in detail_column_info]
    
    # Extract report rows
    report_rows = report_data['factMap']['T!T']['rows']
    
    # Initialize a list to hold formatted rows
    formatted_rows = []
    
    # Iterate over each row in the report
    for row in report_rows:
        # Extract 'dataCells' from each row
        data_cells = row['dataCells']
        # For each cell, extract the 'value'
        formatted_row = [cell['label'] for cell in data_cells]
        # Append the formatted row to the list
        formatted_rows.append(formatted_row)
    
    # Convert the list of rows into a DataFrame with extracted headers
    df = pd.DataFrame(formatted_rows, columns=headers)
    
    # Define Excel file name using the report name
    excel_file = f"{report_name}.xlsx"
    
    # Write DataFrame to an Excel file
    df.to_excel(excel_file, index=False)
    
    print(f"Report '{report_name}' has been saved to '{excel_file}'.")

download_salesforce_report(report_id)
