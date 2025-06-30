## Prerequisites

- Python 3.9 or higher installed
- pip (Python package installer)

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/Khant-haythi/companywebsite.git
cd your-repo

### 2. Create and activate a virtual environment

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

On Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1

### 3. Install dependencies

pip install -r requirements.txt

### 4. Apply migrations

python manage.py migrate

### 5. Create a superuser (optional, for admin access)

python manage.py createsuperuser

### 6. Run the development server

python manage.py runserver