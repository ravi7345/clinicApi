# Clinic API

This is a Django-based API for managing clinic data, including doctors, patients, and reports.

## Getting Started

These instructions will guide you on setting up and running the API on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following software installed on your machine:

- Python (version 3.6 or higher)
- Django (version 3.2 or higher)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/ravi7345/clinicApi.git
2. Navigate to the project directory:

   ```bash
   cd clinicApi

3. Activate a virtual environment (optional but recommended):

   ```bash
   source venv/scripts/activate


4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt

5. Apply database migrations:

   ```bash
   python manage.py migrate.

### Usage

# Start the development server:

    python manage.py runserver

# Access the API endpoints using a tool like cURL or a web client such as Postman.

    API Endpoints
    POST: /doctors/register - Register a new doctor by providing a username
    and password.
    POST: /doctors/login - Authenticate the doctor and return a JWT (JSON Web
    Token) to be used for subsequent requests.
    POST: /patients/register - Register a new patient by providing the necessary
    details (e.g., phone number).
    POST: /patients/:id/create_report - Create a patient report for a specific
    patient ID.
    GET: /patients/:id/all_reports - Retrieve all the reports of a patient, ordered
    from oldest to latest.
    GET: /reports/:status - Retrieve all the reports of all patients filtered by a
    specific status.
    Please refer to the API documentation or code implementation for more details on request and response formats.