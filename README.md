# Elucidat - "FINDING THE TRUTH" - Test Automation Framework

  A test framework for Elucidat.
  
  UI tests:
    Navigate to the start page
    Ensure the currrent score is an integer
    Navigate to a Case
    Navigate through a Case
    Ensure vote cannot be cast without selecting a radiobutton
  API tests (Unimplemented):
    List projects
    Count Releases on a Project
    Get Release details
	
# Setup Instructions

  Follow these steps to set up the project environment.

## Clone the repository
    git clone https://github.com/tlit/elucidat_testframework

    cd elucidat_testframework

## Create a virtual environment
    python -m venv venv

## Activate the virtual environment
### On Windows
    venv\Scripts\activate
### On macOS/Linux
    source venv/bin/activate

## Install dependencies
    pip install -r requirements.txt

## Run the tests; JSON logs will appears in the 'reports' folder
    behave --junit --junit-directory reports
