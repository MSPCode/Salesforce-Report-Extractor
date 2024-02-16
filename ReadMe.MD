# Salesforce Report Downloader

This script allows you to download Salesforce reports directly into an Excel file using the `simple_salesforce` Python package and `pandas`. It connects to Salesforce, fetches the report data by its ID, and then saves this data to an Excel file.

## Prerequisites

Before running this script, ensure you have the following prerequisites installed:

- Python 3.x
- `simple_salesforce` package
- `pandas` package

You can install the required packages using pip:

```bash
pip install simple_salesforce pandas
```

## Configuration

Update the Salesforce login credentials within the script before running it. You will need to provide:

```bash
username: Your Salesforce username.
password: Your Salesforce password.
security_token: Your Salesforce security token. This is required if your organization has IP restrictions.
is_sandbox: Set this to True if you are connecting to a sandbox environment, otherwise False.
report_id: The ID of the Salesforce report you wish to download.
```

## Usage

To use this script, simply run it with Python after configuring your Salesforce credentials and the report ID you wish to download:

```bash
python report_downloader.py
```

The script will connect to Salesforce, download the specified report, and save it as an Excel file in the same directory where the script is located. The name of the Excel file will be the Salesforce report name with spaces replaced by underscores.

## Security

Ensure that your credentials are not included in version control to prevent unauthorized access to your Salesforce credentials.

## Note

This script is meant for educational purposes and should be used responsibly. Ensure you have the necessary permissions to access and download the specified Salesforce report.

## License

MIT
