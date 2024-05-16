# Elucidat - "FINDING THE TRUTH" - Test Automation Framework

A test framework for Elucidat.

## Setup Instructions

Follow these steps to set up the project environment.

# Clone the repository
git clone https://github.com/tlit/elucidat_testframework

cd elucidat_testframework

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the tests
behave
